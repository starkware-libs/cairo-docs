# Extend

Extend a collection with the contents of an iterator.Iterators produce a series of values, and collections can also be thought of as a series of values. The `Extend` trait bridges this gap, allowing you to extend a collection by including the contents of that iterator. When extending a collection with an already existing key, that entry is updated or, in the case of collections that permit multiple entries with equal keys, that entry is inserted.  # ExamplesBasic usage:
```cairo
let mut arr = array![1, 2];

arr.extend(array![3, 4, 5]);

assert_eq!(arr, array![1, 2, 3, 4, 5]);
```

Fully qualified path: `core::iter::traits::collect::Extend`

<pre><code class="language-rust">pub trait Extend&lt;T, A&gt;</code></pre>

## Trait functions

### extend

Extends a collection with the contents of an iterator.

Fully qualified path: `core::iter::traits::collect::Extend::extend`

<pre><code class="language-rust">fn extend&lt;
    I,
    impl IntoIter: IntoIterator&lt;I&gt;,
    +TypeEqual&lt;IntoIter::Iterator::Item, A&gt;,
    +Destruct&lt;IntoIter::IntoIter&gt;,
    +Destruct&lt;I&gt;,
&gt;(
    ref self: T, iter: I,
)</code></pre>


