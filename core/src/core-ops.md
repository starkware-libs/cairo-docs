# ops

Overloadable operators.Implementing these traits allows you to overload certain operators.Note: Other overloadable operators are also defined in the [`core::traits`](./core-traits.md) module.Only operators backed by traits can be overloaded. For example, the addition assignment operator (`+=`) can be overloaded through the [`AddAssign`](`AddAssign`) trait, but since the assignment operator (`=`) has no backing trait, there is no way of overloading its semantics. Additionally, this module does not provide any mechanism to create new operators.Implementations of operator traits should be unsurprising in their respective contexts, keeping in mind their usual meanings and operator precedence. For example, when implementing [`MulAssign`](`MulAssign`), the operation should have some resemblance to multiplication assignment.  # ExamplesThis example creates a `Point` struct that implements [`AddAssign`](`AddAssign`) and [`SubAssign`](`SubAssign`), and then demonstrates adding and subtracting two `Point`s to themselves.
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

Fully qualified path: `core::ops`

## Modules

- [index](./core-ops-index.md)

## Structs

- [Range](./core-ops-range-Range.md)

- [RangeInclusive](./core-ops-range-RangeInclusive.md)

- [RangeInclusiveIterator](./core-ops-range-RangeInclusiveIterator.md)

- [RangeIterator](./core-ops-range-RangeIterator.md)

## Traits

- [AddAssign](./core-ops-arith-AddAssign.md)

- [DivAssign](./core-ops-arith-DivAssign.md)

- [MulAssign](./core-ops-arith-MulAssign.md)

- [RemAssign](./core-ops-arith-RemAssign.md)

- [SubAssign](./core-ops-arith-SubAssign.md)

- [Deref](./core-ops-deref-Deref.md)

- [DerefMut](./core-ops-deref-DerefMut.md)

- [Fn](./core-ops-function-Fn.md)

- [FnOnce](./core-ops-function-FnOnce.md)

- [Index](./core-ops-index-Index.md)

- [IndexView](./core-ops-index-IndexView.md)

- [RangeInclusiveTrait](./core-ops-range-RangeInclusiveTrait.md)

- [RangeTrait](./core-ops-range-RangeTrait.md)

