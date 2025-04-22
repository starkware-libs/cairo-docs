# Felt252DictTrait

Basic trait for the `Felt252Dict` type.

Fully qualified path: `core::dict::Felt252DictTrait`

```rust
pub trait Felt252DictTrait<T>
```

## Trait functions

### insert

Inserts the given value for the given key.  # Examples
```cairo
use core::dict::Felt252Dict;

let mut dict: Felt252Dict<u8> = Default::default();
dict.insert(0, 10);
```

Fully qualified path: `core::dict::Felt252DictTrait::insert`

```rust
fn insert<+Destruct<T>>(ref self: Felt252Dict<T>, key: felt252, value: T)
```


### get

Returns the value stored at the given key. If no value was previously inserted at this key, returns the default value for type T.  # Examples
```cairo
use core::dict::Felt252Dict;

let mut dict: Felt252Dict<u8> = Default::default();
dict.insert(0, 10);
let value = dict.get(0);
assert!(value == 10);
```

Fully qualified path: `core::dict::Felt252DictTrait::get`

```rust
fn get<+Copy<T>>(ref self: Felt252Dict<T>, key: felt252) -> T
```


### squash

Squashes a dictionary and returns the associated `SquashedFelt252Dict`.  # Examples
```cairo
use core::dict::Felt252Dict;

let mut dict: Felt252Dict<u8> = Default::default();
dict.insert(0, 10);
let squashed_dict = dict.squash();
```

Fully qualified path: `core::dict::Felt252DictTrait::squash`

```rust
fn squash(self: Felt252Dict<T>) -> SquashedFelt252Dict<T> nopanic
```


### entry

Retrieves the last entry for a certain key. This method takes ownership of the dictionary and returns the entry to update, as well as the previous value at the given key.  # Examples
```cairo
use core::dict::Felt252Dict;

let mut dict: Felt252Dict<u8> = Default::default();
dict.insert(0, 10);
let (entry, prev_value) = dict.entry(0);
assert!(prev_value == 10);
```

Fully qualified path: `core::dict::Felt252DictTrait::entry`

```rust
fn entry(self: Felt252Dict<T>, key: felt252) -> (Felt252DictEntry<T>, T) nopanic
```


