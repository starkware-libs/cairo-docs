# poseidon

Poseidon Poseidon hash related traits implementations and functions.  This module provides cryptographic hash functions based on the Poseidon permutation.  The Poseidon hash function is an arithmetic-friendly hash function optimized for use in zero-knowledge proof systems. This module implements the Poseidon hash using a sponge construction for arbitrary-length inputs.  # Examples
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

Fully qualified path: `core::poseidon`

## Free functions

- [poseidon_hash_span](./core-poseidon-poseidon_hash_span.md)

## Structs

- [HashState](./core-poseidon-HashState.md)

## Traits

- [PoseidonTrait](./core-poseidon-PoseidonTrait.md)

## Impls

- [PoseidonImpl](./core-poseidon-PoseidonImpl.md)

## Extern types

- [Poseidon](./core-poseidon-Poseidon.md)

## Extern functions

- [hades_permutation](./core-poseidon-hades_permutation.md)

