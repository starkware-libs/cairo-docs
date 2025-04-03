# NullableTrait

Fully qualified path: `core::nullable::NullableTrait`

```rust
pub trait NullableTrait<T>
```

## Trait functions

### deref

Wrapper for `Deref::deref`. Prefer using `Deref::deref` directly.  This function exists for backwards compatibility.  # Examples  Preferred way:
```cairo
let value: Nullable<u32> = NullableTrait::new(42);
let unwrapped = value.deref();
```
This function method does the same thing:
```cairo
use core::nullable::NullableTrait;
let also_unwrapped = NullableTrait::deref(value);
```

Fully qualified path: `core::nullable::NullableTrait::deref`

```rust
fn deref(nullable: Nullable<T>) -> T
```


### deref_or

Returns the contained value if not null, or returns the provided default value.  # Examples
```cairo
let value: Nullable<u32> = NullableTrait::new(42);
assert!(value.deref_or(0) == 42);

let null_value: Nullable<u32> = Default::default();
assert!(null_value.deref_or(0) == 0);
```

Fully qualified path: `core::nullable::NullableTrait::deref_or`

```rust
fn deref_or<+Drop<T>>(self: Nullable<T>, default: T) -> T
```


### new

Creates a new non-null `Nullable` with the given value.  # Examples
```cairo
let value: Nullable<u32> = NullableTrait::new(42);
assert!(!value.is_null());
```

Fully qualified path: `core::nullable::NullableTrait::new`

```rust
fn new(value: T) -> Nullable<T>
```


### is_null

Returns `true` if the value is null.  # Examples
```cairo
let value: Nullable<u32> = NullableTrait::new(42);
assert!(!value.is_null());

let null_value: Nullable<u32> = Default::default();
assert!(null_value.is_null());
```

Fully qualified path: `core::nullable::NullableTrait::is_null`

```rust
fn is_null(self: @Nullable<T>) -> bool
```


### as_snapshot

Creates a new `Nullable` containing a snapshot of the value.  This is useful when working with non-copyable types inside a `Nullable`. This allows you to keep using the original value while also having access to a snapshot of it, preventing the original value from being moved.  # Examples
```cairo
let value: Nullable<Array<u32>> = NullableTrait::new(array![1, 2, 3]);
let res = (@value).as_snapshot();
assert!(res.deref() == @array![1, 2, 3]);
assert!(value.deref() == array![1, 2, 3]);
```

Fully qualified path: `core::nullable::NullableTrait::as_snapshot`

```rust
fn as_snapshot(self: @Nullable<T>) -> Nullable<@T> nopanic
```


