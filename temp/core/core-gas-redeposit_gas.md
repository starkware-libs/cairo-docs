# redeposit_gas

Returns unused gas into the gas builtin.  Useful for cases where different branches take different amounts of gas, but gas withdrawal is the same for both.

Fully qualified path: `core::gas::redeposit_gas`

```rust
pub extern fn redeposit_gas() implicits(GasBuiltin) nopanic;
```

