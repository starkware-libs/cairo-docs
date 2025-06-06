# poseidon

Poseidon hash related traits implementations and functions.
This module provides cryptographic hash functions based on the Poseidon permutation.
The Poseidon hash function is an arithmetic-friendly hash function optimized for use in
zero-knowledge proof systems. This module implements the Poseidon hash using a sponge
construction for arbitrary-length inputs.
# Examples

```cairo
use core::hash::HashStateTrait;
use core::poseidon::PoseidonTrait;

// Create a new hash state
let mut state = PoseidonTrait::new();

// Update with values
state = state.update(1);
state = state.update(2);

// Finalize to get the hash
let hash = state.finalize();
```

Fully qualified path: [core](./core.md)::[poseidon](./core-poseidon.md)


[Free functions](./core-poseidon-free_functions.md)
 ---
| | |
|:---|:---|
| [poseidon_hash_span](./core-poseidon-poseidon_hash_span.md) | Computes the Poseidon hash on the given span input. Applies the sponge construction to digest many elements. To distinguish between use cases, the capacity element is initialized to 0.[...](./core-poseidon-poseidon_hash_span.md) |

[Structs](./core-poseidon-structs.md)
 ---
| | |
|:---|:---|
| [HashState](./core-poseidon-HashState.md) | State for Poseidon hash.[...](./core-poseidon-HashState.md) |

[Traits](./core-poseidon-traits.md)
 ---
| | |
|:---|:---|
| [PoseidonTrait](./core-poseidon-PoseidonTrait.md) | [...](./core-poseidon-PoseidonTrait.md) |

[Impls](./core-poseidon-impls.md)
 ---
| | |
|:---|:---|
| [PoseidonImpl](./core-poseidon-PoseidonImpl.md) | A trait for creating a new Poseidon hash state.[...](./core-poseidon-PoseidonImpl.md) |

[Extern types](./core-poseidon-extern_types.md)
 ---
| | |
|:---|:---|
| [Poseidon](./core-poseidon-Poseidon.md) | [...](./core-poseidon-Poseidon.md) |

[Extern functions](./core-poseidon-extern_functions.md)
 ---
| | |
|:---|:---|
| [hades_permutation](./core-poseidon-hades_permutation.md) | [...](./core-poseidon-hades_permutation.md) |
