# Iterator::sum

`Iterator::sum` is a function which takes an iterator and returns the sum of all of its elements. Its signature:

```cairo,noplayground
    fn sum<+Destruct<T>, +Destruct<Self::Item>, +Sum<Self::Item>>(
        self: T,
    ) -> Self::Item;
```

Here's an example of how to use `sum()`:

```cairo,editable
{{#include ../../../../listings/functions/closures/closure_examples/iter_sum/src/lib.cairo}}
```

### See also:

[`core::iter::Iterator::sum`][sum]

[sum]: https://docs.swmansion.com/scarb/corelib/core-iter-traits-iterator-Iterator.html#sum
