# pedersen

Pedersen hash related traits implementations.
This module provides an implementation of the Pedersen hash function, which is a
collision-resistant cryptographic hash function.
The `HashState` struct represents the state of a Pedersen hash computation. It contains a
single `felt252` field `state` that holds the current hash value.
The `PedersenTrait` provides a `new` method to create a new `HashState` from a base value.
The `HashStateTrait` defined in the Hash module provides the `update` and `finalize` methods
to update the hash state and obtain the final hash value, respectively.
# Examples

```cairo
use core::hash::HashStateTrait;
use core::pedersen::PedersenTrait;

let mut state = PedersenTrait::new(0);
state = state.update(1);
state = state.update(2);
let hash = state.finalize();
assert!(hash == 0x07546be9ecb576c12cd00962356afd90b615d8ef50605bc13badfd1fd218c0d5);
```

Fully qualified path: [core](./core.md)::[pedersen](./core-pedersen.md)


[Structs](./core-pedersen-structs.md)
 ---
| | |
|:---|:---|
| [HashState](./core-pedersen-HashState.md) | Represents the current state of a Pedersen hash computation. The state is maintained as a single `felt252`  value, which is updated through the `HashStateTrait::finalize`  method.[...](./core-pedersen-HashState.md) |

[Traits](./core-pedersen-traits.md)
 ---
| | |
|:---|:---|
| [PedersenTrait](./core-pedersen-PedersenTrait.md) | [...](./core-pedersen-PedersenTrait.md) |

[Impls](./core-pedersen-impls.md)
 ---
| | |
|:---|:---|
| [PedersenImpl](./core-pedersen-PedersenImpl.md) | A trait for creating a new Pedersen hash state.[...](./core-pedersen-PedersenImpl.md) |

[Extern types](./core-pedersen-extern_types.md)
 ---
| | |
|:---|:---|
| [Pedersen](./core-pedersen-Pedersen.md) | [...](./core-pedersen-Pedersen.md) |

[Extern functions](./core-pedersen-extern_functions.md)
 ---
| | |
|:---|:---|
| [pedersen](./core-pedersen-pedersen.md) | [...](./core-pedersen-pedersen.md) |
