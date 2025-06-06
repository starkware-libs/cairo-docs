# fmt

Functionality for formatting values.
The main components of this module are:
- `Error`: A type representing formatting errors.
- `Formatter`: A struct that holds the configuration and buffer for formatting.
- `Display`: A trait for standard formatting using the empty format ("{}").
- `Debug`: A trait for debug formatting using the empty format ("{:?}").
- `LowerHex`: A trait for hex formatting in lower case.

The module includes implementations of the `Display`, `Debug` and `LowerHex` traits for
various types.

Fully qualified path: [core](./core.md)::[fmt](./core-fmt.md)


[Modules](./core-fmt-modules.md)
 ---
| | |
|:---|:---|
| [into_felt252_based](./core-fmt-into_felt252_based.md) | Implementations for `Debug`  and `LowerHex`  for types that can be converted into `felt252`  using the `Into`  trait.[...](./core-fmt-into_felt252_based.md) |

[Structs](./core-fmt-structs.md)
 ---
| | |
|:---|:---|
| [Error](./core-fmt-Error.md) | Dedicated type for representing formatting errors.[...](./core-fmt-Error.md) |
| [Formatter](./core-fmt-Formatter.md) | Configuration for formatting.[...](./core-fmt-Formatter.md) |

[Traits](./core-fmt-traits.md)
 ---
| | |
|:---|:---|
| [Display](./core-fmt-Display.md) | A trait for standard formatting, using the empty format ("{}").[...](./core-fmt-Display.md) |
| [Debug](./core-fmt-Debug.md) | A trait for debug formatting, using the empty format ("{:?}").[...](./core-fmt-Debug.md) |
| [LowerHex](./core-fmt-LowerHex.md) | A trait for hex formatting in lower case, using the empty format ("{:x}").[...](./core-fmt-LowerHex.md) |
