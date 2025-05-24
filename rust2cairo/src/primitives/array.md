# Arrays, Spans, and Fixed-Size Arrays

An Array is a growable collection of objects of the same type `T`, stored in contiguous memory.
Because Cairo's memory is write-once, values stored in an array cannot be modified. The only
operation that can be performed on an array is appending elements at the end, or removing elements
from the front.

A Span is the [snapshot][snapshot] of an Array - representing a range of elements in the array that
can not be appended to. If the array is modified, the associated span will not be affected.

A Fixed-Size Array is an immutable sequence of elements of the same type stored in contiguous
memory. Its size and contents are known at compile time, and they're useful to hard-code a sequence
of data in your program.

```cairo,editable
{{#include ../../listings/array/src/lib.cairo}}
```

## See also:

- [The Cairo Book](https://book.cairo-lang.org/ch02-02-data-types.html)
