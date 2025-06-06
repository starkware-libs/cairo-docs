# boolean

Boolean operations.
The `bool` type is a primitive type in Cairo representing a boolean value that can be either
`true` or `false`. This module provides trait implementations for boolean operations.
# Examples

Basic boolean operations:
```cairo

let value = true;
assert!(value == true);
assert!(!value == false);
```

Converting to optional values with `BoolTrait::then_some`:
```cairo
use core::boolean::BoolTrait;

let bool_value = true;
let result = bool_value.then_some(42_u8);
assert!(result == Some(42));

let bool_value = false;
let result = bool_value.then_some(42_u8);
assert!(result == None);
```

Fully qualified path: [core](./core.md)::[boolean](./core-boolean.md)


[Traits](./core-boolean-traits.md)
 ---
| | |
|:---|:---|
| [BoolTrait](./core-boolean-BoolTrait.md) | [...](./core-boolean-BoolTrait.md) |
