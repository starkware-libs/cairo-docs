# array

A contiguous collection of elements of the same type in memory, written
`Array<T>`.
Arrays have O(1) indexing, O(1) push and O(1) pop
(from the front).
Arrays can only be mutated by appending to the end or popping from the front.
# Examples

You can explicitly create an [`Array`](./core-array-Array.md) with `ArrayTrait::new`:
```cairo
let arr: Array<usize> = ArrayTrait::new();
```

...or by using the `array!` macro:
```cairo
let arr: Array<usize> = array![];

let arr: Array<usize> = array![1, 2, 3, 4, 5];
```

You can `append` values onto the end of an array:
```cairo
let mut arr = array![1, 2];
arr.append(3);
```

Popping values from the front works like this:
```cairo
let mut arr = array![1, 2];
let one = arr.pop_front(); // Returns Some(1)
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

Fully qualified path: [core](./core.md)::[array](./core-array.md)


[Structs](./core-array-structs.md)
 ---
| | |
|:---|:---|
| [Span](./core-array-Span.md) | A span is a view into a contiguous collection of the same type - such as `Array` . It is a structure with a single field that holds a snapshot of an array. `Span`  implements the `Copy`  and the[...](./core-array-Span.md) |
| [SpanIter](./core-array-SpanIter.md) | An iterator struct over a span collection.[...](./core-array-SpanIter.md) |
| [ArrayIter](./core-array-ArrayIter.md) | An iterator struct over an array collection.[...](./core-array-ArrayIter.md) |

[Traits](./core-array-traits.md)
 ---
| | |
|:---|:---|
| [ToSpanTrait](./core-array-ToSpanTrait.md) | `ToSpanTrait`  converts a data structure into a span of its data.[...](./core-array-ToSpanTrait.md) |
| [ArrayTrait](./core-array-ArrayTrait.md) | [...](./core-array-ArrayTrait.md) |
| [SpanTrait](./core-array-SpanTrait.md) | [...](./core-array-SpanTrait.md) |

[Impls](./core-array-impls.md)
 ---
| | |
|:---|:---|
| [SpanIndex](./core-array-SpanIndex.md) | [...](./core-array-SpanIndex.md) |

[Extern types](./core-array-extern_types.md)
 ---
| | |
|:---|:---|
| [Array](./core-array-Array.md) | A collection of elements of the same type contiguous in memory.[...](./core-array-Array.md) |
