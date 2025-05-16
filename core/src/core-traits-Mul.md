# Mul

The multiplication operator `*`.  # Examples`Mul`tipliable types:
```cairo
assert!(3_u8 * 2_u8 == 6_u8);
```
Implementing `Mul` for a type:
```cairo
#[derive(Copy, Drop, PartialEq)]
struct Point {
    x: u32,
    y: u32,
}

impl PointMul of Mul<Point> {
    fn mul(lhs: Point, rhs: Point) -> Point {
        Point {
            x: lhs.x * rhs.x,
            y: lhs.y * rhs.y,
        }
    }
}

let p1 = Point { x: 2, y: 3 };
let p2 = Point { x: 1, y: 0 };
let p3 = p1 * p2;
assert!(p3 == Point { x: 2, y: 0 });
```

Fully qualified path: `core::traits::Mul`

<pre><code class="language-rust">pub trait Mul&lt;T&gt;</code></pre>

## Trait functions

### mul

Performs the `*` operation.  # Examples
```cairo
assert!(12 * 2 == 24);
```

Fully qualified path: `core::traits::Mul::mul`

<pre><code class="language-rust">fn mul(lhs: T, rhs: T) -&gt; T</code></pre>


