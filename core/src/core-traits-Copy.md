# Copy

A trait for copying values.By default, variables in Cairo have 'move semantics', meaning they are moved when used. However, types implementing `Copy` have 'copy semantics', allowing the value to be duplicated instead of moved.  # DerivingThis trait can be automatically derived using `#[derive(Copy)]`. Most basic types implement `Copy` by default.  # ExamplesWithout `Copy` (move semantics):
```cairo
#[derive(Drop)]
struct Point {
    x: u128,
    y: u128,
}

fn main() {
    let p1 = Point { x: 5, y: 10 };
    foo(p1);
    foo(p1); // error: Variable was previously moved.
}

fn foo(p: Point) {}
```
With `Copy` (copy semantics):
```cairo
#[derive(Copy, Drop)]
struct Point {
    x: u128,
    y: u128,
}

fn main() {
    let p1 = Point { x: 5, y: 10 };
    foo(p1);
    foo(p1); // works: `p1` is copied when passed to `foo`
}

fn foo(p: Point) {}
```

Fully qualified path: `core::traits::Copy`

<pre><code class="language-rust">pub trait Copy&lt;T&gt;;</code></pre>

