# Derive

The compiler is capable of providing basic implementations for some traits via the `#[derive]` [attribute][attribute]. These traits can still be manually implemented if a more complex behavior is required.

The following is a list of derivable traits:

- Comparison traits: [`PartialEq`][partial-eq]
- [`Clone`][clone], to create a copy of a value
- [`Copy`][copy], to give a type 'copy semantics' instead of 'move semantics'
- [`Drop`][drop], to enable moving out of scope
- [`Default`][default], to create an empty instance of a data type
- [`Debug`][debug], to format a value using the `{:?}` formatter
- [`Display`][display], to format a value using the `{}` formatter
- [`Hash`][hash], to compute a hash from a value
- [`Serde`][serde], to serialize and deserialize data structures
- [`Store`][store], to enable Starknet storage capabilities

```cairo,editable
{{#include ../../listings/trait_listing/derive/src/lib.cairo}}

```

### See also:

[`derive`][derive]

[attribute]: ../attribute.md
[partial-eq]: https://docs.swmansion.com/scarb/corelib/core-traits-PartialEq.html
[clone]: https://docs.swmansion.com/scarb/corelib/core-clone-Clone.html
[copy]: https://docs.swmansion.com/scarb/corelib/core-traits-Copy.html
[drop]: https://docs.swmansion.com/scarb/corelib/core-traits-Drop.html
[default]: https://docs.swmansion.com/scarb/corelib/core-traits-Default.html
[debug]: https://docs.swmansion.com/scarb/corelib/core-fmt-Debug.html
[display]: https://docs.swmansion.com/scarb/corelib/core-fmt-Display.html
[hash]: https://docs.swmansion.com/scarb/corelib/core-hash-Hash.html
[serde]: https://docs.swmansion.com/scarb/corelib/core-serde-Serde.html
[store]: https://docs.swmansion.com/scarb/corelib/core-starknet-storage_access-Store.html
[derive]: https://book.cairo-lang.org/appendix-03-derivable-traits.html
