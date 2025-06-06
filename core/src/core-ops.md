# ops

Overloadable operators.
Implementing these traits allows you to overload certain operators.
Note: Other overloadable operators are also defined in the [`core::traits`](./core-traits.md) module.
Only operators backed by traits can be overloaded. For
example, the addition assignment operator (`+=`) can be overloaded through the `AddAssign`
trait, but since the assignment operator (`=`) has no backing trait, there
is no way of overloading its semantics. Additionally, this module does not
provide any mechanism to create new operators.
Implementations of operator traits should be unsurprising in their
respective contexts, keeping in mind their usual meanings and
operator precedence. For example, when implementing `MulAssign`, the operation
should have some resemblance to multiplication assignment.
# Examples

This example creates a `Point` struct that implements `AddAssign` and `SubAssign`,
and then demonstrates adding and subtracting two `Point`s to themselves.
```cairo
use core::ops::{AddAssign, SubAssign};

#[derive(Debug, Drop, Copy, PartialEq)]
struct Point {
    x: i32,
    y: i32,
}

impl AddAssignImpl of AddAssign<Point, Point> {
    fn add_assign(ref self: Point, rhs: Point) {
        self = Point { x: self.x + rhs.x, y: self.y + rhs.y }
    }
}

impl SubAssignImpl of SubAssign<Point, Point> {
    fn sub_assign(ref self: Point, rhs: Point) {
        self = Point { x: self.x - rhs.x, y: self.y - rhs.y }
    }
}

fn main() {
    let mut point = Point {x : 3, y: 4};
    point += point;
    assert!(point == Point {x: 6, y: 8});
    point -= point;
    assert!(point == Point {x: 0, y: 0});
}
```

See the documentation for each trait for an example implementation.

Fully qualified path: [core](./core.md)::[ops](./core-ops.md)


[Modules](./core-ops-modules.md)
 ---
| | |
|:---|:---|
| [index](./core-ops-index.md) | Indexing traits for indexing operations on collections. This module provides traits for implementing the indexing operator `[]` , offering two distinct approaches to access elements in collections:[...](./core-ops-index.md) |
| [range](./core-ops-range.md) | Range and iteration utilities. This module provides functionality for creating and iterating over ranges of values. A range represents an interval of values from a start point to an end point.[...](./core-ops-range.md) |
| [arith](./core-ops-arith.md) | Assignment operator traits for arithmetic operations. This module provides traits for implementing assignment operators like `+=` , `-=` , `*=` , `/=`  and `%=`[...](./core-ops-arith.md) |
| [deref](./core-ops-deref.md) | Dereferencing traits for transparent access to wrapped values. This module provides traits that enable accessing the content of wrapped types[...](./core-ops-deref.md) |
| [function](./core-ops-function.md) | Function traits and types. This module defines traits for function-like types that can be called. The two main traits are:[...](./core-ops-function.md) |
## Re-exports

 - ### Structs

| | |
|:---|:---|
| [Range](./core-ops-range-Range.md) | A (half-open) range bounded inclusively below and exclusively above ( `start..end` ). The range `start..end`  contains all values with `start <= x < end` . It is empty if `start >= end` .[...](./core-ops-range-Range.md) |
| [RangeInclusive](./core-ops-range-RangeInclusive.md) | Represents the range start, end .[...](./core-ops-range-RangeInclusive.md) |
| [RangeInclusiveIterator](./core-ops-range-RangeInclusiveIterator.md) | [...](./core-ops-range-RangeInclusiveIterator.md) |
| [RangeIterator](./core-ops-range-RangeIterator.md) | Represents an iterator located at `cur` , whose end is `end`  ( `cur <= end` ).[...](./core-ops-range-RangeIterator.md) |

<br>


 - ### Traits

| | |
|:---|:---|
| [AddAssign](./core-ops-arith-AddAssign.md) | The addition assignment operator `+=` .[...](./core-ops-arith-AddAssign.md) |
| [DivAssign](./core-ops-arith-DivAssign.md) | The division assignment operator `/=` .[...](./core-ops-arith-DivAssign.md) |
| [MulAssign](./core-ops-arith-MulAssign.md) | The multiplication assignment operator `*=` .[...](./core-ops-arith-MulAssign.md) |
| [RemAssign](./core-ops-arith-RemAssign.md) | The remainder assignment operator `%=` .[...](./core-ops-arith-RemAssign.md) |
| [SubAssign](./core-ops-arith-SubAssign.md) | The subtraction assignment operator `-=` .[...](./core-ops-arith-SubAssign.md) |
| [Deref](./core-ops-deref-Deref.md) | A trait for dereferencing a value to provide transparent access to its contents. Implementing this trait allows a type to behave like its inner type, enabling direct access to[...](./core-ops-deref-Deref.md) |
| [DerefMut](./core-ops-deref-DerefMut.md) | A trait for dereferencing in mutable contexts. This trait is similar to `Deref`  but specifically handles cases where the value accessed is mutable. Despite its name, `DerefMut`[...](./core-ops-deref-DerefMut.md) |
| [Fn](./core-ops-function-Fn.md) | The version of the call operator that takes a by-snapshot receiver. Instances of `Fn`  can be called repeatedly. `Fn`  is implemented automatically by closures whose captured variables are all `Copy`[...](./core-ops-function-Fn.md) |
| [FnOnce](./core-ops-function-FnOnce.md) | The version of the call operator that takes a by-value receiver. Instances of `FnOnce`  can be called, but might not be callable multiple[...](./core-ops-function-FnOnce.md) |
| [Index](./core-ops-index-Index.md) | A trait for indexing operations ( `container[index]` ) where the input type is mutated. This trait should be implemented when you want to implement indexing operations on a type that's[...](./core-ops-index-Index.md) |
| [IndexView](./core-ops-index-IndexView.md) | A trait for indexing operations ( `container[index]` ) where the input type is not modified. `container[index]`  is syntactic sugar for `container.index(index)` .[...](./core-ops-index-IndexView.md) |
| [RangeInclusiveTrait](./core-ops-range-RangeInclusiveTrait.md) | [...](./core-ops-range-RangeInclusiveTrait.md) |
| [RangeTrait](./core-ops-range-RangeTrait.md) | [...](./core-ops-range-RangeTrait.md) |

<br>

