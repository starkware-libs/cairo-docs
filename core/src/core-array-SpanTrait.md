# SpanTrait

Fully qualified path: `core::array::SpanTrait`

<pre><code class="language-rust">pub trait SpanTrait&lt;T&gt;</code></pre>

## Trait functions

### pop_front

Pops a value from the front of the span. Returns `Some(@value)` if the array is not empty, `None` otherwise.  # Examples
```cairo
let mut span = array![1, 2, 3].span();
assert!(span.pop_front() == Some(@1));
```

Fully qualified path: `core::array::SpanTrait::pop_front`

<pre><code class="language-rust">fn pop_front(ref self: Span&lt;T&gt;) -&gt; Option&lt;@T&gt;</code></pre>


### pop_back

Pops a value from the back of the span. Returns `Some(@value)` if the array is not empty, `None` otherwise.  # Examples
```cairo
let mut span = array![1, 2, 3].span();
assert!(span.pop_back() == Some(@3));
```

Fully qualified path: `core::array::SpanTrait::pop_back`

<pre><code class="language-rust">fn pop_back(ref self: Span&lt;T&gt;) -&gt; Option&lt;@T&gt;</code></pre>


### multi_pop_front

Pops multiple values from the front of the span. Returns an option containing a snapshot of a box that contains the values as a fixed-size array if the action completed successfully, 'None' otherwise.  # Examples
```cairo
let mut span = array![1, 2, 3].span();
let result = *(span.multi_pop_front::<2>().unwrap());
let unboxed_result = result.unbox();
assert!(unboxed_result == [1, 2]);
```

Fully qualified path: `core::array::SpanTrait::multi_pop_front`

<pre><code class="language-rust">fn multi_pop_front&lt;const SIZE: usize&gt;(ref self: Span&lt;T&gt;) -&gt; Option&lt;@Box&lt;[T; SIZE]&gt;&gt;</code></pre>


### multi_pop_back

Pops multiple values from the back of the span. Returns an option containing a snapshot of a box that contains the values as a fixed-size array if the action completed successfully, 'None' otherwise.  # Examples
```cairo
let mut span = array![1, 2, 3].span();
let result = *(span.multi_pop_back::<2>().unwrap());
let unboxed_result = result.unbox();
assert!(unboxed_result == [2, 3]);
```

Fully qualified path: `core::array::SpanTrait::multi_pop_back`

<pre><code class="language-rust">fn multi_pop_back&lt;const SIZE: usize&gt;(ref self: Span&lt;T&gt;) -&gt; Option&lt;@Box&lt;[T; SIZE]&gt;&gt;</code></pre>


### get

Returns an option containing a box of a snapshot of the element at the given 'index' if the span contains this index, 'None' otherwise.Element at index 0 is the front of the array.  # Examples
```cairo
let span = array![2, 3, 4];
assert!(span.get(1).unwrap().unbox() == @3);
```

Fully qualified path: `core::array::SpanTrait::get`

<pre><code class="language-rust">fn get(self: Span&lt;T&gt;, index: usize) -&gt; Option&lt;Box&lt;@T&gt;&gt;</code></pre>


### at

Returns a snapshot of the element at the given index.Element at index 0 is the front of the array.  # PanicsPanics if the index is out of bounds.  # Examples
```cairo
let span = array![2, 3, 4].span();
assert!(span.at(1) == @3);
```

Fully qualified path: `core::array::SpanTrait::at`

<pre><code class="language-rust">fn at(self: Span&lt;T&gt;, index: usize) -&gt; @T</code></pre>


### slice

Returns a span containing values from the 'start' index, with amount equal to 'length'.  # Examples
```cairo
let span = array![1, 2, 3].span();
assert!(span.slice(1, 2) == array![2, 3].span());
```

Fully qualified path: `core::array::SpanTrait::slice`

<pre><code class="language-rust">fn slice(self: Span&lt;T&gt;, start: usize, length: usize) -&gt; Span&lt;T&gt;</code></pre>


### len

Returns the length of the span as a `usize` value.  # Examples
```cairo
let span = array![2, 3, 4].span();
assert!(span.len() == 3);
```

Fully qualified path: `core::array::SpanTrait::len`

<pre><code class="language-rust">fn len(self: Span&lt;T&gt;) -&gt; usize</code></pre>


### is_empty

Returns whether the span is empty or not.  # Examples
```cairo
let span: Span<felt252> = array![].span();
assert!(span.is_empty());
let span = array![1, 2, 3].span();
assert!(!span.is_empty());
```

Fully qualified path: `core::array::SpanTrait::is_empty`

<pre><code class="language-rust">fn is_empty(self: Span&lt;T&gt;) -&gt; bool</code></pre>


