# nullable

Nullable A wrapper type for handling optional values.  `Nullable<T>` is a wrapper type that can either contain a value stored in a `Box<T>` or be null. It provides a safe way to handle optional values without the risk of dereferencing null pointers.  This makes it particularly useful in dictionaries that store complex data structures that don't implement the `Felt252DictValue` trait; instead, they can be wrapped inside a `Nullable`.  # Examples  Basic usage:
```cairo
let value: Nullable<u32> = NullableTrait::new(10);
let unwrapped_value = value.deref();
```
Handling null values:
```cairo
let null_value: Nullable<u32> = Default::default();
let unwrapped_value = null_value.deref_or(1);
```
Checking if the value is null:
```cairo
let value: Nullable<u32> = NullableTrait::new(10);
let is_null = if value.is_null() {
    // Handle null case
} else {
    // Handle non-null case
};
```

Fully qualified path: `core::nullable`

## Enums

- [FromNullableResult](./core-nullable-FromNullableResult.md)

## Traits

- [NullableTrait](./core-nullable-NullableTrait.md)

## Extern types

- [Nullable](./core-nullable-Nullable.md)

## Extern functions

- [null](./core-nullable-null.md)

- [nullable_from_box](./core-nullable-nullable_from_box.md)

- [match_nullable](./core-nullable-match_nullable.md)

