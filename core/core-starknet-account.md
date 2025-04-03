# account

Account module defining the [`Call`]([`Call`]) struct and the [`AccountContract`](./core-starknet-account-AccountContract.md) trait.  The `Call` struct represents a call to a contract, with the following fields: - `to`: The address of the contract to call. - `selector`: The entry point selector in the called contract. - `calldata`: The calldata to pass to the entry point.  The `AccountContract` trait defines the standard interface for account contracts. It assumes that the calldata for invoke transactions is an `Array<Call>`, following the SNIP6 standard.  Implementing this trait allows contracts to function as account contracts in the Starknet network, supporting class declarations and batched call execution.

Fully qualified path: `core::starknet::account`

## Structs

- [Call](./core-starknet-account-Call.md)

- [AccountContractDispatcher](./core-starknet-account-AccountContractDispatcher.md)

- [AccountContractLibraryDispatcher](./core-starknet-account-AccountContractLibraryDispatcher.md)

- [AccountContractSafeLibraryDispatcher](./core-starknet-account-AccountContractSafeLibraryDispatcher.md)

- [AccountContractSafeDispatcher](./core-starknet-account-AccountContractSafeDispatcher.md)

## Traits

- [AccountContract](./core-starknet-account-AccountContract.md)

- [AccountContractDispatcherTrait](./core-starknet-account-AccountContractDispatcherTrait.md)

- [AccountContractSafeDispatcherTrait](./core-starknet-account-AccountContractSafeDispatcherTrait.md)

