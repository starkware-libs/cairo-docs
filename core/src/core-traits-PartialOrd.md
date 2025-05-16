# PartialOrd

Trait for comparing types that form a [partial order](https://en.wikipedia.org/wiki/Partial_order).The `lt`, `le`, `gt`, and `ge` methods of this trait can be called using the `<`, `<=`, `>`, and `>=` operators, respectively.PartialOrd is not derivable, but can be implemented manually  # Implementing `PartialOrd`Here's how to implement `PartialOrd` for a custom type. This example implements comparison operations for a 2D point where points are compared based on their squared Euclidean distance from the origin (0,0):
```cairo
#[derive(Copy, Drop, PartialEq)]
struct Point {
    x: u32,
    y: u32,
}

impl PointPartialOrd of PartialOrd<Point> {
    fn lt(lhs: Point, rhs: Point) -> bool {
        let lhs_dist = lhs.x * lhs.x + lhs.y * lhs.y;
        let rhs_dist = rhs.x * rhs.x + rhs.y * rhs.y;
        lhs_dist < rhs_dist
    }
}

let p1 = Point { x: 1, y: 1 }; // distance = 2
let p2 = Point { x: 2, y: 2 }; // distance = 8

assert!(p1 < p2);
assert!(p1 <= p2);
assert!(p2 > p1);
assert!(p2 >= p1);
```
Note that only the `lt` method needs to be implemented. The other comparison operations (`le`, `gt`, `ge`) are automatically derived from `lt`. However, you can override them for better performance if needed.

Fully qualified path: `core::traits::PartialOrd`

<pre><code class="language-rust">pub trait PartialOrd&lt;T&gt;</code></pre>

## Trait functions

### lt

Tests less than (for `self` and `other`) and is used by the `<` operator.  # Examples
```cairo
assert_eq!(1 < 1, false);
assert_eq!(1 < 2, true);
assert_eq!(2 < 1, false);
```

Fully qualified path: `core::traits::PartialOrd::lt`

<pre><code class="language-rust">fn lt(lhs: T, rhs: T) -&gt; bool</code></pre>


### ge

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator.  # Examples
```cairo
assert_eq!(1 <= 1, true);
assert_eq!(1 <= 2, true);
assert_eq!(2 <= 1, false);
```

Fully qualified path: `core::traits::PartialOrd::ge`

<pre><code class="language-rust">fn ge(lhs: T, rhs: T) -&gt; bool</code></pre>


### gt

Tests greater than (for `self` and `other`) and is used by the `>` operator.  # Examples
```cairo
assert_eq!(1 > 1, false);
assert_eq!(1 > 2, false);
assert_eq!(2 > 1, true);
```

Fully qualified path: `core::traits::PartialOrd::gt`

<pre><code class="language-rust">fn gt(lhs: T, rhs: T) -&gt; bool</code></pre>


### le

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator.  # Examples
```cairo
assert_eq!(1 >= 1, true);
assert_eq!(1 >= 2, false);
assert_eq!(2 >= 1, true);
```

Fully qualified path: `core::traits::PartialOrd::le`

<pre><code class="language-rust">fn le(lhs: T, rhs: T) -&gt; bool</code></pre>


