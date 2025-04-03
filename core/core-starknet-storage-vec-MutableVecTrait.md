# MutableVecTrait

Trait for the interface of a mutable storage vec.

Fully qualified path: `core::starknet::storage::vec::MutableVecTrait`

```rust
pub trait MutableVecTrait<T>
```

## Trait functions

### get

Fully qualified path: `core::starknet::storage::vec::MutableVecTrait::get`

```rust
fn get(self: T, index: u64) -> Option<StoragePath<Mutable<Self::ElementType>>>
```


### at

Fully qualified path: `core::starknet::storage::vec::MutableVecTrait::at`

```rust
fn at(self: T, index: u64) -> StoragePath<Mutable<Self::ElementType>>
```


### len

Fully qualified path: `core::starknet::storage::vec::MutableVecTrait::len`

```rust
fn len(self: T) -> u64
```


### append

Fully qualified path: `core::starknet::storage::vec::MutableVecTrait::append`

```rust
fn append(self: T) -> StoragePath<Mutable<Self::ElementType>>
```


## Trait types

### ElementType

Fully qualified path: `core::starknet::storage::vec::MutableVecTrait::ElementType`

```rust
type ElementType;
```


