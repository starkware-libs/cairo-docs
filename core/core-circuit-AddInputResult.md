# AddInputResult

The result of filling an input in the circuit instance's data.

Fully qualified path: `core::circuit::AddInputResult`

```rust
pub enum AddInputResult<C> {
    Done: CircuitData<C>,
    More: CircuitInputAccumulator<C>,
}
```

## Variants

### Done

All inputs have been filled.

Fully qualified path: `core::circuit::AddInputResult::Done`

```rust
Done : CircuitData < C >
```


### More

More inputs are needed to fill the circuit instance's data.

Fully qualified path: `core::circuit::AddInputResult::More`

```rust
More : CircuitInputAccumulator < C >
```


