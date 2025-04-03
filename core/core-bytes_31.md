# bytes_31

bytes31. Definitions and utilities for the `bytes31` type.  The `bytes31` type is a compact, indexable 31-byte type.  # Examples  Creating a `bytes31` from a `felt252`:
```cairo
let value: bytes31 = 0xaabb.try_into().unwrap();
```
Accessing a byte by index:
```cairo
assert!(value[0] == 0xbb);
```

Fully qualified path: `core::bytes_31`

## Constants

- [BYTES_IN_BYTES31](./core-bytes_31-BYTES_IN_BYTES31.md)

- [POW_2_128](./core-bytes_31-POW_2_128.md)

- [POW_2_8](./core-bytes_31-POW_2_8.md)

## Free functions

- [split_bytes31](./core-bytes_31-split_bytes31.md)

- [one_shift_left_bytes_felt252](./core-bytes_31-one_shift_left_bytes_felt252.md)

- [one_shift_left_bytes_u128](./core-bytes_31-one_shift_left_bytes_u128.md)

## Traits

- [Bytes31Trait](./core-bytes_31-Bytes31Trait.md)

## Impls

- [Bytes31Impl](./core-bytes_31-Bytes31Impl.md)

- [Bytes31IndexView](./core-bytes_31-Bytes31IndexView.md)

- [Bytes31IntoFelt252](./core-bytes_31-Bytes31IntoFelt252.md)

- [Bytes31IntoU256](./core-bytes_31-Bytes31IntoU256.md)

- [Felt252TryIntoBytes31](./core-bytes_31-Felt252TryIntoBytes31.md)

- [U8IntoBytes31](./core-bytes_31-U8IntoBytes31.md)

- [U128IntoBytes31](./core-bytes_31-U128IntoBytes31.md)

## Extern types

- [bytes31](./core-bytes_31-bytes31.md)

## Extern functions

- [bytes31_const](./core-bytes_31-bytes31_const.md)

