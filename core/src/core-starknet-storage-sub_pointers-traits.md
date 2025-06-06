
[Traits](./core-starknet-storage-sub_pointers-traits.md)
 ---
| | |
|:---|:---|
| [SubPointers](./core-starknet-storage-sub_pointers-SubPointers.md) | Similar to storage node, but for structs which are stored sequentially in the storage. In contrast to storage node, the fields of the struct are just at an offset from the base address of the struct.[...](./core-starknet-storage-sub_pointers-SubPointers.md) |
| [SubPointersForward](./core-starknet-storage-sub_pointers-SubPointersForward.md) | A trait for implementing `SubPointers`  for types which are not a `StoragePointer` , such as `StorageBase`  and `StoragePath` .[...](./core-starknet-storage-sub_pointers-SubPointersForward.md) |
| [SubPointersMut](./core-starknet-storage-sub_pointers-SubPointersMut.md) | A mutable version of `SubPointers` , works the same way, but on `Mutable<T>` .[...](./core-starknet-storage-sub_pointers-SubPointersMut.md) |
| [SubPointersMutForward](./core-starknet-storage-sub_pointers-SubPointersMutForward.md) | A trait for implementing `SubPointersMut`  for types which are not a `StoragePointer` , such as `StorageBase`  and `StoragePath` .[...](./core-starknet-storage-sub_pointers-SubPointersMutForward.md) |
