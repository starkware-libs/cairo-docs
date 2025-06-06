
[Traits](./core-hash-traits.md)
 ---
| | |
|:---|:---|
| [HashStateTrait](./core-hash-HashStateTrait.md) | A trait for hash state accumulators. Provides methods to update a hash state with new values and finalize it into a hash result.[...](./core-hash-HashStateTrait.md) |
| [Hash](./core-hash-Hash.md) | A trait for values that can be hashed. This trait should be implemented for any type that can be included in a hash calculation. The most common way to implement this trait is by using[...](./core-hash-Hash.md) |
| [LegacyHash](./core-hash-LegacyHash.md) | A trait for hashing values using a `felt252`  as hash state, used for backwards compatibility. NOTE: Implement `Hash`  instead of this trait if possible.[...](./core-hash-LegacyHash.md) |
| [HashStateExTrait](./core-hash-HashStateExTrait.md) | Extension trait for hash state accumulators. This trait adds the `update_with`  method to hash states, allowing you to directly hash values of any type T that implements `Hash`[...](./core-hash-HashStateExTrait.md) |
