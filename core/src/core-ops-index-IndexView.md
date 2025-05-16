# IndexView

A trait for indexing operations (`container[index]`) where the input type is not modified.`container[index]` is syntactic sugar for `container.index(index)`.  # ExamplesThe following example implements `IndexView` on a `NucleotideCount` container, which can be indexed without modifying the input, enabling individual counts to be retrieved with index syntax.
```cairo
use core::ops::IndexView;

#[derive(Copy, Drop)]
enum Nucleotide {
     A,
     C,
     G,
     T,
 }

#[derive(Copy, Drop)]
struct NucleotideCount {
     a: usize,
     c: usize,
     g: usize,
     t: usize,
 }

impl NucleotideIndex of IndexView<NucleotideCount, Nucleotide> {
     type Target = usize;

     fn index(self: @NucleotideCount, index: Nucleotide) -> Self::Target {
         match index {
             Nucleotide::A => *self.a,
             Nucleotide::C => *self.c,
             Nucleotide::G => *self.g,
             Nucleotide::T => *self.t,
         }
     }
 }

let nucleotide_count = NucleotideCount {a: 14, c: 9, g: 10, t: 12};
assert!(nucleotide_count[Nucleotide::A] == 14);
assert!(nucleotide_count[Nucleotide::C] == 9);
assert!(nucleotide_count[Nucleotide::G] == 10);
assert!(nucleotide_count[Nucleotide::T] == 12);
```

Fully qualified path: `core::ops::index::IndexView`

<pre><code class="language-rust">pub trait IndexView&lt;C, I&gt;</code></pre>

## Trait functions

### index

Performs the indexing (`container[index]`) operation.  # PanicsMay panic if the index is out of bounds.

Fully qualified path: `core::ops::index::IndexView::index`

<pre><code class="language-rust">fn index(self: @C, index: I) -&gt; Self::Target</code></pre>


## Trait types

### Target

The returned type after indexing.

Fully qualified path: `core::ops::index::IndexView::Target`

<pre><code class="language-rust">type Target;</code></pre>


