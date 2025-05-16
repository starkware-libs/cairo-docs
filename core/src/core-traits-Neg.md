# Neg

The unary negation operator `-`.  # ExamplesAn implementation of `Neg` for `Sign`, which allows the use of `-` to negate its value.
```cairo
#[derive(Copy, Drop, PartialEq)]
enum Sign {
    Negative,
    Zero,
    Positive,
}

impl SignNeg of Neg<Sign> {
    fn neg(a: Sign) -> Sign {
        match a {
            Sign::Negative => Sign::Positive,
            Sign::Zero => Sign::Zero,
            Sign::Positive => Sign::Negative,
        }
    }
}

// A negative positive is a negative
assert!(-Sign::Positive == Sign::Negative);
// A double negative is a positive
assert!(-Sign::Negative == Sign::Positive);
// Zero is its own negation
assert!(-Sign::Zero == Sign::Zero);
```

Fully qualified path: `core::traits::Neg`

<pre><code class="language-rust">pub trait Neg&lt;T&gt;</code></pre>

## Trait functions

### neg

Performs the unary `-` operation.  # Examples
```cairo
let x: i8 = 1;
assert!(-x == -1);
```

Fully qualified path: `core::traits::Neg::neg`

<pre><code class="language-rust">fn neg(a: T) -&gt; T</code></pre>


