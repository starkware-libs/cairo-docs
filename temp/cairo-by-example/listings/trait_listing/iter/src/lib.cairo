//ANCHOR:all
#[derive(Drop)]
struct Fibonacci {
    curr: u32,
    next: u32,
}

// Implement `Iterator` for `Fibonacci`.
// The `Iterator` trait only requires a method to be defined for the `next` element,
// and an `associated type` to declare the return type of the iterator.
impl FibonacciImpl of Iterator<Fibonacci> {
    // We can refer to this type using Self::Item
    type Item = u32;

    // Here, we define the sequence using `.curr` and `.next`.
    // The return type is `Option<T>`:
    //     * When the `Iterator` is finished, `None` is returned.
    //     * Otherwise, the next value is wrapped in `Some` and returned.
    // We use Self::Item in the return type, so we can change
    // the type without having to update the function signatures.
    fn next(ref self: Fibonacci) -> Option<Self::Item> {
        let current = self.curr;

        self.curr = self.next;
        self.next = current + self.next;

        // Since there's no endpoint to a Fibonacci sequence, the `Iterator`
        // will never return `None`, and `Some` is always returned.
        Some(current)
    }
}

// Returns a Fibonacci sequence generator
fn fibonacci() -> Fibonacci {
    Fibonacci { curr: 0, next: 1 }
}

fn main() {
    // `0..3` is an `Iterator` that generates: 0, 1, and 2.
    let mut sequence = (0_u8..3).into_iter();

    println!("Four consecutive `next` calls on 0..3");
    println!("> {:?}", sequence.next());
    println!("> {:?}", sequence.next());
    println!("> {:?}", sequence.next());
    println!("> {:?}", sequence.next());

    // `for` works through an `Iterator` until it returns `None`.
    // Each `Some` value is unwrapped and bound to a variable (here, `i`).
    println!("Iterate through 0..3 using `for`");
    for i in 0_u8..3 {
        println!("> {}", i);
    }

    // The `take(n)` method reduces an `Iterator` to its first `n` terms.
    println!("The first four terms of the Fibonacci sequence are: ");
    for i in fibonacci().take(4) {
        println!("> {}", i);
    }

    // The `skip(n)` method shortens an `Iterator` by dropping its first `n` terms.
    //TODO: uncomment this once the corelib implements the `skip` method
    // println!("The next four terms of the Fibonacci sequence are: ");
    // for i in fibonacci().skip(4).take(4) {
    //     println!("> {}", i);
    // }

    let array = array![1_u32, 3, 3, 7];

    // The `iter` method produces an `Iterator` over an array/slice.
    println!("Iterate the following array {:?}", @array);
    let mut iterator = array.into_iter();
    for i in iterator {
        println!("> {}", i);
    }
}
//ANCHOR_END:all

// The corelib misses the `take` and `skip` methods for the `Iterator` trait.
// We wrote our own implementations until the corelib implements them.
//TODO: remove this once the corelib implements them

pub trait IteratorEx<T, impl I: Iterator<T>, +Destruct<T>, +Destruct<I::Item>> {
    #[inline]
    #[must_use]
    fn skip(self: T, n: usize) -> skip::Skip<T> {
        skip::skip_iterator(self, n)
    }

    #[inline]
    #[must_use]
    fn take(self: T, n: usize) -> take::Take<T> {
        take::take_iterator(self, n)
    }
}

pub trait IteratorEx2<
    T, impl I: Iterator<T>, impl J: IteratorEx<T, I>, +Destruct<T>, +Destruct<I::Item>,
> {
    #[inline]
    #[must_use]
    fn take(self: T, n: usize) -> take::Take<T> {
        take::take_iterator(self, n)
    }
}

impl IteratorExImpl<T, impl I: Iterator<T>, +Destruct<T>, +Destruct<I::Item>> of IteratorEx<T, I> {}

mod skip {
    pub struct Skip<I> {
        iter: I,
        n: usize,
    }

    pub fn skip_iterator<I>(iter: I, n: usize) -> Skip<I> {
        Skip { iter, n }
    }

    impl SkipIterator<
        I, impl TIter: Iterator<I>, +Drop<I>, +Destruct<TIter::Item>,
    > of Iterator<Skip<I>> {
        type Item = TIter::Item;
        #[inline]
        fn next(ref self: Skip<I>) -> Option<Self::Item> {
            if self.n != 0 {
                self.iter.nth(self.n - 1)
            } else {
                self.iter.next()
            }
        }
    }
}
mod take {
    /// An iterator that only iterates over the first `n` iterations of `iter`.
    ///
    /// This `struct` is created by the [`take`] method on [`Iterator`]. See its
    /// documentation for more.
    ///
    /// [`take`]: Iterator::take
    #[must_use]
    #[derive(Drop, Clone)]
    pub struct Take<I> {
        iter: I,
        n: usize,
    }

    pub fn take_iterator<I>(iter: I, n: usize) -> Take<I> {
        Take { iter, n }
    }

    impl TakeIterator<I, impl TIter: Iterator<I>, +Drop<I>> of Iterator<Take<I>> {
        type Item = TIter::Item;
        #[inline]
        fn next(ref self: Take<I>) -> Option<Self::Item> {
            if self.n != 0 {
                self.n -= 1;
                self.iter.next()
            } else {
                None
            }
        }

        #[inline]
        fn nth<+Destruct<Take<I>>, +Destruct<Self::Item>>(
            ref self: Take<I>, n: usize,
        ) -> Option<Self::Item> {
            if self.n > n {
                self.n -= n + 1;
                self.iter.nth(n)
            } else {
                if self.n != 0 {
                    let _ = self.iter.advance_by(self.n - 1);
                    self.n = 0;
                }
                None
            }
        }

        #[inline]
        fn advance_by<+Destruct<Take<I>>, +Destruct<Self::Item>>(
            ref self: Take<I>, n: usize,
        ) -> Result<(), NonZero<usize>> {
            let min = core::cmp::min(self.n, n);
            let rem = match self.iter.advance_by(min) {
                Ok(_) => 0,
                Err(rem) => rem.into(),
            };
            let advanced = min - rem;
            self.n -= advanced;
            let maybe_nz: Option<NonZero<usize>> = (n - advanced).try_into();
            match maybe_nz {
                Some(nz) => Err(nz),
                None => Ok(()),
            }
        }
    }
}
