# Associated functions & Methods

Some functions are connected to a particular type. These come in two forms:
associated functions, and methods. Associated functions are functions that
are defined on a type generally, while methods are associated functions that are
called on a particular instance of a type.

```cairo,editable
{{#include ../../listings/functions/methods/src/lib.cairo}}
```

Methods must be defined within traits in Cairo, unlike Rust where they can be defined directly on types. We use the `#[generate_trait]` attribute to automatically generate the trait definition for us.

The main benefit of using methods instead of functions, in addition to providing method syntax, is for organization. We've put all the things we can do with an instance of a type in one `impl` block rather than making future users of our code search for capabilities of `Point` in various places in the library we provide.
