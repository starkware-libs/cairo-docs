
[Extern functions](./core-starknet-syscalls-extern_functions.md)
 ---
| | |
|:---|:---|
| [call_contract_syscall](./core-starknet-syscalls-call_contract_syscall.md) | Calls a given contract.[...](./core-starknet-syscalls-call_contract_syscall.md) |
| [deploy_syscall](./core-starknet-syscalls-deploy_syscall.md) | Deploys a new instance of a previously declared class.[...](./core-starknet-syscalls-deploy_syscall.md) |
| [emit_event_syscall](./core-starknet-syscalls-emit_event_syscall.md) | Emits an event.[...](./core-starknet-syscalls-emit_event_syscall.md) |
| [get_block_hash_syscall](./core-starknet-syscalls-get_block_hash_syscall.md) | Returns the hash of the block with the given number.[...](./core-starknet-syscalls-get_block_hash_syscall.md) |
| [get_execution_info_syscall](./core-starknet-syscalls-get_execution_info_syscall.md) | Gets information about the currently executing block and the transactions within it. For a complete description of this information, see `Execution information` . When an account’s `__validate__` ,[...](./core-starknet-syscalls-get_execution_info_syscall.md) |
| [get_execution_info_v2_syscall](./core-starknet-syscalls-get_execution_info_v2_syscall.md) | Gets information about the current execution, version 2. This syscall should not be called directly. Instead, use `starknet::info::get_execution_info` .[...](./core-starknet-syscalls-get_execution_info_v2_syscall.md) |
| [library_call_syscall](./core-starknet-syscalls-library_call_syscall.md) | Calls the requested function in any previously declared class.[...](./core-starknet-syscalls-library_call_syscall.md) |
| [send_message_to_l1_syscall](./core-starknet-syscalls-send_message_to_l1_syscall.md) | Sends a message to L1.[...](./core-starknet-syscalls-send_message_to_l1_syscall.md) |
| [storage_read_syscall](./core-starknet-syscalls-storage_read_syscall.md) | Gets the value of a key in the storage of the calling contract.[...](./core-starknet-syscalls-storage_read_syscall.md) |
| [storage_write_syscall](./core-starknet-syscalls-storage_write_syscall.md) | Sets the value of a key in the storage of the calling contract.[...](./core-starknet-syscalls-storage_write_syscall.md) |
| [replace_class_syscall](./core-starknet-syscalls-replace_class_syscall.md) | Replaces the class hash of the current contract, instantly modifying its entrypoints. The new class becomes effective only after the current function call completes.[...](./core-starknet-syscalls-replace_class_syscall.md) |
| [get_class_hash_at_syscall](./core-starknet-syscalls-get_class_hash_at_syscall.md) | Gets the class hash of the contract at the given address.[...](./core-starknet-syscalls-get_class_hash_at_syscall.md) |
| [keccak_syscall](./core-starknet-syscalls-keccak_syscall.md) | Computes the keccak of the input.[...](./core-starknet-syscalls-keccak_syscall.md) |
| [sha256_process_block_syscall](./core-starknet-syscalls-sha256_process_block_syscall.md) | Computes the next SHA-256 state of the input with the given state.[...](./core-starknet-syscalls-sha256_process_block_syscall.md) |
| [meta_tx_v0_syscall](./core-starknet-syscalls-meta_tx_v0_syscall.md) | Invokes the given entry point as a v0 meta transaction.[...](./core-starknet-syscalls-meta_tx_v0_syscall.md) |
