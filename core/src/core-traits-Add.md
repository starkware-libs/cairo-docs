# Add

The addition operator `+`.  # Examples`Add`able types:
```cairo
assert!(1_u8 + 2_u8 == 3_u8);
```
Implementing `Add` for a type:
```cairo
#[derive(Copy, Drop, PartialEq)]
struct Point {
    x: u32,
    y: u32,
}

impl PointAdd of Add<Point> {
    fn add(lhs: Point, rhs: Point) -> Point {
        Point {
            x: lhs.x + rhs.x,
            y: lhs.y + rhs.y,
        }
    }
}

let p1 = Point { x: 1, y: 0 };
let p2 = Point { x: 2, y: 3 };
let p3 = p1 + p2;
assert!(p3 == Point { x: 3, y: 3 });
```

Fully qualified path: `core::traits::Add`

<pre><code class="language-rust">pub trait Add&lt;T&gt;</code></pre>

## Trait functions

### add

Performs the `+` operation.  # Examples
```cairo
assert!(12 + 1 == 13);
```

Fully qualified path: `core::traits::Add::add`

<pre><code class="language-rust">fn add(lhs: T, rhs: T) -&gt; T</code></pre>


