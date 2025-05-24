# ByteArrays

The main string type in Cairo is `ByteArray`, which is an optimized data structure to store sequences of bytes.
This is mainly used for strings, but can also be used to hold any sequence of bytes.

```cairo,editable
{{#include ../../listings/core/bytearrays/src/lib.cairo}}
```

More `ByteArray` methods can be found under the
[core::byte_array][byte_array] module.

[byte_array]: https://docs.swmansion.com/scarb/corelib/core-byte_array.html
