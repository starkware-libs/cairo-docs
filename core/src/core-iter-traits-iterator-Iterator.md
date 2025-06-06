# Iterator

A trait for dealing with iterators.
This is the main iterator trait. For more about the concept of iterators
generally, please see the [module-level documentation](./core-iter.md). In particular, you
may want to know how to [implement `Iterator`](./core-iter.md).

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)::[traits](./core-iter-traits.md)::[iterator](./core-iter-traits-iterator.md)::[Iterator](./core-iter-traits-iterator-Iterator.md)

<pre><code class="language-cairo">pub trait Iterator&lt;T&gt;</code></pre>

## Trait functions

### next

Advances the iterator and returns the next value.
Returns [`None`](./core-option.md#none) when iteration is finished. Individual iterator
implementations may choose to resume iteration, and so calling `next()`
again may or may not eventually start returning [`Some(Item)`](./core-option.md#some) again at some
point.
# Examples

```cairo
let mut iter = [1, 2, 3].span().into_iter();

// A call to next() returns the next value...
assert_eq!(Some(@1), iter.next());
assert_eq!(Some(@2), iter.next());
assert_eq!(Some(@3), iter.next());

// ... and then None once it's over.
assert_eq!(None, iter.next());

// More calls may or may not return `None`. Here, they always will.
assert_eq!(None, iter.next());
assert_eq!(None, iter.next());
```

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)::[traits](./core-iter-traits.md)::[iterator](./core-iter-traits-iterator.md)::[Iterator](./core-iter-traits-iterator-Iterator.md)::[next](./core-iter-traits-iterator-Iterator.md#next)

<pre><code class="language-cairo">fn next&lt;T, T&gt;(ref self: T) -&gt; <a href="core-option-Option.html">Option&lt;Iterator&lt;T&gt;Item&gt;</a></code></pre>


### count

Consumes the iterator, counting the number of iterations and returning it.
This method will call `next` repeatedly until [`None`](./core-option.md#none) is encountered,
returning the number of times it saw [`Some`](./core-option.md#some). Note that `next` has to be
called at least once even if the iterator does not have any elements.
# Overflow Behavior

The method does no guarding against overflows, so counting elements of
an iterator with more than [`Bounded::<usize>::MAX`](./core-num-traits-bounded-Bounded.md) elements either produces the
wrong result or panics.
# Panics

This function might panic if the iterator has more than [`Bounded::<usize>::MAX`](./core-num-traits-bounded-Bounded.md)
elements.
# Examples

```cairo
let mut a = array![1, 2, 3].into_iter();
assert_eq!(a.count(), 3);

let mut a = array![1, 2, 3, 4, 5].into_iter();
assert_eq!(a.count(), 5);
```

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)::[traits](./core-iter-traits.md)::[iterator](./core-iter-traits-iterator.md)::[Iterator](./core-iter-traits-iterator-Iterator.md)::[count](./core-iter-traits-iterator-Iterator.md#count)

<pre><code class="language-cairo">fn count&lt;T, T, +Destruct&lt;T&gt;, +Destruct&lt;Self::Item&gt;&gt;(self: T) -&gt; <a href="core-integer-u32.html">u32</a></code></pre>


### last

Consumes the iterator, returning the last element.
This method will evaluate the iterator until it returns [`None`](./core-option.md#none). While
doing so, it keeps track of the current element. After [`None`](./core-option.md#none) is
returned, `last()` will then return the last element it saw.
# Examples

```cairo
let mut a = array![1, 2, 3].into_iter();
assert_eq!(a.last(), Option::Some(3));

let mut a = array![].into_iter();
assert_eq!(a.last(), Option::None);
```

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)::[traits](./core-iter-traits.md)::[iterator](./core-iter-traits-iterator.md)::[Iterator](./core-iter-traits-iterator-Iterator.md)::[last](./core-iter-traits-iterator-Iterator.md#last)

<pre><code class="language-cairo">fn last&lt;T, T, +Destruct&lt;T&gt;, +Destruct&lt;Self::Item&gt;&gt;(self: T) -&gt; <a href="core-option-Option.html">Option&lt;Iterator&lt;T&gt;Item&gt;</a></code></pre>


### advance_by

Advances the iterator by `n` elements.
This method will eagerly skip `n` elements by calling `next` up to `n`
times until [`None`](./core-option.md#none) is encountered.
`advance_by(n)` will return `Ok(())` if the iterator successfully advances by
`n` elements, or a `Err(NonZero<usize>)` with value `k` if [`None`](./core-option.md#none) is encountered,
where `k` is remaining number of steps that could not be advanced because the iterator ran
out.
If `self` is empty and `n` is non-zero, then this returns `Err(n)`.
Otherwise, `k` is always less than `n`.
# Examples

```cairo
let mut iter = array![1_u8, 2, 3, 4].into_iter();

assert_eq!(iter.advance_by(2), Ok(()));
assert_eq!(iter.next(), Some(3));
assert_eq!(iter.advance_by(0), Ok(()));
assert_eq!(iter.advance_by(100), Err(99));
```

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)::[traits](./core-iter-traits.md)::[iterator](./core-iter-traits-iterator.md)::[Iterator](./core-iter-traits-iterator-Iterator.md)::[advance_by](./core-iter-traits-iterator-Iterator.md#advance_by)

<pre><code class="language-cairo">fn advance_by&lt;T, T, +Destruct&lt;T&gt;, +Destruct&lt;Self::Item&gt;&gt;(
    ref self: T, n: <a href="core-integer-u32.html">u32</a>,
) -&gt; <a href="core-result-Result.html">Result&lt;(), NonZero&lt;u32&gt;&gt;</a></code></pre>


### nth

Returns the `n`th element of the iterator.
Like most indexing operations, the count starts from zero, so `nth(0)`
returns the first value, `nth(1)` the second, and so on.
Note that all preceding elements, as well as the returned element, will be
consumed from the iterator. That means that the preceding elements will be
discarded, and also that calling `nth(0)` multiple times on the same iterator
will return different elements.
`nth()` will return [`None`](./core-option.md#none) if `n` is greater than or equal to the length of the
iterator.
# Examples

Basic usage:
```cairo
let mut iter = array![1, 2, 3].into_iter();
assert_eq!(iter.nth(1), Some(2));
```

Calling `nth()` multiple times doesn't rewind the iterator:
```cairo
let mut iter = array![1, 2, 3].into_iter();

assert_eq!(iter.nth(1), Some(2));
assert_eq!(iter.nth(1), None);
```

Returning `None` if there are less than `n + 1` elements:
```cairo
let mut iter = array![1, 2, 3].into_iter();
assert_eq!(iter.nth(10), None);
```

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)::[traits](./core-iter-traits.md)::[iterator](./core-iter-traits-iterator.md)::[Iterator](./core-iter-traits-iterator-Iterator.md)::[nth](./core-iter-traits-iterator-Iterator.md#nth)

<pre><code class="language-cairo">fn nth&lt;T, T, +Destruct&lt;T&gt;, +Destruct&lt;Self::Item&gt;&gt;(ref self: T, n: <a href="core-integer-u32.html">u32</a>) -&gt; <a href="core-option-Option.html">Option&lt;Iterator&lt;T&gt;Item&gt;</a></code></pre>


### map

Takes a closure and creates an iterator which calls that closure on each
element.
`map()` transforms one iterator into another, by means of its argument:
something that implements `FnOnce`. It produces a new iterator which
calls this closure on each element of the original iterator.
If you are good at thinking in types, you can think of `map()` like this:
If you have an iterator that gives you elements of some type `A`, and
you want an iterator of some other type `B`, you can use `map()`,
passing a closure that takes an `A` and returns a `B`.
`map()` is conceptually similar to a `for` loop. However, as `map()` is
lazy, it is best used when you're already working with other iterators.
If you're doing some sort of looping for a side effect, it's considered
more idiomatic to use `for` than `map()`.
# Examples

Basic usage:
```cairo
let mut iter = array![1, 2, 3].into_iter().map(|x| 2 * x);

assert!(iter.next() == Some(2));
assert!(iter.next() == Some(4));
assert!(iter.next() == Some(6));
assert!(iter.next() == None);
```

If you're doing some sort of side effect, prefer `for` to `map()`:
```cairo
// don't do this:
let _ = (0..5_usize).into_iter().map(|x| println!("{x}"));

// it won't even execute, as it is lazy. Cairo will warn you about this if not specifically
ignored, as is done here.

// Instead, use for:
for x in 0..5_usize {
    println!("{x}");
}
```

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)::[traits](./core-iter-traits.md)::[iterator](./core-iter-traits-iterator.md)::[Iterator](./core-iter-traits-iterator-Iterator.md)::[map](./core-iter-traits-iterator-Iterator.md#map)

<pre><code class="language-cairo">fn map&lt;T, T, B, F, +core::ops::Fn&lt;F, (Self::Item,)&gt;[Output: B], +Drop&lt;T&gt;, +Drop&lt;F&gt;&gt;(
    self: T, f: F,
) -&gt; <a href="core-iter-adapters-map-Map.html">Map&lt;T, F&gt;</a></code></pre>


### enumerate

Creates an iterator which gives the current iteration count as well as
the next value.
The iterator returned yields pairs `(i, val)`, where `i` is the
current index of iteration and `val` is the value returned by the
iterator.
`enumerate()` keeps its count as a [`usize`](./core-usize.md).
# Overflow Behavior

The method does no guarding against overflows, so enumerating more than
`Bounded::<usize>::MAX` elements will always panic.
# Panics

Will panic if the to-be-returned index overflows a `usize`.
# Examples

```cairo
let mut iter = array!['a', 'b', 'c'].into_iter().enumerate();

assert_eq!(iter.next(), Some((0, 'a')));
assert_eq!(iter.next(), Some((1, 'b')));
assert_eq!(iter.next(), Some((2, 'c')));
assert_eq!(iter.next(), None);
```

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)::[traits](./core-iter-traits.md)::[iterator](./core-iter-traits-iterator.md)::[Iterator](./core-iter-traits-iterator-Iterator.md)::[enumerate](./core-iter-traits-iterator-Iterator.md#enumerate)

<pre><code class="language-cairo">fn enumerate&lt;T, T&gt;(self: T) -&gt; <a href="core-iter-adapters-enumerate-Enumerate.html">Enumerate&lt;T&gt;</a></code></pre>


### fold

Folds every element into an accumulator by applying an operation,
returning the final result.
`fold()` takes two arguments: an initial value, and a closure with two
arguments: an 'accumulator', and an element. The closure returns the value that
the accumulator should have for the next iteration.
The initial value is the value the accumulator will have on the first
call.
After applying this closure to every element of the iterator, `fold()`
returns the accumulator.
Folding is useful whenever you have a collection of something, and want
to produce a single value from it.
Note: `fold()`, and similar methods that traverse the entire iterator,
might not terminate for infinite iterators, even on traits for which a
result is determinable in finite time.
Note: `fold()` combines elements in a left-associative fashion. For associative
operators like `+`, the order the elements are combined in is not important, but for
non-associative operators like `-` the order will affect the final result.
# Note to Implementers

Several of the other (forward) methods have default implementations in
terms of this one, so try to implement this explicitly if it can
do something better than the default `for` loop implementation.
In particular, try to have this call `fold()` on the internal parts
from which this iterator is composed.
# Examples

Basic usage:
```cairo
let mut iter = array![1, 2, 3].into_iter();

// the sum of all of the elements of the array
let sum = iter.fold(0, |acc, x| acc + x);

assert_eq!(sum, 6);
```

Let's walk through each step of the iteration here:

|element|acc|x|result|
|---|---|---|---|
||0|||
|1|0|1|1|
|2|1|2|3|
|3|3|3|6|

And so, our final result, `6`.
It's common for people who haven't used iterators a lot to
use a `for` loop with a list of things to build up a result. Those
can be turned into `fold()`s:
```cairo
let mut numbers = array![1, 2, 3, 4, 5].span();

let mut result = 0;

// for loop:
for i in numbers{
    result = result + (*i);
};

// fold:
let mut numbers_iter = numbers.into_iter();
let result2 = numbers_iter.fold(0, |acc, x| acc + (*x));

// they're the same
assert_eq!(result, result2);
```

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)::[traits](./core-iter-traits.md)::[iterator](./core-iter-traits-iterator.md)::[Iterator](./core-iter-traits-iterator-Iterator.md)::[fold](./core-iter-traits-iterator-Iterator.md#fold)

<pre><code class="language-cairo">fn fold&lt;
    T,
    T,
    B,
    F,
    +core::ops::Fn&lt;F, (B, Self::Item)&gt;[Output: B],
    +Destruct&lt;T&gt;,
    +Destruct&lt;F&gt;,
    +Destruct&lt;B&gt;,
&gt;(
    ref self: T, init: B, f: F,
) -&gt; B</code></pre>


### any

Tests if any element of the iterator matches a predicate.
`any()` takes a closure that returns `true` or `false`. It applies this closure to each
element of the iterator, and if any of them return `true`, then so does `any()`. If they all
return `false`, it returns `false`.
`any()` is short-circuiting; in other words, it will stop processing as soon as it finds a
`true`, given that no matter what else happens, the result will also be `true`.
An empty iterator returns `false`.
# Examples

Basic usage:
```cairo
assert!(array![1, 2, 3].into_iter().any(|x| x == 2));

assert!(!array![1, 2, 3].into_iter().any(|x| x > 5));
```

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)::[traits](./core-iter-traits.md)::[iterator](./core-iter-traits-iterator.md)::[Iterator](./core-iter-traits-iterator-Iterator.md)::[any](./core-iter-traits-iterator-Iterator.md#any)

<pre><code class="language-cairo">fn any&lt;
    T,
    T,
    P,
    +core::ops::Fn&lt;P, (Self::Item,)&gt;[Output: bool],
    +Destruct&lt;P&gt;,
    +Destruct&lt;T&gt;,
    +Destruct&lt;Self::Item&gt;,
&gt;(
    ref self: T, predicate: P,
) -&gt; <a href="core-bool.html">bool</a></code></pre>


### all

Tests if every element of the iterator matches a predicate.
`all()` takes a closure that returns `true` or `false`. It applies this closure to each
element of the iterator, and if all of them return `true`, then so does `all()`. If any
of them return `false`, it returns `false`.
`all()` is short-circuiting; in other words, it will stop processing as soon as it finds a
`false`, given that no matter what else happens, the result will also be `false`.
An empty iterator returns `true`.
# Examples

Basic usage:
```cairo
assert!(array![1, 2, 3].into_iter().all(|x| x > 0));

assert!(!array![1, 2, 3].into_iter().all(|x| x > 2));
```

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)::[traits](./core-iter-traits.md)::[iterator](./core-iter-traits-iterator.md)::[Iterator](./core-iter-traits-iterator-Iterator.md)::[all](./core-iter-traits-iterator-Iterator.md#all)

<pre><code class="language-cairo">fn all&lt;
    T,
    T,
    P,
    +core::ops::Fn&lt;P, (Self::Item,)&gt;[Output: bool],
    +Destruct&lt;P&gt;,
    +Destruct&lt;T&gt;,
    +Destruct&lt;Self::Item&gt;,
&gt;(
    ref self: T, predicate: P,
) -&gt; <a href="core-bool.html">bool</a></code></pre>


### find

Searches for an element of an iterator that satisfies a predicate.
`find()` takes a closure that returns `true` or `false`. It applies
this closure to each element of the iterator as a snapshot, and if
any of them return `true`, then `find()` returns `Some(element)`.
If they all return `false`, it returns [`None`](./core-option.md#none).
`find()` is short-circuiting; in other words, it will stop processing
as soon as the closure returns `true`.
# Examples

Basic usage:
```cairo
let mut iter = array![1, 2, 3].into_iter();

assert_eq!(iter.find(|x| *x == 2), Option::Some(2));

assert_eq!(iter.find(|x| *x == 5), Option::None);
```

Stopping at the first `true`:
```cairo
let mut iter = array![1, 2, 3].into_iter();

assert_eq!(iter.find(|x| *x == 2), Option::Some(2));

// we can still use `iter`, as there are more elements.
assert_eq!(iter.next(), Option::Some(3));
```

Note that `iter.find(f)` is equivalent to `iter.filter(f).next()`.

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)::[traits](./core-iter-traits.md)::[iterator](./core-iter-traits-iterator.md)::[Iterator](./core-iter-traits-iterator-Iterator.md)::[find](./core-iter-traits-iterator-Iterator.md#find)

<pre><code class="language-cairo">fn find&lt;T, T, P, +core::ops::Fn&lt;P, (@Self::Item,)&gt;[Output: bool], +Destruct&lt;P&gt;, +Destruct&lt;T&gt;, +Destruct&lt;Self::Item&gt;&gt;(ref self: T, predicate: P) -&gt; <a href="core-option-Option.html">Option&lt;Iterator&lt;T&gt;Item&gt;</a></code></pre>


### filter

Creates an iterator which uses a closure to determine if an element
should be yielded. The closure takes each element as a snapshot.
Given an element the closure must return `true` or `false`. The returned
iterator will yield only the elements for which the closure returns
`true`.
# Examples

Basic usage:
```cairo
let a = array![0_u32, 1, 2];

let mut iter = a.into_iter().filter(|x| *x > 0);

assert_eq!(iter.next(), Option::Some(1));
assert_eq!(iter.next(), Option::Some(2));
assert_eq!(iter.next(), Option::None);
```

Note that `iter.filter(f).next()` is equivalent to `iter.find(f)`.

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)::[traits](./core-iter-traits.md)::[iterator](./core-iter-traits-iterator.md)::[Iterator](./core-iter-traits-iterator-Iterator.md)::[filter](./core-iter-traits-iterator-Iterator.md#filter)

<pre><code class="language-cairo">fn filter&lt;
    T,
    T,
    P,
    +core::ops::Fn&lt;P, (@Self::Item,)&gt;[Output: bool],
    +Destruct&lt;P&gt;,
    +Destruct&lt;T&gt;,
    +Destruct&lt;Self::Item&gt;,
&gt;(
    self: T, predicate: P,
) -&gt; <a href="core-iter-adapters-filter-Filter.html">Filter&lt;T, P&gt;</a></code></pre>


### zip

'Zips up' two iterators into a single iterator of pairs.
`zip()` returns a new iterator that will iterate over two other
iterators, returning a tuple where the first element comes from the
first iterator, and the second element comes from the second iterator.
In other words, it zips two iterators together, into a single one.
If either iterator returns [`None`](./core-option.md#none), `next` from the zipped iterator
will return [`None`](./core-option.md#none).
If the zipped iterator has no more elements to return then each further attempt to advance
it will first try to advance the first iterator at most one time and if it still yielded an
item try to advance the second iterator at most one time.
# Examples

Basic usage:
```cairo
let mut iter = array![1, 2, 3].into_iter().zip(array![4, 5, 6].into_iter());

assert_eq!(iter.next(), Some((1, 4)));
assert_eq!(iter.next(), Some((2, 5)));
assert_eq!(iter.next(), Some((3, 6)));
assert_eq!(iter.next(), None);
```

Since the argument to `zip()` uses [`IntoIterator`](./core-iter-traits-collect-IntoIterator.md), we can pass
anything that can be converted into an [`Iterator`](./core-iter-traits-iterator-Iterator.md), not just an
[`Iterator`](./core-iter-traits-iterator-Iterator.md) itself. For example:
```cairo
let mut iter = array![1, 2, 3].into_iter().zip(array![4, 5, 6]);

assert_eq!(iter.next(), Some((1, 4)));
assert_eq!(iter.next(), Some((2, 5)));
assert_eq!(iter.next(), Some((3, 6)));
assert_eq!(iter.next(), None);
```

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)::[traits](./core-iter-traits.md)::[iterator](./core-iter-traits-iterator.md)::[Iterator](./core-iter-traits-iterator-Iterator.md)::[zip](./core-iter-traits-iterator-Iterator.md#zip)

<pre><code class="language-cairo">fn zip&lt;T, T, U, impl UIntoIter: IntoIterator&lt;U&gt;, +Destruct&lt;T&gt;&gt;(
    self: T, other: U,
) -&gt; <a href="core-iter-adapters-zip-Zip.html">Zip&lt;T, IntoIter&gt;</a></code></pre>


### collect

Transforms an iterator into a collection.
`collect()` can take anything iterable, and turn it into a relevant
collection. This is one of the more powerful methods in the core
library, used in a variety of contexts.
The most basic pattern in which `collect()` is used is to turn one
collection into another. You take a collection, call `iter` on it,
do a bunch of transformations, and then `collect()` at the end.
`collect()` can also create instances of types that are not typical
collections.
Because `collect()` is so general, it can cause problems with type
inference. As such, `collect()` is one of the few times you'll see
the syntax affectionately known as the 'turbofish': `::<>`. This
helps the inference algorithm understand specifically which collection
you're trying to collect into.
# Examples

Basic usage:
```cairo
let doubled: Array<u32> = array![1, 2, 3].into_iter().map(|x| x * 2).collect();

assert_eq!(array![2, 4, 6], doubled);
```

Note that we needed the `: Array<u32>` on the left-hand side.
Using the 'turbofish' instead of annotating `doubled`:
```cairo
let doubled = array![1, 2, 3].into_iter().map(|x| x * 2).collect::<Array<u32>>();

assert_eq!(array![2, 4, 6], doubled);
```

Because `collect()` only cares about what you're collecting into, you can
still use a partial type hint, `_`, with the turbofish:
```cairo
let doubled = array![1, 2, 3].into_iter().map(|x| x * 2).collect::<Array<_>>();

assert_eq!(array![2, 4, 6], doubled);
```

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)::[traits](./core-iter-traits.md)::[iterator](./core-iter-traits-iterator.md)::[Iterator](./core-iter-traits-iterator-Iterator.md)::[collect](./core-iter-traits-iterator-Iterator.md#collect)

<pre><code class="language-cairo">fn collect&lt;
    T,
    T,
    B,
    impl IntoIter: IntoIterator&lt;T&gt;,
    impl ItemEqual: TypeEqual&lt;
        IntoIter::Iterator::Item, core::iter::traits::iterator::Iterator::&lt;T&gt;::Item,
    &gt;,
    +Destruct&lt;IntoIter::IntoIter&gt;,
    +FromIterator&lt;B, Self::Item&gt;,
    +Destruct&lt;T&gt;,
&gt;(
    self: T,
) -&gt; B</code></pre>


### peekable

Creates an iterator which can use the `peek` method to look at the next element of the
iterator. See its documentation for more information.
Note that the underlying iterator is still advanced when `peek` is called for the first
time: In order to retrieve the next element, `next` is called on the underlying iterator,
hence any side effects (i.e. anything other than fetching the next value) of the `next`
method will occur.
# Examples

Basic usage:
```cairo
let mut iter = (1..4_u8).into_iter().peekable();

// peek() lets us see one step into the future
assert_eq!(iter.peek(), Option::Some(1));
assert_eq!(iter.next(), Option::Some(1));

assert_eq!(iter.next(), Option::Some(2));

// we can peek() multiple times, the iterator won't advance
assert_eq!(iter.peek(), Option::Some(3));
assert_eq!(iter.peek(), Option::Some(3));

assert_eq!(iter.next(), Option::Some(3));

// after the iterator is finished, so is peek()
assert_eq!(iter.peek(), Option::None);
assert_eq!(iter.next(), Option::None);
```

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)::[traits](./core-iter-traits.md)::[iterator](./core-iter-traits-iterator.md)::[Iterator](./core-iter-traits-iterator-Iterator.md)::[peekable](./core-iter-traits-iterator-Iterator.md#peekable)

<pre><code class="language-cairo">fn peekable&lt;T, T&gt;(self: T) -&gt; <a href="core-iter-adapters-peekable-Peekable.html">Peekable&lt;T, Iterator&lt;T&gt;Item&gt;</a></code></pre>


### take

Creates an iterator that yields the first `n` elements, or fewer
if the underlying iterator ends sooner.
`take(n)` yields elements until `n` elements are yielded or the end of
the iterator is reached (whichever happens first).
The returned iterator is a prefix of length `n` if the original iterator
contains at least `n` elements, otherwise it contains all of the
(fewer than `n`) elements of the original iterator.
# Examples

Basic usage:
```cairo
let mut iter = array![1, 2, 3].into_iter().take(2);

assert_eq!(iter.next(), Some(1));
assert_eq!(iter.next(), Some(2));
assert_eq!(iter.next(), None);
```

If less than `n` elements are available,
`take` will limit itself to the size of the underlying iterator:
```cairo
let mut iter = array![1, 2].into_iter().take(5);
assert_eq!(iter.next(), Some(1));
assert_eq!(iter.next(), Some(2));
assert_eq!(iter.next(), None);
```

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)::[traits](./core-iter-traits.md)::[iterator](./core-iter-traits-iterator.md)::[Iterator](./core-iter-traits-iterator-Iterator.md)::[take](./core-iter-traits-iterator-Iterator.md#take)

<pre><code class="language-cairo">fn take&lt;T, T&gt;(self: T, n: <a href="core-integer-u32.html">u32</a>) -&gt; <a href="core-iter-adapters-take-Take.html">Take&lt;T&gt;</a></code></pre>


### sum

Sums the elements of an iterator.
Takes each element, adds them together, and returns the result.
An empty iterator returns the zero value of the type.
`sum()` can be used to sum any type implementing [`Sum`][`core::iter::Sum`],
including [`Option`][`Option::sum`] and [`Result`][`Result::sum`].
# Panics

When calling `sum()` and a primitive integer type is being returned, this
method will panic if the computation overflows.
# Examples

```cairo
let mut iter = array![1, 2, 3].into_iter();
let sum: usize = iter.sum();

assert_eq!(sum, 6);
```

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)::[traits](./core-iter-traits.md)::[iterator](./core-iter-traits-iterator.md)::[Iterator](./core-iter-traits-iterator-Iterator.md)::[sum](./core-iter-traits-iterator-Iterator.md#sum)

<pre><code class="language-cairo">fn sum&lt;T, T, +Destruct&lt;T&gt;, +Destruct&lt;Self::Item&gt;, +Sum&lt;Self::Item&gt;&gt;(self: T) -&gt; <a href="core-iter-traits-iterator-Iterator.html">Iterator&lt;T&gt;Item</a></code></pre>


### product

Iterates over the entire iterator, multiplying all the elements
An empty iterator returns the one value of the type.
# Panics

When calling `product()` and a primitive integer type is being returned, this
method will panic if the computation overflows.
# Examples

```cairo
fn factorial(n: u32) -> u32 {
    (1..=n).into_iter().product()
}
assert_eq!(factorial(0), 1);
assert_eq!(factorial(1), 1);
assert_eq!(factorial(5), 120);
```

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)::[traits](./core-iter-traits.md)::[iterator](./core-iter-traits-iterator.md)::[Iterator](./core-iter-traits-iterator-Iterator.md)::[product](./core-iter-traits-iterator-Iterator.md#product)

<pre><code class="language-cairo">fn product&lt;T, T, +Destruct&lt;T&gt;, +Destruct&lt;Self::Item&gt;, +Product&lt;Self::Item&gt;&gt;(self: T) -&gt; <a href="core-iter-traits-iterator-Iterator.html">Iterator&lt;T&gt;Item</a></code></pre>


### chain

Takes two iterators and creates a new iterator over both in sequence.
`chain()` will return a new iterator which will first iterate over
values from the first iterator and then over values from the second
iterator.
In other words, it links two iterators together, in a chain. 🔗
Arguments do not have to be of the same type as long as the underlying iterated
over items are.
# Examples

Basic usage:
```cairo
use core::ops::Range;

let a: Array<u8> = array![7, 8, 9];
let b: Range<u8> = 0..5;

let mut iter = a.into_iter().chain(b.into_iter());

assert_eq!(iter.next(), Option::Some(7));
assert_eq!(iter.next(), Option::Some(8));
assert_eq!(iter.next(), Option::Some(9));
assert_eq!(iter.next(), Option::Some(0));
assert_eq!(iter.next(), Option::Some(1));
assert_eq!(iter.next(), Option::Some(2));
assert_eq!(iter.next(), Option::Some(3));
assert_eq!(iter.next(), Option::Some(4));
assert_eq!(iter.next(), Option::None);
```

Since the argument to `chain()` uses [`IntoIterator`](./core-iter-traits-collect-IntoIterator.md), we can pass
anything that can be converted into an [`Iterator`](./core-iter-traits-iterator-Iterator.md), not just an
[`Iterator`](./core-iter-traits-iterator-Iterator.md) itself. For example, arrays implement
[`IntoIterator`](./core-iter-traits-collect-IntoIterator.md), and so can be passed to `chain()` directly:
```cairo
let a = array![1, 2, 3];
let b = array![4, 5, 6];

let mut iter = a.into_iter().chain(b);

assert_eq!(iter.next(), Option::Some(1));
assert_eq!(iter.next(), Option::Some(2));
assert_eq!(iter.next(), Option::Some(3));
assert_eq!(iter.next(), Option::Some(4));
assert_eq!(iter.next(), Option::Some(5));
assert_eq!(iter.next(), Option::Some(6));
assert_eq!(iter.next(), Option::None);
```

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)::[traits](./core-iter-traits.md)::[iterator](./core-iter-traits-iterator.md)::[Iterator](./core-iter-traits-iterator-Iterator.md)::[chain](./core-iter-traits-iterator-Iterator.md#chain)

<pre><code class="language-cairo">fn chain&lt;
    T,
    T,
    U,
    impl IntoIterU: IntoIterator&lt;U&gt;,
    +TypeEqual&lt;Self::Item, IntoIterU::Iterator::Item&gt;,
    +Destruct&lt;T&gt;,
&gt;(
    self: T, other: U,
) -&gt; <a href="core-iter-adapters-chain-Chain.html">Chain&lt;T, IntoIter&gt;</a></code></pre>


## Trait types

### Item

The type of the elements being iterated over.

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)::[traits](./core-iter-traits.md)::[iterator](./core-iter-traits-iterator.md)::[Iterator](./core-iter-traits-iterator-Iterator.md)::[Item](./core-iter-traits-iterator-Iterator.md#item)

<pre><code class="language-cairo">type Item;</code></pre>


