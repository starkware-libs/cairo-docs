# RangeInclusiveTrait

Fully qualified path: `core::ops::range::RangeInclusiveTrait`

<pre><code class="language-rust">pub trait RangeInclusiveTrait&lt;T, +Destruct&lt;T&gt;, +PartialOrd&lt;@T&gt;&gt;</code></pre>

## Trait functions

### contains

Returns `true` if `item` is contained in the range.  # Examples
```cairo
assert!(!(3..=5).contains(@2));
assert!( (3..=5).contains(@3));
assert!( (3..=5).contains(@4));
assert!( (3..=5).contains(@5));
assert!(!(3..=5).contains(@6));

assert!( (3..=3).contains(@3));
assert!(!(3..=2).contains(@3));
```

Fully qualified path: `core::ops::range::RangeInclusiveTrait::contains`

<pre><code class="language-rust">fn contains(self: @RangeInclusive&lt;T&gt;, item: @T) -&gt; bool</code></pre>


### is_empty

Returns `true` if the range contains no items.  # Examples
```cairo
assert!(!(3_u8..=5_u8).is_empty());
assert!(!(3_u8..=3_u8).is_empty());
assert!( (3_u8..=2_u8).is_empty());
```

Fully qualified path: `core::ops::range::RangeInclusiveTrait::is_empty`

<pre><code class="language-rust">fn is_empty(self: @RangeInclusive&lt;T&gt;) -&gt; bool</code></pre>


