# BYTE_ARRAY_MAGIC

A magic constant for identifying serialization of `ByteArray` variables. An array of `felt252` with this magic value as one of the `felt252` indicates that you should expect right after it a serialized `ByteArray`. This is currently used mainly for prints and panics.

Fully qualified path: `core::byte_array::BYTE_ARRAY_MAGIC`

```rust
pub const BYTE_ARRAY_MAGIC: felt252 =
    0x46a6158a16a947e5916b2a2ca68501a45e93d7110e81aa2d6438b1c57c879a3;
```

