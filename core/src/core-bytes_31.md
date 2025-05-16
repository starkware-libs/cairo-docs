# bytes_31

Definitions and utilities for the `bytes31` type.The `bytes31` type is a compact, indexable 31-byte type.  # ExamplesCreating a `bytes31` from a `felt252`:
```cairo
let value: bytes31 = 0xaabb.try_into().unwrap();
```
Accessing a byte by index:
```cairo
assert!(value[0] == 0xbb);
```

Fully qualified path: `core::bytes_31`

## Traits

- [Bytes31Trait](./core-bytes_31-Bytes31Trait.md)

## Impls

- [Bytes31Impl](./core-bytes_31-Bytes31Impl.md)

## Extern types

- [bytes31](./core-bytes_31-bytes31.md)

