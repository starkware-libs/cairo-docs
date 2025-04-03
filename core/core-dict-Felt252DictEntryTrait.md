# Felt252DictEntryTrait

Basic trait for the `Felt252DictEntryTrait` type.

Fully qualified path: `core::dict::Felt252DictEntryTrait`

```rust
pub trait Felt252DictEntryTrait<T>
```

## Trait functions

### finalize

Finalizes the changes made to a dictionary entry and gives back the ownership of the dictionary.  # Examples
```cairo
use core::dict::Felt252DictEntryTrait;

// Create a dictionary that stores arrays
let mut dict: Felt252Dict<Nullable<Array<felt252>>> = Default::default();

let a = array![1, 2, 3];
dict.insert(0, NullableTrait::new(a));

let (entry, prev_value) = dict.entry(0);
let new_value = NullableTrait::new(array![4, 5, 6]);
dict = entry.finalize(new_value);
assert!(prev_value == a);
assert!(dict.get(0) == new_value);
```

Fully qualified path: `core::dict::Felt252DictEntryTrait::finalize`

```rust
fn finalize(self: Felt252DictEntry<T>, new_value: T) -> Felt252Dict<T>
```


