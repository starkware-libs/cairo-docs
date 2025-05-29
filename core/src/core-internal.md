# internal

Fully qualified path: [core](./core.md)::[internal](./core-internal.md)


[Structs](./core-internal-structs.md)
 ---
| | |
|:---|:---|
| [DropWith](./core-internal-DropWith.md) | Wrapper type to ensure that a type `T`  is dropped using a specific `Drop`  impl.[...](./core-internal-DropWith.md) |
| [InferDrop](./core-internal-InferDrop.md) | Helper to have the same interface as `DropWith`  while inferring the `Drop`  implementation.[...](./core-internal-InferDrop.md) |
| [DestructWith](./core-internal-DestructWith.md) | Wrapper type to ensure that a type `T`  is destructed using a specific `Destruct`  impl.[...](./core-internal-DestructWith.md) |
| [InferDestruct](./core-internal-InferDestruct.md) | Helper to have the same interface as `DestructWith`  while inferring the `Destruct` implementation.[...](./core-internal-InferDestruct.md) |

[Enums](./core-internal-enums.md)
 ---
| | |
|:---|:---|
| [OptionRev](./core-internal-OptionRev.md) | Same as `Option` , except that the order of the variants is reversed. This is used as the return type of some libfuncs for efficiency reasons.[...](./core-internal-OptionRev.md) |
| [LoopResult](./core-internal-LoopResult.md) | The return type for loops with an early return.[...](./core-internal-LoopResult.md) |

[Extern functions](./core-internal-extern_functions.md)
 ---
| | |
|:---|:---|
| [revoke_ap_tracking](./core-internal-revoke_ap_tracking.md) | [...](./core-internal-revoke_ap_tracking.md) |
| [require_implicit](./core-internal-require_implicit.md) | Function to enforce that `Implicit`  is used by a function calling it. Note: This extern function is not mapped to a Sierra function, and all usages of it are removed during compilation.[...](./core-internal-require_implicit.md) |
