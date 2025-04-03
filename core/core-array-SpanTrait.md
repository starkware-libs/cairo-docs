# SpanTrait

Fully qualified path: `core::array::SpanTrait`

```rust
pub trait SpanTrait<T>
```

## Trait functions

### pop_front

Pops a value from the front of the span. Returns `Option::Some(@value)` if the array is not empty, `Option::None` otherwise.  # Examples
```cairo
let mut span = array![1, 2, 3].span();
assert!(span.pop_front() == Option::Some(@1));
```

Fully qualified path: `core::array::SpanTrait::pop_front`

```rust
fn pop_front(ref self: Span<T>) -> Option<@T>
```


### pop_back

Pops a value from the back of the span. Returns `Option::Some(@value)` if the array is not empty, `Option::None` otherwise.  # Examples
```cairo
let mut span = array![1, 2, 3].span();
assert!(span.pop_back() == Option::Some(@3));
```

Fully qualified path: `core::array::SpanTrait::pop_back`

```rust
fn pop_back(ref self: Span<T>) -> Option<@T>
```


### multi_pop_front

Pops multiple values from the front of the span. Returns an option containing a snapshot of a box that contains the values as a fixed-size array if the action completed successfully, 'Option::None' otherwise.  # Examples
```cairo
let mut span = array![1, 2, 3].span();
let result = *(span.multi_pop_front::<2>().unwrap());
let unboxed_result = result.unbox();
assert!(unboxed_result == [1, 2]);
```

Fully qualified path: `core::array::SpanTrait::multi_pop_front`

```rust
fn multi_pop_front<const SIZE: usize>(ref self: Span<T>) -> Option<@Box<[T; SIZE]>>
```


### multi_pop_back

Pops multiple values from the back of the span. Returns an option containing a snapshot of a box that contains the values as a fixed-size array if the action completed successfully, 'Option::None' otherwise.  # Examples
```cairo
let mut span = array![1, 2, 3].span();
let result = *(span.multi_pop_back::<2>().unwrap());
let unboxed_result = result.unbox();
assert!(unboxed_result == [2, 3]);;
```

Fully qualified path: `core::array::SpanTrait::multi_pop_back`

```rust
fn multi_pop_back<const SIZE: usize>(ref self: Span<T>) -> Option<@Box<[T; SIZE]>>
```


### get

Returns an option containing a box of a snapshot of the element at the given 'index' if the span contains this index, 'Option::None' otherwise.  Element at index 0 is the front of the array.  # Examples
```cairo
let span = array![2, 3, 4];
assert!(span.get(1).unwrap().unbox() == @3);
```

Fully qualified path: `core::array::SpanTrait::get`

```rust
fn get(self: Span<T>, index: usize) -> Option<Box<@T>>
```


### at

Returns a snapshot of the element at the given index.  Element at index 0 is the front of the array.  # Panics  Panics if the index is out of bounds.  # Examples
```cairo
let span = array![2, 3, 4].span();
assert!(span.at(1) == @3);
```

Fully qualified path: `core::array::SpanTrait::at`

```rust
fn at(self: Span<T>, index: usize) -> @T
```


### slice

Returns a span containing values from the 'start' index, with amount equal to 'length'.  # Examples
```cairo
let span = array![1, 2, 3].span();
assert!(span.slice(1, 2) == array![2, 3].span());
```

Fully qualified path: `core::array::SpanTrait::slice`

```rust
fn slice(self: Span<T>, start: usize, length: usize) -> Span<T>
```


### len

Returns the length of the span as a `usize` value.  # Examples
```cairo
let span = array![2, 3, 4].span();
assert!(span.len() == 3);
```

Fully qualified path: `core::array::SpanTrait::len`

```rust
fn len(self: Span<T>) -> usize
```


### is_empty

Returns whether the span is empty or not.  # Examples
```cairo
let span: Span<felt252> = array![].span();
assert!(span.is_empty());
let span = array![1, 2, 3].span();
assert!(!span.is_empty());
```

Fully qualified path: `core::array::SpanTrait::is_empty`

```rust
fn is_empty(self: Span<T>) -> bool
```


