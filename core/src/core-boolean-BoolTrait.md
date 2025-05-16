# BoolTrait

Fully qualified path: `core::boolean::BoolTrait`

<pre><code class="language-rust">pub trait BoolTrait&lt;T, +Drop&lt;T&gt;&gt;</code></pre>

## Trait functions

### then_some

Returns `Some(t)` if the `bool` is `true`, `None` otherwise.  # Examples
```cairo
assert!(false.then_some(0) == None);
assert!(true.then_some(0) == Some(0));
```

Fully qualified path: `core::boolean::BoolTrait::then_some`

<pre><code class="language-rust">fn then_some(self: bool, t: T) -&gt; Option&lt;T&gt; nopanic</code></pre>


