# References

Memory is immutable by default due to the underlying VM architecture. However, we can abstract this immutability using `ref` parameters, which allow us to modify a value and implicitly return ownership back to the caller.

```cairo,editable
{{#include ../../../listings/scope/retaining_ownership/ref_listing/src/lib.cairo}}
```

### See also:

[Snapshots and References](https://book.cairo-lang.org/ch04-02-references-and-snapshots.html)
