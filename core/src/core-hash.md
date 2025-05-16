# hash

Generic hashing support.This module provides a hash state abstraction that can be updated with values and finalized to produce a hash. This allows for flexible and efficient hashing of any type with different hash functions.The simplest way to make a type hashable is to use `#[derive(Hash)]`. Hashing a value is done by initiating a `HashState` corresponding to a hash function, updating it with the value, and then finalizing it to get the hash result.  # ExamplesBasic usage with Pedersen and Poseidon hash:
```cairo
use core::pedersen::PedersenTrait;
use core::poseidon::PoseidonTrait;

#[derive(Copy, Drop, Hash)]
struct Person {
    id: u32,
    phone: u64,
}

fn main() {
  let person1 = Person { id: 1, phone: 555_666_7777 };
  let person2 = Person { id: 2, phone: 555_666_7778 };

  assert!(
      PedersenTrait::new(0)
          .update_with(person1)
          .finalize() != PedersenTrait::new(0)
          .update_with(person2)
          .finalize(),
  );
  assert!(
      PoseidonTrait::new()
          .update_with(person1)
          .finalize() != PoseidonTrait::new()
          .update_with(person2)
          .finalize(),
  );
}
```

Fully qualified path: `core::hash`

## Modules

- [into_felt252_based](./core-hash-into_felt252_based.md)

## Traits

- [HashStateTrait](./core-hash-HashStateTrait.md)

- [Hash](./core-hash-Hash.md)

- [LegacyHash](./core-hash-LegacyHash.md)

- [HashStateExTrait](./core-hash-HashStateExTrait.md)

