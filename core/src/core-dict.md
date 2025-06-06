# dict

A dictionary-like data structure that maps `felt252` keys to values of any type.
The `Felt252Dict` provides efficient key-value storage with operations for inserting,
retrieving, and updating values. Each operation creates a new entry that can be validated
through a process called squashing.
# Examples

One can create a new dictionary using the `Default::default` method:
```cairo
use core::dict::Felt252Dict;

let mut dict: Felt252Dict<u8> = Default::default();
```

... then insert new values corresponding to a given key with the `Felt252DictTrait::insert`
method, and retrieve any value given a key with the `Felt252DictTrait::get` method.
```cairo
dict.insert(0, 10);
dict.insert(1, 20);
assert!(dict.get(0) == 10);
assert!(dict.get(1) == 20);

dict.insert(0, 20);
assert!(dict.get(0) == 20);
```

It is also possible to use the `Felt252DictTrait::entry` method to retrieve the last entry
given a certain key.
In this case, the method takes ownership of the dictionary and returns the entry to update.
After that, using the `Felt252DictEntryTrait::finalize` allows to create a new entry in the
dictionary.
Using `entry` and `finalize` methods can be very useful given that it does not require the type
in the dictionary to be copyable, meaning that we can use non-copyable types like arrays as
dictionary values.
```cairo
use core::dict::Felt252Dict;

let mut dict: Felt252Dict<u8> = Default::default();
dict.insert(0, 10);

let (entry, prev_value) = dict.entry(0);
let new_value: u8 = 20;
dict = entry.finalize(new_value);
```

Fully qualified path: [core](./core.md)::[dict](./core-dict.md)


[Traits](./core-dict-traits.md)
 ---
| | |
|:---|:---|
| [Felt252DictTrait](./core-dict-Felt252DictTrait.md) | Basic trait for the `Felt252Dict`  type.[...](./core-dict-Felt252DictTrait.md) |
| [Felt252DictEntryTrait](./core-dict-Felt252DictEntryTrait.md) | Basic trait for the `Felt252DictEntryTrait`  type.[...](./core-dict-Felt252DictEntryTrait.md) |
| [SquashedFelt252DictTrait](./core-dict-SquashedFelt252DictTrait.md) | [...](./core-dict-SquashedFelt252DictTrait.md) |

[Extern types](./core-dict-extern_types.md)
 ---
| | |
|:---|:---|
| [Felt252Dict](./core-dict-Felt252Dict.md) | A dictionary that maps `felt252`  keys to a value of any type.[...](./core-dict-Felt252Dict.md) |
| [SquashedFelt252Dict](./core-dict-SquashedFelt252Dict.md) | A dictionary in a squashed state. It cannot be mutated anymore.[...](./core-dict-SquashedFelt252Dict.md) |
| [Felt252DictEntry](./core-dict-Felt252DictEntry.md) | An intermediate type that is returned after calling the `entry`  method that consumes ownership of the dictionary. This ensures that the dictionary cannot be mutated until the entry is[...](./core-dict-Felt252DictEntry.md) |
