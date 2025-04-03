# Zeroable

A trait for types that have a concept of zero and can be compared to zero.  This trait is useful for numeric types or any type that has an additive identity element.

Fully qualified path: `core::zeroable::Zeroable`

```rust
pub(crate) trait Zeroable<T>
```

## Trait functions

### zero

Returns the additive identity element of `self`, 0.  This method should return a value that, when added to any other value of type `T`, does not change that value.  # Examples
```cairo
assert!(Zeroable::<i32>::zero() == 0);
```

Fully qualified path: `core::zeroable::Zeroable::zero`

```rust
fn zero() -> T
```


### is_zero

Returns whether `self` is equal to 0, the additive identity element.  # Examples
```cairo
assert!(0.is_zero());
assert!(!5.is_zero());
```

Fully qualified path: `core::zeroable::Zeroable::is_zero`

```rust
fn is_zero(self: T) -> bool
```


### is_non_zero

Returns whether `self` is not equal to 0, the additive identity element.  This method is the logical inverse of `is_zero()`.  # Examples
```cairo
assert!(5.is_non_zero());
assert!(!0.is_non_zero());
```

Fully qualified path: `core::zeroable::Zeroable::is_non_zero`

```rust
fn is_non_zero(self: T) -> bool
```


