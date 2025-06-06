# gas

Utilities for handling gas in Cairo code.

Fully qualified path: [core](./core.md)::[gas](./core-gas.md)


[Extern types](./core-gas-extern_types.md)
 ---
| | |
|:---|:---|
| [BuiltinCosts](./core-gas-BuiltinCosts.md) | Type representing the table of the costs of the different builtin usages.[...](./core-gas-BuiltinCosts.md) |
| [GasBuiltin](./core-gas-GasBuiltin.md) | The gas builtin. This type is used to handle gas in the Cairo code. Contains the amount of gas available for the current run.[...](./core-gas-GasBuiltin.md) |
| [GasReserve](./core-gas-GasReserve.md) | Represents a gas reserve. Gas reserves can be created at any point using gas from the gas counter, and can be utilized at a later point in time.[...](./core-gas-GasReserve.md) |

[Extern functions](./core-gas-extern_functions.md)
 ---
| | |
|:---|:---|
| [withdraw_gas](./core-gas-withdraw_gas.md) | Withdraws gas from the `GasBuiltin`  to handle the success case flow. Returns `Some(())`  if there is sufficient gas to handle the success case, otherwise returns `None` .[...](./core-gas-withdraw_gas.md) |
| [withdraw_gas_all](./core-gas-withdraw_gas_all.md) | Same as `withdraw_gas` , but directly receives `BuiltinCosts` , which enables optimizations by removing the need for repeated internal calls for fetching the table of constants that may[...](./core-gas-withdraw_gas_all.md) |
| [redeposit_gas](./core-gas-redeposit_gas.md) | Returns unused gas into the gas builtin. Useful for cases where different branches take different amounts of gas, but gas withdrawal is the same for both.[...](./core-gas-redeposit_gas.md) |
| [get_builtin_costs](./core-gas-get_builtin_costs.md) | Returns the `BuiltinCosts`  table to be used in `withdraw_gas_all` .[...](./core-gas-get_builtin_costs.md) |
| [gas_reserve_create](./core-gas-gas_reserve_create.md) | Creates a new gas reserve by withdrawing the specified amount from the gas counter. Returns `Some(GasReserve)`  if there is sufficient gas, otherwise returns `None` .[...](./core-gas-gas_reserve_create.md) |
| [gas_reserve_utilize](./core-gas-gas_reserve_utilize.md) | Adds the gas stored in the reserve back to the gas counter. The reserve is consumed in the process.[...](./core-gas-gas_reserve_utilize.md) |
