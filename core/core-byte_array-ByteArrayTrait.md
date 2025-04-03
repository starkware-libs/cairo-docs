# ByteArrayTrait

Fully qualified path: `core::byte_array::ByteArrayTrait`

```rust
pub trait ByteArrayTrait
```

## Trait functions

### append_word

Appends a single word of `len` bytes to the end of the `ByteArray`.  This function assumes that: 1. `word` could be validly converted to a `bytes31` which has no more than `len` bytes    of data. 2. len <= BYTES_IN_BYTES31.  If these assumptions are not met, it can corrupt the `ByteArray`. Thus, this should be a private function. We could add masking/assertions but it would be more expensive.  # Examples
```cairo
let mut ba = "";
ba.append_word('word', 4);
assert!(ba == "word");
```

Fully qualified path: `core::byte_array::ByteArrayTrait::append_word`

```rust
fn append_word(ref self: ByteArray, word: felt252, len: usize)
```


### append

Appends a `ByteArray` to the end of another `ByteArray`.  # Examples
```cairo
let mut ba: ByteArray = "1";
ba.append(@"2");
assert!(ba == "12");
```

Fully qualified path: `core::byte_array::ByteArrayTrait::append`

```rust
fn append(ref self: ByteArray, other: @ByteArray)
```


### concat

Concatenates two `ByteArray` and returns the result.  The content of `left` is cloned in a new memory segment. # Examples
```cairo
let ba = "1";
let other_ba = "2";
let result = ByteArrayTrait::concat(@ba, @other_ba);
assert!(result == "12");
```

Fully qualified path: `core::byte_array::ByteArrayTrait::concat`

```rust
fn concat(left: @ByteArray, right: @ByteArray) -> ByteArray
```


### append_byte

Appends a single byte to the end of the `ByteArray`.  # Examples
```cairo
let mut ba = "";
ba.append_byte(0);
assert!(ba == "0");
```

Fully qualified path: `core::byte_array::ByteArrayTrait::append_byte`

```rust
fn append_byte(ref self: ByteArray, byte: u8)
```


### len

Returns the length of the `ByteArray`.  # Examples
```cairo
let ba: ByteArray = "byte array";
let len = ba.len();
assert!(len == 10);
```

Fully qualified path: `core::byte_array::ByteArrayTrait::len`

```rust
fn len(self: @ByteArray) -> usize
```


### at

Returns an option of the byte at the given index of `self` or `Option::None` if the index is out of bounds.  # Examples
```cairo
let ba: ByteArray = "byte array";
let byte = ba.at(0).unwrap();
assert!(byte == 98);
```

Fully qualified path: `core::byte_array::ByteArrayTrait::at`

```rust
fn at(self: @ByteArray, index: usize) -> Option<u8>
```


### rev

Returns a `ByteArray` with the reverse order of `self`.  # Examples
```cairo
let ba: ByteArray = "123";
let rev_ba = ba.rev();
assert!(rev_ba == "321");
```

Fully qualified path: `core::byte_array::ByteArrayTrait::rev`

```rust
fn rev(self: @ByteArray) -> ByteArray
```


### append_word_rev

Appends the reverse of the given word to the end of `self`.  This function assumes that: 1. len < 31 2. word is validly convertible to bytes31 of length `len`.  # Examples
```cairo
let mut ba: ByteArray = "";
ba.append_word_rev('123', 3);
assert!(ba == "321");
```

Fully qualified path: `core::byte_array::ByteArrayTrait::append_word_rev`

```rust
fn append_word_rev(ref self: ByteArray, word: felt252, len: usize)
```


### append_word_fits_into_pending

Appends a single word of `len` bytes to the end of the `ByteArray`, assuming there is enough space in the pending word (`self.pending_word_len + len < BYTES_IN_BYTES31`).  `word` is of type `felt252` but actually represents a `bytes31`. It is represented as a `felt252` to improve performance of building the `ByteArray`.

Fully qualified path: `core::byte_array::ByteArrayTrait::append_word_fits_into_pending`

```rust
fn append_word_fits_into_pending(ref self: ByteArray, word: felt252, len: usize)
```


### append_split_index_lt_16

Appends a single word to the end of `self`, given that `0 < split_index < 16`.  `split_index` is the number of bytes left in `self.pending_word` after this function. This is the index of the split (LSB's index is 0).  Note: this function doesn't update the new pending length of `self`. It's the caller's responsibility.

Fully qualified path: `core::byte_array::ByteArrayTrait::append_split_index_lt_16`

```rust
fn append_split_index_lt_16(ref self: ByteArray, word: felt252, split_index: usize)
```


### append_split_index_16

Appends a single word to the end of `self`, given that the index of splitting `word` is exactly 16.  `split_index` is the number of bytes left in `self.pending_word` after this function. This is the index of the split (LSB's index is 0).  Note: this function doesn't update the new pending length of `self`. It's the caller's responsibility.

Fully qualified path: `core::byte_array::ByteArrayTrait::append_split_index_16`

```rust
fn append_split_index_16(ref self: ByteArray, word: felt252)
```


### append_split_index_gt_16

Appends a single word to the end of `self`, given that the index of splitting `word` is > 16.  `split_index` is the number of bytes left in `self.pending_word` after this function. This is the index of the split (LSB's index is 0).  Note: this function doesn't update the new pending length of `self`. It's the caller's responsibility.

Fully qualified path: `core::byte_array::ByteArrayTrait::append_split_index_gt_16`

```rust
fn append_split_index_gt_16(ref self: ByteArray, word: felt252, split_index: usize)
```


### append_split

A helper function to append a remainder to `self`, by: 1. completing `self.pending_word` to a full word using `complete_full_word`, assuming it's    validly convertible to a `bytes31` of length exactly `BYTES_IN_BYTES31 -    self.pending_word_len`. 2. Setting `self.pending_word` to `new_pending`.  Note: this function doesn't update the new pending length of `self`. It's the caller's responsibility.

Fully qualified path: `core::byte_array::ByteArrayTrait::append_split`

```rust
fn append_split(ref self: ByteArray, complete_full_word: felt252, new_pending: felt252)
```


