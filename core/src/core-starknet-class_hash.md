# class_hash

The `ClassHash` type represents a Starknet contract class hash, with a value range of `[0, 2**251)`.A variable of type `ClassHash` can be created from a `felt252` value using the `class_hash_const` function, or using the `TryInto` trait.  # Examples
```cairo
use starknet::class_hash::class_hash_const;

let hash = class_hash_const::<0x123>();
let hash = 0x123.try_into().unwrap();
```

Fully qualified path: `core::starknet::class_hash`

## Extern types

- [ClassHash](./core-starknet-class_hash-ClassHash.md)

## Extern functions

- [class_hash_const](./core-starknet-class_hash-class_hash_const.md)

