# nullable

A wrapper type for handling optional values.
`Nullable<T>` is a wrapper type that can either contain a value stored in a `Box<T>`
or be null. It provides a safe way to handle optional values without the risk of
dereferencing null pointers.
This makes it particularly useful in dictionaries that store complex data structures that don't
implement the `Felt252DictValue` trait; instead, they can be wrapped inside a `Nullable`.
# Examples

Basic usage:
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

Fully qualified path: [core](./core.md)::[nullable](./core-nullable.md)


[Enums](./core-nullable-enums.md)
 ---
| | |
|:---|:---|
| [FromNullableResult](./core-nullable-FromNullableResult.md) | Represents the result of matching a `Nullable`  value. Used to safely handle both null and non-null cases when using `match_nullable`  on a `Nullable` .[...](./core-nullable-FromNullableResult.md) |

[Traits](./core-nullable-traits.md)
 ---
| | |
|:---|:---|
| [NullableTrait](./core-nullable-NullableTrait.md) | [...](./core-nullable-NullableTrait.md) |

[Extern types](./core-nullable-extern_types.md)
 ---
| | |
|:---|:---|
| [Nullable](./core-nullable-Nullable.md) | A type that can either be null or contain a boxed value.[...](./core-nullable-Nullable.md) |

[Extern functions](./core-nullable-extern_functions.md)
 ---
| | |
|:---|:---|
| [null](./core-nullable-null.md) | [...](./core-nullable-null.md) |
| [match_nullable](./core-nullable-match_nullable.md) | [...](./core-nullable-match_nullable.md) |
