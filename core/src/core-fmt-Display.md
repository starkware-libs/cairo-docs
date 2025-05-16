# Display

A trait for standard formatting, using the empty format ("{}").  # Examples
```cairo
let word: ByteArray = "123";
println!("{}", word);
```

Fully qualified path: `core::fmt::Display`

<pre><code class="language-rust">pub trait Display&lt;T&gt;</code></pre>

## Trait functions

### fmt

Fully qualified path: `core::fmt::Display::fmt`

<pre><code class="language-rust">fn fmt(self: @T, ref f: Formatter) -&gt; Result&lt;(), Error&gt;</code></pre>


