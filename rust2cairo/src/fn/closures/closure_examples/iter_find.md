# Searching through iterators

`Iterator::find` is a function which iterates over an iterator and searches for the
first value which satisfies some condition. If none of the values satisfy the
condition, it returns `None`. Its signature:

```cairo,ignore
pub trait Iterator<T> {
    // The type being iterated over.
    type Item;

    // `find` takes `ref self` meaning the caller may be
    // modified, but not consumed.
    fn find<
        P,
        // `Fn` meaning that any captured variable will not be consumed. `@Self::Item` states it
        // takes arguments to the closure by snapshot.
        +core::ops::Fn<P, (@Self::Item,)>[Output: bool],
        +Destruct<P>,
        +Destruct<T>,
        +Destruct<Self::Item>,
    >(
        ref self: T, predicate: P,
    ) -> Option<
        Self::Item,
    >;
}
```

```cairo,editable
{{#include ../../../../listings/functions/closures/closure_examples/iter_find/src/lib.cairo}}
```

`Iterator::find` gives you a snapshot of the item.

### See also:

[`std::iter::Iterator::find`][find]

[find]: https://docs.swmansion.com/scarb/corelib/core-iter-traits-iterator-Iterator.html#find
