# withdraw_gas_all

Same as `withdraw_gas`, but directly receives `BuiltinCosts`, which enables optimizations by removing the need for repeated internal calls for fetching the table of consts that may internally happen in calls to `withdraw_gas`. Should be used with caution.

Fully qualified path: `core::gas::withdraw_gas_all`

```rust
pub extern fn withdraw_gas_all(
    costs: BuiltinCosts,
) -> Option<()> implicits(RangeCheck, GasBuiltin) nopanic;
```

