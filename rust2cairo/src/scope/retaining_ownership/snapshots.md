# Snapshots

Most of the time, we'd like to access data without taking ownership over it. To accomplish this,
Cairo uses a _snapshot_ mechanism. Instead of passing objects by value (`T`), objects can be passed
by snapshot (`@T`).

The compiler statically guarantees that snapshots always point to valid values. Since Cairo's memory
is immutable, snapshots are simply views into memory cells at a specific state.

```cairo,editable
{{#include ../../../listings/scope/retaining_ownership/snapshots_listing/src/lib.cairo}}
```
