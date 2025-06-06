# byte_array

`ByteArray` is designed to handle large sequences of bytes with operations like appending,
concatenation, and accessing individual bytes. It uses a structure that combines an `Array` of
`bytes31` for full words and a `felt252` for handling partial words, optimizing for both space
and performance.
# Examples

There are multiple ways to create a new `ByteArray`:
- From a string literal:

```cairo
let s = "Hello";
```

- Using the `format!` macro:

```cairo
let max_tps:u16 = 850;
let s = format!("Starknet's max TPS is: {}", max_tps);
```

You can append bytes to an existing `ByteArray` with `ByteArrayTrait::append_byte`:
```cairo
let mut ba: ByteArray = "";
ba.append_byte(0x41); // Appending a single byte 'A'
```

You can create a new `ByteArray` from an existing one by concatenating with
`+`:
```cairo
let s = "Hello";
let message = s + " world!";
```

Indexing operations are available on the `ByteArray` type as well:
```cairo
let mut ba: ByteArray = "ABC";
let first_byte = ba[0]
assert!(first_byte == 0x41);
```

Fully qualified path: [core](./core.md)::[byte_array](./core-byte_array.md)


[Constants](./core-byte_array-constants.md)
 ---
| | |
|:---|:---|
| [BYTE_ARRAY_MAGIC](./core-byte_array-BYTE_ARRAY_MAGIC.md) | A magic constant for identifying serialization of `ByteArray`  variables. An array of `felt252` with this magic value as one of the `felt252`  indicates that you should expect right after it a[...](./core-byte_array-BYTE_ARRAY_MAGIC.md) |

[Structs](./core-byte_array-structs.md)
 ---
| | |
|:---|:---|
| [ByteArray](./core-byte_array-ByteArray.md) | Byte array type.[...](./core-byte_array-ByteArray.md) |
| [ByteArrayIter](./core-byte_array-ByteArrayIter.md) | An iterator struct over a ByteArray.[...](./core-byte_array-ByteArrayIter.md) |

[Traits](./core-byte_array-traits.md)
 ---
| | |
|:---|:---|
| [ByteArrayTrait](./core-byte_array-ByteArrayTrait.md) | [...](./core-byte_array-ByteArrayTrait.md) |

[Impls](./core-byte_array-impls.md)
 ---
| | |
|:---|:---|
| [ByteArrayImpl](./core-byte_array-ByteArrayImpl.md) | Functions associated with the `ByteArray`  type.[...](./core-byte_array-ByteArrayImpl.md) |
