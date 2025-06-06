# testing

Measurement of gas consumption for testing purpose.
This module provides the `get_available_gas` function, useful for asserting the amount of gas
consumed by a particular operation or function call.
By calling `get_available_gas` before and after the operation, you can calculate the exact
amount of gas used.

Fully qualified path: [core](./core.md)::[testing](./core-testing.md)


[Extern functions](./core-testing-extern_functions.md)
 ---
| | |
|:---|:---|
| [get_available_gas](./core-testing-get_available_gas.md) | Returns the amount of gas available in the `GasBuiltin` . Useful for asserting that a certain amount of gas was consumed. Note: The actual gas consumption observed by calls to `get_available_gas`[...](./core-testing-get_available_gas.md) |
| [get_unspent_gas](./core-testing-get_unspent_gas.md) | Returns the amount of gas available in the `GasBuiltin` , as well as the amount of gas unused in the local wallet. Useful for asserting that a certain amount of gas was used.[...](./core-testing-get_unspent_gas.md) |
