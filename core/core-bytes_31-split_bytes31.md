# split_bytes31

Splits a `bytes31` into two `bytes31`s at the given index (LSB's index is 0). The input `bytes31` and the output `bytes31`s are represented using `felt252`s to improve performance.  Note: this function assumes that: 1. `word` is validly convertible to a `bytes31`` which has no more than `len`bytes of data. 2.`index <= len`. 3. `len <= BYTES_IN_BYTES31`. If these assumptions are not met, it can corrupt the `byte31`s. Thus, this should be a private function. We could add masking/assertions but it would be more expansive.

Fully qualified path: `core::bytes_31::split_bytes31`

```rust
pub(crate) fn split_bytes31(word: felt252, len: usize, index: usize) -> (felt252, felt252)
```

