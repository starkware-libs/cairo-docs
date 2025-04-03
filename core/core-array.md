# array

Module for `Array` and other continuous same type collections. A contiguous collection of elements of the same type in memory, written `Array<T>`.  Arrays have O(1) indexing, O(1) push and O(1) pop (from the front).  Arrays can only be mutated by appending to the end or popping from the front.  # Examples  You can explicitly create an [`Array`](./core-array-Array.md) with [`ArrayTrait::new`]([`ArrayTrait::new`]):
```cairo
let arr: Array<usize> = ArrayTrait::new();
```
...or by using the `array!` macro:
```cairo
let arr: Array<usize> = array![];

let arr: Array<usize> = array![1, 2, 3, 4, 5];
```
You can [`append`]([`append`]) values onto the end of an array:
```cairo
let mut arr = array![1, 2];
arr.append(3);
```
Popping values from the front works like this:
```cairo
let mut arr = array![1, 2];
let one = arr.pop_front(); // Returns Option::Some(1)
```
Arrays support indexing (through the [`IndexView`](./core-traits-IndexView.md) trait):
```cairo
let arr = array![1, 2, 3];
let three = arr[2]; // Returns a snapshot (@T)
```
Arrays can be converted to [`Span`](./core-array-Span.md)s for read-only access:
```cairo
let arr = array![1, 2, 3];
let span = arr.span();
```
A span can be manipulated without affecting the original array:
```cairo
let mut arr = array![1, 2, 3];
let mut span = arr.span();
span.pop_back();
assert!(arr == array![1, 2, 3]);
```

Fully qualified path: `core::array`

## Structs

- [Span](./core-array-Span.md)

- [SpanIter](./core-array-SpanIter.md)

- [ArrayIter](./core-array-ArrayIter.md)

## Traits

- [ToSpanTrait](./core-array-ToSpanTrait.md)

- [ArrayTrait](./core-array-ArrayTrait.md)

- [SpanTrait](./core-array-SpanTrait.md)

## Impls

- [SpanIndex](./core-array-SpanIndex.md)

## Extern types

- [Array](./core-array-Array.md)

## Extern functions

- [array_snapshot_pop_front](./core-array-array_snapshot_pop_front.md)

