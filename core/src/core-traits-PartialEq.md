# PartialEq

Trait for comparisons using the equality operator.Implementing this trait for types provides the `==` and `!=` operators for those types.  # DerivableThis trait can be used with `#[derive]`. When `derive`d on structs, two instances are equal if all fields are equal, and not equal if any fields are not equal. When `derive`d on enums, two instances are equal if they are the same variant and all fields are equal.  # Implementing `PartialEq`An example in which two points are equal if their x and y coordinates are equal.
```cairo
#[derive(Copy, Drop)]
struct Point {
    x: u32,
    y: u32
}

impl PointEq of PartialEq<Point> {
    fn eq(lhs: @Point, rhs: @Point) -> bool {
        lhs.x == rhs.x && lhs.y == rhs.y
    }
}

let p1 = Point { x: 1, y: 2 };
let p2 = Point { x: 1, y: 2 };
assert!(p1 == p2);
assert!(!(p1 != p2));
```

Fully qualified path: `core::traits::PartialEq`

<pre><code class="language-rust">pub trait PartialEq&lt;T&gt;</code></pre>

## Trait functions

### eq

Returns whether `lhs` and `rhs` equal, and is used by `==`.  # Examples
```cairo
assert!(1 == 1);
```

Fully qualified path: `core::traits::PartialEq::eq`

<pre><code class="language-rust">fn eq(lhs: @T, rhs: @T) -&gt; bool</code></pre>


### ne

Returns whether `lhs` and `rhs` are not equal, and is used by `!=`.  # Examples
```cairo
assert!(0 != 1);
```

Fully qualified path: `core::traits::PartialEq::ne`

<pre><code class="language-rust">fn ne(lhs: @T, rhs: @T) -&gt; bool</code></pre>


