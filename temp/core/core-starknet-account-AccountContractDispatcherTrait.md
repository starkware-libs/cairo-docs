# AccountContractDispatcherTrait

Fully qualified path: `core::starknet::account::AccountContractDispatcherTrait`

```rust
pub trait AccountContractDispatcherTrait<T>
```

## Trait functions

### __validate_declare__

An entry point that is called to check if the account is willing to pay for the declaration of the class with the given hash. The entry point should return `core::starknet::VALIDATED` if the account is willing to pay for the declaration.

Fully qualified path: `core::starknet::account::AccountContractDispatcherTrait::__validate_declare__`

```rust
fn __validate_declare__(self: T, class_hash: felt252) -> felt252
```


### __validate__

An entry point that is called to check if the account is willing to pay for executing a given set of calls. The entry point should return `core::starknet::VALIDATED` if the account is willing to pay for the execution, in which case `__execute__` will be called on the same set of calls.

Fully qualified path: `core::starknet::account::AccountContractDispatcherTrait::__validate__`

```rust
fn __validate__(self: T, calls: Array<Call>) -> felt252
```


### __execute__

An entry point that is called to execute a given set of calls. This entry point should block the deprecated v0 invoke transactions as they do not go through the `__validate__` entry point.

Fully qualified path: `core::starknet::account::AccountContractDispatcherTrait::__execute__`

```rust
fn __execute__(self: T, calls: Array<Call>) -> Array<Span<felt252>>
```


