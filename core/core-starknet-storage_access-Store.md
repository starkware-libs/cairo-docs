# Store

Trait for types that can be used as a value in Starknet storage variables.

Fully qualified path: `core::starknet::storage_access::Store`

```rust
pub trait Store<T>
```

## Trait functions

### read

Reads a value from storage from domain `address_domain` and base address `base`.

Fully qualified path: `core::starknet::storage_access::Store::read`

```rust
fn read(address_domain: u32, base: StorageBaseAddress) -> SyscallResult<T>
```


### write

Writes a value to storage to domain `address_domain` and base address `base`.

Fully qualified path: `core::starknet::storage_access::Store::write`

```rust
fn write(address_domain: u32, base: StorageBaseAddress, value: T) -> SyscallResult<()>
```


### read_at_offset

Reads a value from storage from domain `address_domain` and base address `base` at offset `offset`.

Fully qualified path: `core::starknet::storage_access::Store::read_at_offset`

```rust
fn read_at_offset(address_domain: u32, base: StorageBaseAddress, offset: u8) -> SyscallResult<T>
```


### write_at_offset

Writes a value to storage to domain `address_domain` and base address `base` at offset `offset`.

Fully qualified path: `core::starknet::storage_access::Store::write_at_offset`

```rust
fn write_at_offset(
    address_domain: u32, base: StorageBaseAddress, offset: u8, value: T,
) -> SyscallResult<()>
```


### size

Fully qualified path: `core::starknet::storage_access::Store::size`

```rust
fn size() -> u8
```


