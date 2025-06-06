# iter

Composable external iteration.
If you've found yourself with a collection of some kind, and needed to
perform an operation on the elements of said collection, you'll quickly run
into 'iterators'. Iterators are heavily used in idiomatic code, so
it's worth becoming familiar with them.
Before explaining more, let's talk about how this module is structured:
# Organization

This module is largely organized by type:
- Traits are the core portion: these traits define what kind of iterators
exist and what you can do with them. The methods of these traits are worth
putting some extra study time into.
- Functions provide some helpful ways to create some basic iterators.
- Structs are often the return types of the various methods on this
module's traits. You'll usually want to look at the method that creates
the `struct`, rather than the `struct` itself. For more detail about why,
see 'Implementing Iterator'.

That's it! Let's dig into iterators.
# Iterator

The heart and soul of this module is the [`Iterator`](./core-iter-traits-iterator-Iterator.md) trait. The core of
[`Iterator`](./core-iter-traits-iterator-Iterator.md) looks like this:
```cairo
trait Iterator {
    type Item;
    fn next(ref self) -> Option<Self::Item>;
}
```

An iterator has a method, `next`, which when called, returns an
[Option](./core-option-Option.md)<Item>. Calling `next` will return [`Some(Item)`](./core-option.md#some) as long as
there are elements, and once they've all been exhausted, will return `None` to
indicate that iteration is finished.
[`Iterator`](./core-iter-traits-iterator-Iterator.md)'s full definition includes a number of other methods as well,
but they are default methods, built on top of `next`, and so you get
them for free.
Iterators are also composable, and it's common to chain them together to do
more complex forms of processing. See the Adapters section
below for more details.
# Forms of iteration

There is currently only one common method which can create iterators from a collection:
- `into_iter()`, which iterates over `T`.
# Implementing Iterator

Creating an iterator of your own involves two steps: creating a `struct` to
hold the iterator's state, and then implementing [`Iterator`](./core-iter-traits-iterator-Iterator.md) for that `struct`.
This is why there are so many `struct`s in this module: there is one for
each iterator and iterator adapter.
Let's make an iterator named `Counter` which counts from `1` to `5`:
```cairo
// First, the struct:

/// An iterator which counts from one to five
#[derive(Drop)]
struct Counter {
    count: usize,
}

// we want our count to start at one, so let's add a new() method to help.
// This isn't strictly necessary, but is convenient. Note that we start
// `count` at zero, we'll see why in `next()`'s implementation below.
#[generate_trait]
impl CounterImpl of CounterTrait {
    fn new() -> Counter {
        Counter { count: 0 }
    }
}

// Then, we implement `Iterator` for our `Counter`:

impl CounterIter of core::iter::Iterator<Counter> {
    // we will be counting with usize
    type Item = usize;

    // next() is the only required method
    fn next(ref self: Counter) -> Option<Self::Item> {
        // Increment our count. This is why we started at zero.
        self.count += 1;

        // Check to see if we've finished counting or not.
        if self.count < 6 {
            Some(self.count)
        } else {
            None
        }
    }
}

// And now we can use it!

let mut counter = CounterTrait::new();

assert!(counter.next() == Some(1));
assert!(counter.next() == Some(2));
assert!(counter.next() == Some(3));
assert!(counter.next() == Some(4));
assert!(counter.next() == Some(5));
assert!(counter.next() == None);
```

Calling `next` this way gets repetitive. Cairo has a construct which can
call `next` on your iterator, until it reaches `None`. Let's go over that
next.
# `for` loops and `IntoIterator`

Cairo's `for` loop syntax is actually sugar for iterators. Here's a basic
example of `for`:
```cairo
let values = array![1, 2, 3, 4, 5];

for x in values {
    println!("{x}");
}
```

This will print the numbers one through five, each on their own line. But
you'll notice something here: we never called anything on our array to
produce an iterator. What gives?
There's a trait in the core library for converting something into an
iterator: [`IntoIterator`](./core-iter-traits-collect-IntoIterator.md). This trait has one method, `into_iter`,
which converts the thing implementing [`IntoIterator`](./core-iter-traits-collect-IntoIterator.md) into an iterator.
Let's take a look at that `for` loop again, and what the compiler converts
it into:
```cairo
let values = array![1, 2, 3, 4, 5];

for x in values {
    println!("{x}");
}
```

Cairo de-sugars this into:
```cairo
let values = array![1, 2, 3, 4, 5];
{
    let mut iter = IntoIterator::into_iter(values);
    let result = loop {
            let mut next = 0;
            match iter.next() {
                Some(val) => next = val,
                None => {
                    break;
                },
            };
            let x = next;
            let () = { println!("{x}"); };
        };
    result
}
```

First, we call `into_iter()` on the value. Then, we match on the iterator
that returns, calling `next` over and over until we see a `None`. At
that point, we `break` out of the loop, and we're done iterating.
There's one more subtle bit here: the core library contains an
interesting implementation of [`IntoIterator`](./core-iter-traits-collect-IntoIterator.md):
```ignore (only-for-syntax-highlight)
impl IteratorIntoIterator<T, +Iterator<T>> of IntoIterator<T>
```

In other words, all [`Iterator`](./core-iter-traits-iterator-Iterator.md)s implement [`IntoIterator`](./core-iter-traits-collect-IntoIterator.md), by just
returning themselves. This means two things:
1. If you're writing an [`Iterator`](./core-iter-traits-iterator-Iterator.md), you can use it with a `for` loop.
2. If you're creating a collection, implementing [`IntoIterator`](./core-iter-traits-collect-IntoIterator.md) for it
will allow your collection to be used with the `for` loop.
# Adapters

Functions which take an [`Iterator`](./core-iter-traits-iterator-Iterator.md) and return another [`Iterator`](./core-iter-traits-iterator-Iterator.md) are
often called 'iterator adapters', as they're a form of the 'adapter
pattern'.
Common iterators adapters include `map`, `enumerate` and `zip`.
# Laziness

Iterators (and iterator adapters) are lazy. This means that
just creating an iterator doesn't do a whole lot. Nothing really happens
until you call `next`. This is sometimes a source of confusion when
creating an iterator solely for its side effects. For example, the `map`
method calls a closure on each element it iterates over:
```cairo
let v = array![1, 2, 3, 4, 5];
let _ = v.into_iter().map(|x| println!("{x}"));
```

This will not print any values, as we only created an iterator, rather than
using it. The compiler will warn us about this kind of behavior:
```text
Unhandled `#[must_use]` type
```

Fully qualified path: [core](./core.md)::[iter](./core-iter.md)


[Modules](./core-iter-modules.md)
 ---
| | |
|:---|:---|
| [adapters](./core-iter-adapters.md) | [...](./core-iter-adapters.md) |
| [traits](./core-iter-traits.md) | [...](./core-iter-traits.md) |
## Re-exports

 - ### Traits

| | |
|:---|:---|
| [PeekableTrait](./core-iter-adapters-peekable-PeekableTrait.md) | [...](./core-iter-adapters-peekable-PeekableTrait.md) |
| [Extend](./core-iter-traits-collect-Extend.md) | Extend a collection with the contents of an iterator. Iterators produce a series of values, and collections can also be thought of as a series of values. The `Extend`[...](./core-iter-traits-collect-Extend.md) |
| [FromIterator](./core-iter-traits-collect-FromIterator.md) | Conversion from an [`Iterator`](./core-iter-traits-iterator-Iterator.md) . By implementing `FromIterator`  for a type, you define how it will be[...](./core-iter-traits-collect-FromIterator.md) |
| [IntoIterator](./core-iter-traits-collect-IntoIterator.md) | Conversion into an [`Iterator`](./core-iter-traits-iterator-Iterator.md) . By implementing `IntoIterator`  for a type, you define how it will be[...](./core-iter-traits-collect-IntoIterator.md) |
| [Iterator](./core-iter-traits-iterator-Iterator.md) | A trait for dealing with iterators. This is the main iterator trait. For more about the concept of iterators generally, please see the [module-level documentation](./core-iter.md)[...](./core-iter-traits-iterator-Iterator.md) |

<br>

