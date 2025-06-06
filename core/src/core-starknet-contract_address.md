# contract_address

The `ContractAddress` type represents a Starknet contract address, with a value range of
`[0, 2**251)`.
A variable of type `ContractAddress` can be created from a `felt252` value using the
`contract_address_const` function, or using the `TryInto` trait.
# Examples

```cairo
use starknet::contract_address::contract_address_const;

let contract_address = contract_address_const::<0x0>();
```

Fully qualified path: [core](./core.md)::[starknet](./core-starknet.md)::[contract_address](./core-starknet-contract_address.md)


[Extern types](./core-starknet-contract_address-extern_types.md)
 ---
| | |
|:---|:---|
| [ContractAddress](./core-starknet-contract_address-ContractAddress.md) | Represents a Starknet contract address. The value range of this type is `[0, 2**251)` .[...](./core-starknet-contract_address-ContractAddress.md) |

[Extern functions](./core-starknet-contract_address-extern_functions.md)
 ---
| | |
|:---|:---|
| [contract_address_const](./core-starknet-contract_address-contract_address_const.md) | Returns a `ContractAddress`  given a `felt252`  value.[...](./core-starknet-contract_address-contract_address_const.md) |
