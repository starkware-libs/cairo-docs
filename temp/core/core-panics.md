# panics

Panics. Core panic mechanism.  This module provides the core panic functionality used for error handling in Cairo. It defines the basic types and functions used to trigger and manage panics, which are Cairo's mechanism for handling unrecoverable errors.  Panics can be triggered in several ways:  Using the `panic` function:
```cairo
use core::panics::panic;

panic(array!['An error occurred']);
```
Or using the `panic!` macro:
```cairo
panic!("Panic message");
```
This macro internally converts the message into a `ByteArray` and uses `panic_with_byte_array`.

Fully qualified path: `core::panics`

## Free functions

- [panic_with_byte_array](./core-panics-panic_with_byte_array.md)

## Structs

- [Panic](./core-panics-Panic.md)

## Enums

- [PanicResult](./core-panics-PanicResult.md)

## Extern functions

- [panic](./core-panics-panic.md)

