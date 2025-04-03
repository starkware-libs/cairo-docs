# Retaining Ownership

Most of the time, we'd like to access data without taking ownership over it. To accomplish this,
Cairo proposes two mechanism:

- [Snapshots][snapshots]: Instead of passing objects by value (`T`), objects can be passed
  by snapshot (`@T`). A snapshot is an immutable view into memory cells at a specific state that can not be mutated.
- [References][references]: Instead of passing objects by value (`T`), objects can be passed
  by reference (`ref T`). A reference is simply a syntactic sugar for a variable whose ownership is transferred, can be mutated, and returned back to the original owner.

[references]: ./retaining_ownership/ref.md
[snapshots]: ./retaining_ownership/snapshots.md
