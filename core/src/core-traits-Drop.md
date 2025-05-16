# Drop

A trait for types that can be safely dropped.Types implementing `Drop` can be automatically discarded when they go out of scope. The drop operation is a no-op - it simply indicates to the compiler that this type can be safely discarded.  # DerivingThis trait can be automatically derived using `#[derive(Drop)]`. All basic types implement `Drop` by default, except for `Felt252Dict`.  # ExamplesWithout `Drop`:
```cairo
struct Point {
    x: u128,
    y: u128,
}

fn foo(p: Point) {} // Error: `p` cannot be dropped
```
With `Drop`:
```cairo
#[derive(Drop)]
struct Point {
    x: u128,
    y: u128,
}

fn foo(p: Point) {} // OK: `p` is dropped at the end of the function
```

Fully qualified path: `core::traits::Drop`

<pre><code class="language-rust">pub trait Drop&lt;T&gt;;</code></pre>

