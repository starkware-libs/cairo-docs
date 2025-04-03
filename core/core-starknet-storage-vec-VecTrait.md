# VecTrait

Trait for the interface of a storage vec.

Fully qualified path: `core::starknet::storage::vec::VecTrait`

```rust
pub trait VecTrait<T>
```

## Trait functions

### get

Fully qualified path: `core::starknet::storage::vec::VecTrait::get`

```rust
fn get(self: T, index: u64) -> Option<StoragePath<Self::ElementType>>
```


### at

Fully qualified path: `core::starknet::storage::vec::VecTrait::at`

```rust
fn at(self: T, index: u64) -> StoragePath<Self::ElementType>
```


### len

Fully qualified path: `core::starknet::storage::vec::VecTrait::len`

```rust
fn len(self: T) -> u64
```


## Trait types

### ElementType

Fully qualified path: `core::starknet::storage::vec::VecTrait::ElementType`

```rust
type ElementType;
```


