# bytes_31

Definitions and utilities for the `bytes31` type.
The `bytes31` type is a compact, indexable 31-byte type.
# Examples

Creating a `bytes31` from a `felt252`:
```cairo
let value: bytes31 = 0xaabb.try_into().unwrap();
```

Accessing a byte by index:
```cairo
assert!(value[0] == 0xbb);
```

Fully qualified path: [core](./core.md)::[bytes_31](./core-bytes_31.md)


[Traits](./core-bytes_31-traits.md)
 ---
| | |
|:---|:---|
| [Bytes31Trait](./core-bytes_31-Bytes31Trait.md) | [...](./core-bytes_31-Bytes31Trait.md) |

[Impls](./core-bytes_31-impls.md)
 ---
| | |
|:---|:---|
| [Bytes31Impl](./core-bytes_31-Bytes31Impl.md) | A trait for accessing a specific byte of a `bytes31`  type.[...](./core-bytes_31-Bytes31Impl.md) |

[Extern types](./core-bytes_31-extern_types.md)
 ---
| | |
|:---|:---|
| [bytes31](./core-bytes_31-bytes31.md) | Represents a 31-byte fixed-size byte type.[...](./core-bytes_31-bytes31.md) |
