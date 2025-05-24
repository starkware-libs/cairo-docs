# To ByteArray

To convert any type to a `ByteArray` is as simple as implementing the [`fmt::Display`] trait for the
type, which also allows printing the type as discussed in the section on [`print!`][print].

```cairo,editable
{{#include ../../listings/conversion/to_bytearray/src/lib.cairo}}
```
