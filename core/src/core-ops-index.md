# index

Indexing traits for indexing operations on collections.
This module provides traits for implementing the indexing operator `[]`, offering two distinct
approaches to access elements in collections:
- [`IndexView`](./core-ops-index-IndexView.md) - For snapshot-based access
- [`Index`](./core-ops-index-Index.md) - For reference-based access
# When to use which trait

- Use [`IndexView`](./core-ops-index-IndexView.md) when the collection can be accessed in a read-only context and is not
mutated by a read access. This is the most common case in Cairo.
- Use [`Index`](./core-ops-index-Index.md) when the input type needs to be passed as `ref`. This is mainly useful for types
depending on a [`Felt252Dict`](./core-dict-Felt252Dict.md), where dictionary accesses are modifying the data structure
itself.

Only one of these traits should be implemented for any given type, not both.

Fully qualified path: [core](./core.md)::[ops](./core-ops.md)::[index](./core-ops-index.md)


[Traits](./core-ops-index-traits.md)
 ---
| | |
|:---|:---|
| [IndexView](./core-ops-index-IndexView.md) | A trait for indexing operations ( `container[index]` ) where the input type is not modified. `container[index]`  is syntactic sugar for `container.index(index)` .[...](./core-ops-index-IndexView.md) |
| [Index](./core-ops-index-Index.md) | A trait for indexing operations ( `container[index]` ) where the input type is mutated. This trait should be implemented when you want to implement indexing operations on a type that's[...](./core-ops-index-Index.md) |
