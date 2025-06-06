# panics

Core panic mechanism.
This module provides the core panic functionality used for error handling in Cairo.
It defines the basic types and functions used to trigger and manage panics, which
are Cairo's mechanism for handling unrecoverable errors.
Panics can be triggered in several ways:
Using the `panic` function:
```cairo
use core::panics::panic;

panic(array!['An error occurred']);
```

Or using the `panic!` macro:
```cairo
panic!("Panic message");
```

This macro internally converts the message into a `ByteArray` and uses `panic_with_byte_array`.

Fully qualified path: [core](./core.md)::[panics](./core-panics.md)


[Free functions](./core-panics-free_functions.md)
 ---
| | |
|:---|:---|
| [panic_with_byte_array](./core-panics-panic_with_byte_array.md) | Panics with a `ByteArray`  message. Constructs a panic message by prepending the `BYTE_ARRAY_MAGIC`  value and serializing the provided `ByteArray`  into the panic data.[...](./core-panics-panic_with_byte_array.md) |

[Structs](./core-panics-structs.md)
 ---
| | |
|:---|:---|
| [Panic](./core-panics-Panic.md) | Represents a panic condition in Cairo. A `Panic`  is created when the program encounters an unrecoverable error condition and needs to terminate execution.[...](./core-panics-Panic.md) |

[Enums](./core-panics-enums.md)
 ---
| | |
|:---|:---|
| [PanicResult](./core-panics-PanicResult.md) | Result type for operations that can trigger a panic.[...](./core-panics-PanicResult.md) |

[Extern functions](./core-panics-extern_functions.md)
 ---
| | |
|:---|:---|
| [panic](./core-panics-panic.md) | Triggers an immediate panic with the provided data and terminates execution.[...](./core-panics-panic.md) |
