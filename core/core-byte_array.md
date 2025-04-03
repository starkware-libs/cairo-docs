# byte_array

BytesArray. `ByteArray` is designed to handle large sequences of bytes with operations like appending, concatenation, and accessing individual bytes. It uses a structure that combines an `Array` of `bytes31` for full words and a `felt252` for handling partial words, optimizing for both space and performance.  # Examples  There are multiple ways to create a new `ByteArray`: - From a string literal:
```cairo
let s = "Hello";
```
Using the `format!` macro:
```cairo
let max_tps:u16 = 850;
let s = format!("Starknet's max TPS is: {}", max_tps);
```
You can append bytes to an existing `ByteArray`  with [`ByteArrayTrait::append_byte`]([`ByteArrayTrait::append_byte`]):
```cairo
let mut ba: ByteArray = "";
ba.append_byte(0x41); // Appending a single byte 'A'
```
You can create a new `ByteArray` from an existing one by concatenating with `+`:
```cairo
let s = "Hello";
let message = s + " world!";
```
Indexing operations are available on the `ByteArray` type as well:
```cairo
let mut ba: ByteArray = "ABC";
let first_bytes = ba[0]
assert!(first_byte == 0x41);
```

Fully qualified path: `core::byte_array`

## Constants

- [BYTE_ARRAY_MAGIC](./core-byte_array-BYTE_ARRAY_MAGIC.md)

## Structs

- [ByteArray](./core-byte_array-ByteArray.md)

## Traits

- [ByteArrayTrait](./core-byte_array-ByteArrayTrait.md)

## Impls

- [ByteArrayStringLiteral](./core-byte_array-ByteArrayStringLiteral.md)

- [ByteArrayImpl](./core-byte_array-ByteArrayImpl.md)

- [ByteArrayIndexView](./core-byte_array-ByteArrayIndexView.md)

