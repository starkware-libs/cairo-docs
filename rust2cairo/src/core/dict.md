# Dictionaries

Where arrays store values in a contiguous segment of memory at an index relative to the start of the array, [`Felt252Dict`s][dict] store values by key.
Cairo's `Felt252Dict` uses `felt252` as the key type, which can represent integers, short strings
(31 characters or less), or other values that can be converted to `felt252`.

`Felt252Dict`s are efficient key-value storage structures in Cairo that create new entries for each operation.
When a dictionary goes out of scope, it must be squashed to validate all operations.
You can create a dictionary using `Default::default()`.

```cairo
{{#include ../../listings/core/dict/src/lib.cairo}}
```

[dict]: https://book.cairo-lang.org/ch03-02-dictionaries.html
