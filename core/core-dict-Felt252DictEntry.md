# Felt252DictEntry

An intermediate type that is returned after calling the `entry` method that consumes ownership of the dictionary. This ensures that the dictionary cannot be mutated until the entry is finalized, which restores ownership of the dictionary.

Fully qualified path: `core::dict::Felt252DictEntry`

```rust
pub extern type Felt252DictEntry<T>
```

