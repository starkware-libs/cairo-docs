# AppendFormattedToByteArray

A trait for appending the ASCII representation of a number to an existing `ByteArray`.

Fully qualified path: `core::to_byte_array::AppendFormattedToByteArray`

```rust
pub trait AppendFormattedToByteArray<T>
```

## Trait functions

### append_formatted_to_byte_array

Appends the ASCII representation of the value to the provided `ByteArray`.  # Examples
```cairo
use core::to_byte_array::AppendFormattedToByteArray;

let mut buffer = "Count: ";
let num: u32 = 42;
num.append_formatted_to_byte_array(ref buffer, 10);
assert!(buffer == "Count: 42");
```

Fully qualified path: `core::to_byte_array::AppendFormattedToByteArray::append_formatted_to_byte_array`

```rust
fn append_formatted_to_byte_array(self: @T, ref byte_array: ByteArray, base: NonZero<T>)
```


