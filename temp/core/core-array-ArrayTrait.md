# ArrayTrait

Fully qualified path: `core::array::ArrayTrait`

```rust
pub trait ArrayTrait<T>
```

## Trait functions

### new

Constructs a new, empty `Array<T>`.  # Examples
```cairo
let arr: Array<u32> = ArrayTrait::new();

let arr = ArrayTrait::<u128>::new();
```
It is also possible to use the `array!` macro to create a new array.
```cairo
let arr: Array<bool> = array![];
```

Fully qualified path: `core::array::ArrayTrait::new`

```rust
fn new() -> Array<T> nopanic
```


### append

Adds a value of type `T` to the end of the array.  # Examples
```cairo
let mut arr: Array<u8> = array![1, 2];
arr.append(3);
assert!(arr == array![1, 2, 3]);
```

Fully qualified path: `core::array::ArrayTrait::append`

```rust
fn append(ref self: Array<T>, value: T) nopanic
```


### append_span

Adds a span to the end of the array.  # Examples
```cairo
let mut arr: Array<u8> = array![];
arr.append_span(array![1, 2, 3].span());
assert!(arr == array![1, 2, 3]);
```

Fully qualified path: `core::array::ArrayTrait::append_span`

```rust
fn append_span<+Clone<T>, +Drop<T>>(ref self: Array<T>, span: Span<T>)
```


### pop_front

Pops a value from the front of the array. Returns `Option::Some(value)` if the array is not empty, `Option::None` otherwise.  # Examples
```cairo
let mut arr = array![2, 3, 4];
assert!(arr.pop_front() == Option::Some(2));
assert!(arr.pop_front() == Option::Some(3));
assert!(arr.pop_front() == Option::Some(4));
assert!(arr.pop_front().is_none());
```

Fully qualified path: `core::array::ArrayTrait::pop_front`

```rust
fn pop_front(ref self: Array<T>) -> Option<T> nopanic
```


### pop_front_consume

Pops a value from the front of the array. Returns an option containing the remaining array and the value removed if the array is not empty, otherwise `Option::None` and drops the array.  # Examples
```cairo
let arr = array![2, 3, 4];
assert!(arr.pop_front_consume() == Option::Some((array![3, 4], 2)));

let arr: Array<u8> = array![];
assert!(arr.pop_front_consume().is_none());
```

Fully qualified path: `core::array::ArrayTrait::pop_front_consume`

```rust
fn pop_front_consume(self: Array<T>) -> Option<(Array<T>, T)> nopanic
```


### get

Returns an option containing a box of a snapshot of the element at the given 'index' if the array contains this index, 'Option::None' otherwise.  Element at index 0 is the front of the array.  # Examples
```cairo
let arr = array![2, 3, 4];
assert!(arr.get(1).unwrap().unbox() == @3);
```

Fully qualified path: `core::array::ArrayTrait::get`

```rust
fn get(self: @Array<T>, index: usize) -> Option<Box<@T>>
```


### at

Returns a snapshot of the element at the given index.  Element at index 0 is the front of the array.  # Panics  Panics if the index is out of bounds.  # Examples
```cairo
let mut arr: Array<usize> = array![3,4,5,6];
assert!(arr.at(1) == @4);
```

Fully qualified path: `core::array::ArrayTrait::at`

```rust
fn at(self: @Array<T>, index: usize) -> @T
```


### len

Returns the length of the array as a `usize` value.  # Examples
```cairo
let arr = array![2, 3, 4];
assert!(arr.len() == 3);
```

Fully qualified path: `core::array::ArrayTrait::len`

```rust
fn len(self: @Array<T>) -> usize
```


### is_empty

Returns whether the array is empty or not.  # Examples
```cairo
let mut arr = array![];
assert!(arr.is_empty());
arr.append(1);
assert!(!arr.is_empty());
```

Fully qualified path: `core::array::ArrayTrait::is_empty`

```rust
fn is_empty(self: @Array<T>) -> bool
```


### span

Returns a span of the array.  # Examples
```cairo
let arr: Array<u8> = array![1, 2, 3];
let span: Span<u8> = arr.span();
```

Fully qualified path: `core::array::ArrayTrait::span`

```rust
fn span(snapshot: @Array<T>) -> Span<T>
```


