# info

Information about the Starknet execution environment.
This module provides access to runtime information about the current transaction,
block, and execution context in a Starknet smart contract. It enables contracts
to access execution context data.
# Examples

```cairo
use starknet::{get_block_info, get_caller_address, get_contract_address};

// Get block information
let block_info = get_block_info().unbox();
let timestamp = block_info.block_timestamp;

// Get caller and contract addresses
let caller = get_caller_address();
let contract = get_contract_address();
```

Fully qualified path: [core](./core.md)::[starknet](./core-starknet.md)::[info](./core-starknet-info.md)


[Modules](./core-starknet-info-modules.md)
 ---
| | |
|:---|:---|
| [v2](./core-starknet-info-v2.md) | The extended version of the `get_execution_info`  syscall result.[...](./core-starknet-info-v2.md) |

[Free functions](./core-starknet-info-free_functions.md)
 ---
| | |
|:---|:---|
| [get_block_info](./core-starknet-info-get_block_info.md) | Returns the block information for the current block.[...](./core-starknet-info-get_block_info.md) |
| [get_block_number](./core-starknet-info-get_block_number.md) | Returns the number of the current block.[...](./core-starknet-info-get_block_number.md) |
| [get_block_timestamp](./core-starknet-info-get_block_timestamp.md) | Returns the timestamp of the current block.[...](./core-starknet-info-get_block_timestamp.md) |
| [get_caller_address](./core-starknet-info-get_caller_address.md) | Returns the address of the caller contract. Returns `0`  if there is no caller—for example, when a transaction begins execution inside an account contract. Note: This function returns the direct[...](./core-starknet-info-get_caller_address.md) |
| [get_contract_address](./core-starknet-info-get_contract_address.md) | Returns the address of the contract being executed.[...](./core-starknet-info-get_contract_address.md) |
| [get_execution_info](./core-starknet-info-get_execution_info.md) | Returns the execution info for the current execution.[...](./core-starknet-info-get_execution_info.md) |
| [get_tx_info](./core-starknet-info-get_tx_info.md) | Returns the transaction information for the current transaction.[...](./core-starknet-info-get_tx_info.md) |

[Structs](./core-starknet-info-structs.md)
 ---
| | |
|:---|:---|
| [BlockInfo](./core-starknet-info-BlockInfo.md) | Information about the current block.[...](./core-starknet-info-BlockInfo.md) |
