# `cfg`

Configuration conditional checks are possible through the `cfg` attribute `#[cfg(...)]`

This attribute enables conditional compilation, removing code that is not valid for the current
configuration.

For example, a package supporting various hash functions might define features like this in the
`Scarb.toml` file:

```toml,editable
{{#include ../../listings/attribute/cfg/Scarb.toml}}
```

And then use the features in the source code:

```cairo,editable
{{#include ../../listings/attribute/cfg/src/lib.cairo}}
```

### See also:

[the Scarb reference][ref]

[ref]: https://docs.swmansion.com/scarb/docs/reference/conditional-compilation.html
