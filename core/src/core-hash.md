# hash

Generic hashing support.
This module provides a hash state abstraction that can be updated with values and finalized to
produce a hash. This allows for flexible and efficient hashing of any type with different hash
functions.
The simplest way to make a type hashable is to use `#[derive(Hash)]`. Hashing a value is done by
initiating a `HashState` corresponding to a hash function, updating it with the value, and then
finalizing it to get the hash result.
# Examples

Basic usage with Pedersen and Poseidon hash:
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

Fully qualified path: [core](./core.md)::[hash](./core-hash.md)


[Modules](./core-hash-modules.md)
 ---
| | |
|:---|:---|
| [into_felt252_based](./core-hash-into_felt252_based.md) | Implementation for `Hash`  for types that can be converted into `felt252`  using the `Into`  trait.[...](./core-hash-into_felt252_based.md) |

[Traits](./core-hash-traits.md)
 ---
| | |
|:---|:---|
| [HashStateTrait](./core-hash-HashStateTrait.md) | A trait for hash state accumulators. Provides methods to update a hash state with new values and finalize it into a hash result.[...](./core-hash-HashStateTrait.md) |
| [Hash](./core-hash-Hash.md) | A trait for values that can be hashed. This trait should be implemented for any type that can be included in a hash calculation. The most common way to implement this trait is by using[...](./core-hash-Hash.md) |
| [LegacyHash](./core-hash-LegacyHash.md) | A trait for hashing values using a `felt252`  as hash state, used for backwards compatibility. NOTE: Implement `Hash`  instead of this trait if possible.[...](./core-hash-LegacyHash.md) |
| [HashStateExTrait](./core-hash-HashStateExTrait.md) | Extension trait for hash state accumulators. This trait adds the `update_with`  method to hash states, allowing you to directly hash values of any type T that implements `Hash`[...](./core-hash-HashStateExTrait.md) |
