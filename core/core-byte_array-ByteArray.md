# ByteArray

Byte array type.

Fully qualified path: `core::byte_array::ByteArray`

```rust
#[derive(Drop, Clone, PartialEq, Serde, Default)]
pub struct ByteArray {
    pub(crate) data: Array<bytes31>,
    pub(crate) pending_word: felt252,
    pub(crate) pending_word_len: usize,
}
```

