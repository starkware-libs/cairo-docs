# to_byte_array

ASCII representation of numeric types for `ByteArray` manipulation.
This module enables conversion of numeric values into their ASCII string representation,
with support for different numeric bases and efficient appending to existing `ByteArray`.
# Examples

Basic decimal formatting:
```cairo
use core::to_byte_array::{FormatAsByteArray, AppendFormattedToByteArray};

let value: u32 = 42;
let base: NonZero<u32> = 10;

// Create a new formatted `ByteArray`
let formatted = value.format_as_byte_array(base);
assert!(formatted == "42");

// Append to an existing `ByteArray`
let mut buffer = "Value: ";
value.append_formatted_to_byte_array(ref buffer, base);
assert!(buffer == "Value: 42");
```

Custom base formatting:
```cairo
use core::to_byte_array::FormatAsByteArray;
let value: u32 = 255;

// Hexadecimal representation
let hex = value.format_as_byte_array(16);
assert!(hex == "ff");

// Binary representation
let bin = value.format_as_byte_array(2);
assert!(bin == "11111111");
```

Fully qualified path: [core](./core.md)::[to_byte_array](./core-to_byte_array.md)


[Traits](./core-to_byte_array-traits.md)
 ---
| | |
|:---|:---|
| [AppendFormattedToByteArray](./core-to_byte_array-AppendFormattedToByteArray.md) | A trait for appending the ASCII representation of a number to an existing `ByteArray` .[...](./core-to_byte_array-AppendFormattedToByteArray.md) |
| [FormatAsByteArray](./core-to_byte_array-FormatAsByteArray.md) | A trait for formatting values into their ASCII string representation in a `ByteArray` .[...](./core-to_byte_array-FormatAsByteArray.md) |
