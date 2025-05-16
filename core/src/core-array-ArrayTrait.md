# ArrayTrait

Fully qualified path: `core::array::ArrayTrait`

<pre><code class="language-rust">pub trait ArrayTrait&lt;T&gt;</code></pre>

## Trait functions

### new

Constructs a new, empty `Array<T>`.  # Examples
```cairo
let arr: Array<u32> = ArrayTrait::new();

let arr = ArrayTrait::<u128>::new();
```
It is also possible to use the `array!` macro to create a new array.
```cairo
let arr: Array<bool> = array![];
```

Fully qualified path: `core::array::ArrayTrait::new`

<pre><code class="language-rust">fn new() -&gt; Array&lt;T&gt; nopanic</code></pre>


### append

Adds a value of type `T` to the end of the array.  # Examples
```cairo
let mut arr: Array<u8> = array![1, 2];
arr.append(3);
assert!(arr == array![1, 2, 3]);
```

Fully qualified path: `core::array::ArrayTrait::append`

<pre><code class="language-rust">fn append(ref self: Array&lt;T&gt;, value: T) nopanic</code></pre>


### append_span

Adds a span to the end of the array.  # Examples
```cairo
let mut arr: Array<u8> = array![];
arr.append_span(array![1, 2, 3].span());
assert!(arr == array![1, 2, 3]);
```

Fully qualified path: `core::array::ArrayTrait::append_span`

<pre><code class="language-rust">fn append_span&lt;+Clone&lt;T&gt;, +Drop&lt;T&gt;&gt;(ref self: Array&lt;T&gt;, span: Span&lt;T&gt;)</code></pre>


### pop_front

Pops a value from the front of the array. Returns `Some(value)` if the array is not empty, `None` otherwise.  # Examples
```cairo
let mut arr = array![2, 3, 4];
assert!(arr.pop_front() == Some(2));
assert!(arr.pop_front() == Some(3));
assert!(arr.pop_front() == Some(4));
assert!(arr.pop_front().is_none());
```

Fully qualified path: `core::array::ArrayTrait::pop_front`

<pre><code class="language-rust">fn pop_front(ref self: Array&lt;T&gt;) -&gt; Option&lt;T&gt; nopanic</code></pre>


### pop_front_consume

Pops a value from the front of the array. Returns an option containing the remaining array and the value removed if the array is not empty, otherwise `None` and drops the array.  # Examples
```cairo
let arr = array![2, 3, 4];
assert!(arr.pop_front_consume() == Some((array![3, 4], 2)));

let arr: Array<u8> = array![];
assert!(arr.pop_front_consume().is_none());
```

Fully qualified path: `core::array::ArrayTrait::pop_front_consume`

<pre><code class="language-rust">fn pop_front_consume(self: Array&lt;T&gt;) -&gt; Option&lt;(Array&lt;T&gt;, T)&gt; nopanic</code></pre>


### get

Returns an option containing a box of a snapshot of the element at the given 'index' if the array contains this index, 'None' otherwise.Element at index 0 is the front of the array.  # Examples
```cairo
let arr = array![2, 3, 4];
assert!(arr.get(1).unwrap().unbox() == @3);
```

Fully qualified path: `core::array::ArrayTrait::get`

<pre><code class="language-rust">fn get(self: @Array&lt;T&gt;, index: usize) -&gt; Option&lt;Box&lt;@T&gt;&gt;</code></pre>


### at

Returns a snapshot of the element at the given index.Element at index 0 is the front of the array.  # PanicsPanics if the index is out of bounds.  # Examples
```cairo
let mut arr: Array<usize> = array![3,4,5,6];
assert!(arr.at(1) == @4);
```

Fully qualified path: `core::array::ArrayTrait::at`

<pre><code class="language-rust">fn at(self: @Array&lt;T&gt;, index: usize) -&gt; @T</code></pre>


### len

Returns the length of the array as a `usize` value.  # Examples
```cairo
let arr = array![2, 3, 4];
assert!(arr.len() == 3);
```

Fully qualified path: `core::array::ArrayTrait::len`

<pre><code class="language-rust">fn len(self: @Array&lt;T&gt;) -&gt; usize</code></pre>


### is_empty

Returns whether the array is empty or not.  # Examples
```cairo
let mut arr = array![];
assert!(arr.is_empty());
arr.append(1);
assert!(!arr.is_empty());
```

Fully qualified path: `core::array::ArrayTrait::is_empty`

<pre><code class="language-rust">fn is_empty(self: @Array&lt;T&gt;) -&gt; bool</code></pre>


### span

Returns a span of the array.  # Examples
```cairo
let arr: Array<u8> = array![1, 2, 3];
let span: Span<u8> = arr.span();
```

Fully qualified path: `core::array::ArrayTrait::span`

<pre><code class="language-rust">fn span(snapshot: @Array&lt;T&gt;) -&gt; Span&lt;T&gt;</code></pre>


