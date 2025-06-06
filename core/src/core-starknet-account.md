# account

Account module defining the `Call` struct and the [`AccountContract`](./core-starknet-account-AccountContract.md) trait.
The `Call` struct represents a call to a contract, with the following fields:
- `to`: The address of the contract to call.
- `selector`: The entry point selector in the called contract.
- `calldata`: The calldata to pass to the entry point.

The `AccountContract` trait defines the standard interface for account contracts. It assumes
that the calldata for invoke transactions is an `Array<Call>`, following the SNIP6 standard.
Implementing this trait allows contracts to function as account contracts in the Starknet
network, supporting class declarations and batched call execution.

Fully qualified path: [core](./core.md)::[starknet](./core-starknet.md)::[account](./core-starknet-account.md)


[Structs](./core-starknet-account-structs.md)
 ---
| | |
|:---|:---|
| [Call](./core-starknet-account-Call.md) | A struct representing a call to a contract.[...](./core-starknet-account-Call.md) |
| [AccountContractDispatcher](./core-starknet-account-AccountContractDispatcher.md) | [...](./core-starknet-account-AccountContractDispatcher.md) |
| [AccountContractLibraryDispatcher](./core-starknet-account-AccountContractLibraryDispatcher.md) | [...](./core-starknet-account-AccountContractLibraryDispatcher.md) |
| [AccountContractSafeLibraryDispatcher](./core-starknet-account-AccountContractSafeLibraryDispatcher.md) | [...](./core-starknet-account-AccountContractSafeLibraryDispatcher.md) |
| [AccountContractSafeDispatcher](./core-starknet-account-AccountContractSafeDispatcher.md) | [...](./core-starknet-account-AccountContractSafeDispatcher.md) |

[Traits](./core-starknet-account-traits.md)
 ---
| | |
|:---|:---|
| [AccountContract](./core-starknet-account-AccountContract.md) | A trait for account contracts that support class declarations (only `__validate__`  and `__execute__`  are mandatory for an account). This trait assumes that the calldata for invoke transactions is[...](./core-starknet-account-AccountContract.md) |
| [AccountContractDispatcherTrait](./core-starknet-account-AccountContractDispatcherTrait.md) | [...](./core-starknet-account-AccountContractDispatcherTrait.md) |
| [AccountContractSafeDispatcherTrait](./core-starknet-account-AccountContractSafeDispatcherTrait.md) | [...](./core-starknet-account-AccountContractSafeDispatcherTrait.md) |
