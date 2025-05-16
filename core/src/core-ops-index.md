# index

Indexing traits for indexing operations on collections.This module provides traits for implementing the indexing operator `[]`, offering two distinct approaches to access elements in collections:[`IndexView`](./core-ops-index-IndexView.md) - For snapshot-based access * [`Index`](./core-ops-index-Index.md) - For reference-based access  # When to use which traitUse [`IndexView`](./core-ops-index-IndexView.md) when the collection can be accessed in a read-only context and is not mutated by a read access. This is the most common case in Cairo. - Use [`Index`](./core-ops-index-Index.md) when the input type needs to be passed as `ref`. This is mainly useful for types depending on a [`Felt252Dict`](./core-dict-Felt252Dict.md), where dictionary accesses are modifying the data structure itself.Only one of these traits should be implemented for any given type, not both.

Fully qualified path: `core::ops::index`

## Traits

- [IndexView](./core-ops-index-IndexView.md)

- [Index](./core-ops-index-Index.md)

