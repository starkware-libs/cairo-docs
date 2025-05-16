# syscalls

Utilities for interacting with the Starknet OS.Writing smart contracts requires various associated operations, such as calling another contract or accessing the contract’s storage, that standalone programs do not require. Cairo supports these operations by using system calls.System calls enable a contract to require services from the Starknet OS. You can use system calls in a function to get information that depends on the broader state of Starknet, such as the current timestamp of the address of the caller, but also to modify the state of Starknet by, for example, storing values in a contract's storage or deploying new contracts.

Fully qualified path: `core::starknet::syscalls`

## Extern functions

- [call_contract_syscall](./core-starknet-syscalls-call_contract_syscall.md)

- [deploy_syscall](./core-starknet-syscalls-deploy_syscall.md)

- [emit_event_syscall](./core-starknet-syscalls-emit_event_syscall.md)

- [get_block_hash_syscall](./core-starknet-syscalls-get_block_hash_syscall.md)

- [get_execution_info_syscall](./core-starknet-syscalls-get_execution_info_syscall.md)

- [get_execution_info_v2_syscall](./core-starknet-syscalls-get_execution_info_v2_syscall.md)

- [library_call_syscall](./core-starknet-syscalls-library_call_syscall.md)

- [send_message_to_l1_syscall](./core-starknet-syscalls-send_message_to_l1_syscall.md)

- [storage_read_syscall](./core-starknet-syscalls-storage_read_syscall.md)

- [storage_write_syscall](./core-starknet-syscalls-storage_write_syscall.md)

- [replace_class_syscall](./core-starknet-syscalls-replace_class_syscall.md)

- [get_class_hash_at_syscall](./core-starknet-syscalls-get_class_hash_at_syscall.md)

- [keccak_syscall](./core-starknet-syscalls-keccak_syscall.md)

- [sha256_process_block_syscall](./core-starknet-syscalls-sha256_process_block_syscall.md)

