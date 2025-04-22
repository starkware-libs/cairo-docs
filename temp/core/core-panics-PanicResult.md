# PanicResult

Result type for operations that can trigger a panic.

Fully qualified path: `core::panics::PanicResult`

```rust
pub enum PanicResult<T> {
    Ok: T,
    Err: (Panic, Array<felt252>),
}
```

## Variants

### Ok

Fully qualified path: `core::panics::PanicResult::Ok`

```rust
Ok : T
```


### Err

Fully qualified path: `core::panics::PanicResult::Err`

```rust
Err : ( Panic , Array < felt252 > )
```


