# FnOnce

The version of the call operator that takes a by-value receiver.Instances of `FnOnce` can be called, but might not be callable multiple times. Because of this, if the only thing known about a type is that it implements `FnOnce`, it can only be called once.`FnOnce` is implemented automatically by closures that might consume captured variables.
```cairo
# Examples

fn consume_with_relish<
    F, O, +Drop<F>, +core::ops::FnOnce<F, ()>[Output: O], +core::fmt::Display<O>, +Drop<O>,
>(
    func: F,
) {
    // `func` consumes its captured variables, so it cannot be run more
    // than once.
    println!("Consumed: {}", func());

    println!("Delicious!");
    // Attempting to invoke `func()` again will throw a `Variable was previously moved.`
    // error for `func`.
}

  let x: ByteArray = "x";
  let consume_and_return_x = || x;
  consume_with_relish(consume_and_return_x);
  // `consume_and_return_x` can no longer be invoked at this point
```

Fully qualified path: `core::ops::function::FnOnce`

<pre><code class="language-rust">pub trait FnOnce&lt;T, Args&gt;</code></pre>

## Trait functions

### call

Performs the call operation.

Fully qualified path: `core::ops::function::FnOnce::call`

<pre><code class="language-rust">fn call(self: T, args: Args) -&gt; Self::Output</code></pre>


## Trait types

### Output

The returned type after the call operator is used.

Fully qualified path: `core::ops::function::FnOnce::Output`

<pre><code class="language-rust">type Output;</code></pre>


