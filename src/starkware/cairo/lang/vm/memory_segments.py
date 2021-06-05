from collections import defaultdict
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

from starkware.cairo.lang.vm.memory_dict import MemoryDict
from starkware.cairo.lang.vm.relocatable import MaybeRelocatable, RelocatableValue

FIRST_MEMORY_ADDR = 1


class MemorySegmentManager:
    """
    Manages the list of memory segments, and allows relocating them once their sizes are known.
    """

    def __init__(self, memory: MemoryDict, prime: int):
        self.memory = memory
        self.prime = prime
        # Number of segments.
        self.n_segments = 0
        # A map from segment index to its size.
        self.segment_sizes: Dict[int, int] = {}
        # A map from segment index to a list of pairs (offset, page_id) that constitute the
        # public memory. Note that the offset is absolute (not based on the page_id).
        self.public_memory_offsets: Dict[int, List[Tuple[int, int]]] = {}
        # The number of temporary segments, see 'add_temp_segment' for more details.
        self.n_temp_segments = 0

    def add(self, size: Optional[int] = None) -> RelocatableValue:
        """
        Adds a new segment and returns its starting location as a RelocatableValue.

        If size is not None the segment is finalized with the given size.
        """
        segment_index = self.n_segments
        self.n_segments += 1
        if size is not None:
            self.finalize(segment_index, size)
        return RelocatableValue(segment_index=segment_index, offset=0)

    def add_temp_segment(self) -> RelocatableValue:
        """
        Adds a new temporary segment and returns its starting location as a RelocatableValue.

        A temporary segment is a segment that is relocated before the cairo pie is produced.
        """

        self.n_temp_segments += 1
        # Temporary segments have negative segment indices that start from -1.
        segment_index = -self.n_temp_segments

        return RelocatableValue(segment_index=segment_index, offset=0)

    def finalize(
            self, segment_index: int, size: int, public_memory: Sequence[Tuple[int, int]] = []):
        """
        Writes the following information for the given segment:
        * size - The size of the segment (to be used in relocate_segments).
        * public_memory - A list of offsets for memory cells that will be considered as public
        memory.
        """
        self.segment_sizes[segment_index] = size
        self.public_memory_offsets[segment_index] = list(public_memory)

    def finalize_all_by_effective_size(self):
        """
        Finalizes all segments that were not finalized yet, by computing their current used size.
        """
        segment_index_to_max_offset = get_segment_index_to_max_offset(memory=self.memory)
        for segment_index in range(self.n_segments):
            if segment_index in self.segment_sizes:
                # Segment was already finalized.
                continue

            assert segment_index not in self.public_memory_offsets
            self.segment_sizes[segment_index] = segment_index_to_max_offset[segment_index] + 1
            self.public_memory_offsets[segment_index] = []

    def relocate_segments(self) -> Dict[int, int]:
        current_addr = FIRST_MEMORY_ADDR
        res = {}
        for segment_index in range(self.n_segments):
            res[segment_index] = current_addr
            assert segment_index in self.segment_sizes, \
                f'Segment {segment_index} must be finalized.'
            current_addr += self.segment_sizes[segment_index]
        return res

    def get_public_memory_addresses(self, segment_offsets: Dict[int, int]) -> List[Tuple[int, int]]:
        """
        Returns a list of addresses of memory cells that constitute the public memory.
        segment_offsets should be the dictionary returned by relocate_segments().
        """
        res = []
        for segment_index in range(self.n_segments):
            offsets = self.public_memory_offsets[segment_index]
            segment_start = segment_offsets[segment_index]
            for offset, page_id in offsets:
                res.append((segment_start + offset, page_id))
        return res

    def initialize_segments_from(self, other: 'MemorySegmentManager'):
        """
        Adds the segments used by the given MemorySegmentManager.
        Note that this function must be called before any segments are added, to make the segment
        indices identical.
        """
        assert self.n_segments == 0, \
            'initialize_segments_from() must be called before segments are added.'
        self.n_segments = other.n_segments

    def load_data(self, ptr: MaybeRelocatable, data: Sequence[MaybeRelocatable]) -> \
            MaybeRelocatable:
        """
        Writes data into the memory at address ptr and returns the first address after the data.
        """
        for i, v in enumerate(data):
            self.memory[ptr + i] = v
        return ptr + len(data)

    def gen_arg(self, arg, apply_modulo_to_args=True):
        """
        Converts args to Cairo-friendly ones.
        If an argument is Iterable it is replaced by a pointer to a new segment containing the items
        in the Iterable arg (recursively).
        If apply_modulo_to_args=True, all the integers are taken modulo the program's prime.
        """
        if isinstance(arg, Iterable):
            base = self.add()
            self.write_arg(base, arg)
            return base
        if apply_modulo_to_args and isinstance(arg, int):
            return arg % self.prime
        return arg

    def write_arg(self, ptr, arg, apply_modulo_to_args=True):
        assert isinstance(arg, Iterable)
        data = [self.gen_arg(arg=x, apply_modulo_to_args=apply_modulo_to_args) for x in arg]
        return self.load_data(ptr, data)

    def get_memory_holes(self) -> int:
        """
        Returns the total number of memory holes in all segments.
        """
        used_offsets_sets: Dict[int, Set] = defaultdict(set)
        for addr in self.memory.keys():
            assert isinstance(addr, RelocatableValue), \
                f'Expected memory address to be relocatable value. Found: {addr}.'
            assert addr.offset >= 0, \
                f'Address offsets must be non-negative. Found: {addr.offset}.'
            used_offsets_sets[addr.segment_index].add(addr.offset)
        return sum(
            max(used_offsets) + 1 - len(used_offsets)
            for used_offsets in used_offsets_sets.values())


def get_segment_used_size(segment_index: int, memory: MemoryDict) -> int:
    """
    Returns the used size of the given memory segment by finding which is the maximal offset that
    was accessed.
    """
    max_offset = -1
    for addr in memory:
        assert isinstance(addr, RelocatableValue), \
            f'Expected memory address to be relocatable value. Found: {addr}.'
        if addr.segment_index != segment_index:
            continue
        max_offset = max(max_offset, addr.offset)
    return max_offset + 1


def get_segment_index_to_max_offset(memory: MemoryDict) -> Dict[int, int]:
    """
    Returns a mapping between the segment indices and the maximal offset that
    was accessed in each segment.
    """
    segment_index_to_max_offset: Dict[int, int] = defaultdict(lambda: -1)
    for addr in memory:
        assert isinstance(addr, RelocatableValue), \
            f'Expected memory address to be relocatable value. Found: {addr}.'
        previous_max_offset = segment_index_to_max_offset[addr.segment_index]
        segment_index_to_max_offset[addr.segment_index] = max(previous_max_offset, addr.offset)
    return segment_index_to_max_offset
