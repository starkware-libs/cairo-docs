
[Extern functions](./core-starknet-storage_access-extern_functions.md)
 ---
| | |
|:---|:---|
| [storage_base_address_const](./core-starknet-storage_access-storage_base_address_const.md) | Returns a `StorageBaseAddress`  given a constant `felt252`  value. The value is validated to be in the range `[0, 2**251 - 256)`  at compile time.[...](./core-starknet-storage_access-storage_base_address_const.md) |
| [storage_base_address_from_felt252](./core-starknet-storage_access-storage_base_address_from_felt252.md) | Returns a `StorageBaseAddress`  given a `felt252`  value. Wraps around the value if it is not in the range `[0, 2**251 - 256)` .[...](./core-starknet-storage_access-storage_base_address_from_felt252.md) |
| [storage_address_from_base_and_offset](./core-starknet-storage_access-storage_address_from_base_and_offset.md) | Sums the base address and the offset to return a storage address.[...](./core-starknet-storage_access-storage_address_from_base_and_offset.md) |
| [storage_address_from_base](./core-starknet-storage_access-storage_address_from_base.md) | Converts a `StorageBaseAddress`  into a `StorageAddress` . This should be used through the high-level `Into`  trait.[...](./core-starknet-storage_access-storage_address_from_base.md) |
