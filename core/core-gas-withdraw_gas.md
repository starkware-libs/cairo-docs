# withdraw_gas

Withdraws gas from the `GasBuiltin` to handle the success case flow. Returns `Option::Some(())` if there is sufficient gas to handle the success case, otherwise returns `Option::None`.  Example:
```cairo
// The success branch is the following lines, the failure branch is the `panic` caused by the
// `unwrap` call.
withdraw_gas().unwrap();

// Direct handling of `withdraw_gas`.
match withdraw_gas() {
    Option::Some(()) => success_case(),
    Option::None => cheap_not_enough_gas_case(),
}
```

Fully qualified path: `core::gas::withdraw_gas`

```rust
pub extern fn withdraw_gas() -> Option<()> implicits(RangeCheck, GasBuiltin) nopanic;
```

