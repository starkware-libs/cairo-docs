# Not

The unary logical negation operator `!`.  # ExamplesAn implementation of `Not` for `Answer`, which enables the use of `!` to invert its value.
```cairo
#[derive(Drop, PartialEq)]
enum Answer {
    Yes,
    No,
}

impl AnswerNot of Not<Answer> {
    fn not(a: Answer) -> Answer {
        match a {
            Answer::Yes => Answer::No,
            Answer::No => Answer::Yes,
        }
    }
}

assert!(!Answer::Yes == Answer::No);
assert!(!Answer::No == Answer::Yes);
```

Fully qualified path: `core::traits::Not`

<pre><code class="language-rust">pub trait Not&lt;T&gt;</code></pre>

## Trait functions

### not

Performs the unary `!` operation.  # Examples
```cairo
assert!(!true == false);
assert!(!false == true);
```

Fully qualified path: `core::traits::Not::not`

<pre><code class="language-rust">fn not(a: T) -&gt; T</code></pre>


