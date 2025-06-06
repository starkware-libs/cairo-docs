# class_hash

The `ClassHash` type represents a Starknet contract class hash, with a value range of
`[0, 2**251)`.
A variable of type `ClassHash` can be created from a `felt252` value using the
`class_hash_const` function, or using the `TryInto` trait.
# Examples

```cairo
use starknet::class_hash::class_hash_const;

let hash = class_hash_const::<0x123>();
let hash = 0x123.try_into().unwrap();
```

Fully qualified path: [core](./core.md)::[starknet](./core-starknet.md)::[class_hash](./core-starknet-class_hash.md)


[Extern types](./core-starknet-class_hash-extern_types.md)
 ---
| | |
|:---|:---|
| [ClassHash](./core-starknet-class_hash-ClassHash.md) | Represents a Starknet contract class hash. The value range of this type is `[0, 2**251)` .[...](./core-starknet-class_hash-ClassHash.md) |

[Extern functions](./core-starknet-class_hash-extern_functions.md)
 ---
| | |
|:---|:---|
| [class_hash_const](./core-starknet-class_hash-class_hash_const.md) | Returns a `ClassHash`  given a `felt252`  value.[...](./core-starknet-class_hash-class_hash_const.md) |
