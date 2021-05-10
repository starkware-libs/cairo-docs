import dataclasses
import random
from collections.abc import Iterable
from typing import List, Sequence

from starkware.cairo.common.structs import CairoStructFactory
from starkware.cairo.lang.builtins.hash.hash_builtin_runner import CELLS_PER_HASH, HashBuiltinRunner
from starkware.cairo.lang.builtins.range_check.range_check_builtin_runner import (
    RangeCheckBuiltinRunner)
from starkware.cairo.lang.builtins.signature.signature_builtin_runner import (
    CELLS_PER_SIGNATURE, SignatureBuiltinRunner)
from starkware.cairo.lang.compiler.identifier_definition import LabelDefinition
from starkware.cairo.lang.compiler.program import Program
from starkware.cairo.lang.compiler.scoped_name import ScopedName
from starkware.cairo.lang.tracer.tracer import trace_runner
from starkware.cairo.lang.vm.cairo_runner import CairoRunner, process_ecdsa, verify_ecdsa_sig
from starkware.cairo.lang.vm.output_builtin_runner import OutputBuiltinRunner
from starkware.cairo.lang.vm.relocatable import MaybeRelocatable, RelocatableValue
from starkware.cairo.lang.vm.security import SecurityError, verify_secure_runner
from starkware.cairo.lang.vm.vm import VmException
from starkware.crypto.signature.signature import pedersen_hash


@dataclasses.dataclass
class ExpectedBuiltinUsage:
    n_hashes: int = 0
    n_range_checks: int = 0
    n_signatures: int = 0
    n_output_cells: int = 0

    def __add__(self, other):
        if not isinstance(other, ExpectedBuiltinUsage):
            return NotImplemented
        return ExpectedBuiltinUsage(
            n_hashes=self.n_hashes + other.n_hashes,
            n_range_checks=self.n_range_checks + other.n_range_checks,
            n_signatures=self.n_signatures + other.n_signatures,
            n_output_cells=self.n_output_cells + other.n_output_cells,
        )

    @property
    def hash_cells(self):
        """
        Returns the number of cells used by the hash builtin.
        """
        return self.n_hashes * CELLS_PER_HASH

    @property
    def signature_cells(self):
        """
        Returns the number of cells used by the signature builtin.
        """
        return self.n_signatures * CELLS_PER_SIGNATURE


def expected_builtin_usage_merkle_update(tree_height: int):
    """
    Returns the expected builtin usage due to a call to merkle_update.
    """
    # Merkle update uses two hash builtins per tree level, for computing the previous and new value
    # of each node along the path from the leaf to the root.
    return ExpectedBuiltinUsage(n_hashes=2 * tree_height)


def compute_merkle(leaf: int, auth_path: List[int], index: int, hash_func):
    """
    Computes the root of a Merkle tree, given a value of a leaf along with its index, and the
    corresponding authentication path from the root (non-inclusive) to the leaf.
    """
    for sibling in auth_path[::-1]:
        if index & 1 == 0:
            leaf = hash_func(leaf, sibling)
        else:
            leaf = hash_func(sibling, leaf)
        index //= 2
    assert index == 0
    return leaf


def compute_merkle_from_leaves(layer, hash_func):
    while len(layer) > 1:
        layer = [hash_func(x, y) for x, y in zip(layer[::2], layer[1::2])]
    return layer[0]


def create_memory_struct(runner, data: Sequence[int]):
    """
    Stores a given sequence of field elements in the VM memory in a new segment.
    Can be used to pass a struct pointer as a function argument.
    """
    base = runner.segments.add()
    runner.load_data(base, data)
    return base


def rand_value_with_collisions(BOUND, collision_bound=8):
    """
    Generates a uniform random number with probability 0.5 and a random number in the range
    [0, collision_bound) with probability 0.5. This way, high numbers will be generated, but also a
    lot of collisions.
    """
    return random.randrange(random.choice([collision_bound, BOUND]))


class CairoFunctionRunner(CairoRunner):
    def __init__(self, program, layout='plain'):
        super().__init__(program=program, layout=layout)
        hash_builtin = HashBuiltinRunner(
            name='pedersen', included=True, ratio=32, hash_func=pedersen_hash)
        self.builtin_runners['hash_builtin'] = hash_builtin
        range_check_builtin = RangeCheckBuiltinRunner(
            included=True, ratio=None, inner_rc_bound=2 ** 16, n_parts=8)
        self.builtin_runners['range_check_builtin'] = range_check_builtin
        output_builtin = OutputBuiltinRunner(included=True)
        self.builtin_runners['output_builtin'] = output_builtin
        signature_builtin = SignatureBuiltinRunner(
            name='ecdsa', included=True, ratio=None, process_signature=process_ecdsa,
            verify_signature=verify_ecdsa_sig)
        self.builtin_runners['ecdsa_builtin'] = signature_builtin
        self.initialize_segments()

    @property
    def hash_builtin(self) -> HashBuiltinRunner:
        return self.builtin_runners['hash_builtin']

    @property
    def range_check_builtin(self) -> RangeCheckBuiltinRunner:
        return self.builtin_runners['range_check_builtin']

    @property
    def output_builtin(self) -> OutputBuiltinRunner:
        return self.builtin_runners['output_builtin']

    @property
    def ecdsa_builtin(self) -> SignatureBuiltinRunner:
        return self.builtin_runners['ecdsa_builtin']

    def assert_eq(self, arg: MaybeRelocatable, expected_value, apply_modulo=True):
        """
        Assert that arg is the cairo representation of expected_value.
        If the expected_value is Iterable then arg is interpreted as a pointer to a list
        and assert_eq is called recursively on all the items in the expected_value.
        If apply_modulo=True, all the integers are taken modulo the program's prime.
        """
        assert isinstance(arg, (int, RelocatableValue)), f'Expecting MaybeRelocatable got {arg}'

        if isinstance(expected_value, Iterable):
            for idx, value in enumerate(expected_value):
                self.assert_eq(self.vm_memory[arg + idx], value, apply_modulo=apply_modulo)
            return
        if apply_modulo and isinstance(arg, int):
            expected_value = expected_value % self.program.prime

        assert arg == expected_value

    def run(
            self, func_name, *args, hint_locals={}, verify_secure=True, trace_on_failure=False,
            apply_modulo_to_args=True, use_full_name=False, **kwargs):
        """
        Runs func_name(*args).
        args are converted to Cairo-friendly ones using gen_arg.

        Additional params:
        verify_secure - run verify_secure_runner to do extra verifications.
        trace_on_failure - Run the tracer in case of failure to help debugging.
        apply_modulo_to_args - Apply modulo operation on integer arguments.
        use_full_name - Treat func_name as a fully qualified identifer name, instance of a relative
          one.
        """

        structs_factory = CairoStructFactory(self.program)
        full_args_struct = structs_factory.build_func_args(ScopedName.from_string(func_name))
        all_args = full_args_struct(*args, **kwargs)
        real_args = [self.gen_arg(x, apply_modulo_to_args) for x in all_args]
        if use_full_name:
            assert isinstance(self.program, Program)
            identifier = self.program.identifiers.get_by_full_name(
                name=ScopedName.from_string(func_name))
            assert isinstance(identifier, LabelDefinition)
            entrypoint = identifier.pc
        else:
            entrypoint = func_name
        end = self.initialize_function_entrypoint(entrypoint=entrypoint, args=real_args)
        self.initialize_vm(hint_locals=hint_locals)
        try:
            self.run_until_pc(end)
            self.end_run()

            if verify_secure:
                verify_secure_runner(runner=self, verify_builtins=False)
        except (VmException, SecurityError, AssertionError) as ex:
            if trace_on_failure:
                print(f"""\
Got {type(ex).__name__} exception during the execution of {func_name}:
{str(ex)}
""")
                trace_runner(runner=self)
            raise

    def get_return_values(self, n_ret):
        return self.vm_memory.get_range(self.vm.run_context.ap - n_ret, n_ret)
