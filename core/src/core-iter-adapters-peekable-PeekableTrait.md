# PeekableTrait

Fully qualified path: `core::iter::adapters::peekable::PeekableTrait`

<pre><code class="language-rust">pub trait PeekableTrait&lt;I, impl IterI: Iterator&lt;I&gt;, +Copy&lt;IterI::Item&gt;, +Drop&lt;IterI::Item&gt;&gt;</code></pre>

## Trait functions

### peek

Returns a copy to the next() value without advancing the iterator.Like [`next`](`next`), if there is a value, it is wrapped in a `Some(T)`. But if the iteration is over, `None` is returned.  # ExamplesBasic usage:
```cairo
let mut iter = (1..4_u8).into_iter().peekable();

// peek() lets us see one step into the future
assert_eq!(iter.peek(), Some(1));
assert_eq!(iter.next(), Some(1));

assert_eq!(iter.next(), Some(2));

// The iterator does not advance even if we `peek` multiple times
assert_eq!(iter.peek(), Some(3));
assert_eq!(iter.peek(), Some(3));

assert_eq!(iter.next(), Some(3));

// After the iterator is finished, so is `peek()`
assert_eq!(iter.peek(), None);
assert_eq!(iter.next(), None);
```

Fully qualified path: `core::iter::adapters::peekable::PeekableTrait::peek`

<pre><code class="language-rust">fn peek(ref self: Peekable&lt;I, IterI::Item&gt;) -&gt; Option&lt;IterI::Item&gt;</code></pre>


