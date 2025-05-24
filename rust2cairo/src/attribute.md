# Attributes

An attribute is metadata applied to some module, crate or item. This metadata
can be used to/for:

<!-- TODO: Link these to their respective examples -->

- [conditional compilation of code][cfg]
- disable [lints][lint] (warnings)
- enable compiler features
- mark functions as unit tests
- [attribute like macros][macros]

Attributes look like `#[outer_attribute]`. They apply to the [item][item] immediately
following it. Some examples of items are: a function, a module
declaration, a constant, a structure, an enum. Here is an example
where attribute `#[derive(Debug)]` applies to the struct
`Rectangle`:

```cairo
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}
```

Attributes can take arguments with different syntaxes:

- `#[attribute(key: "value")]`
- `#[attribute(value)]`

Attributes can have multiple values and can be separated over multiple lines, too:

```cairo,ignore
#[attribute(value, value2)]


#[attribute(value, value2, value3,
            value4, value5)]
```

[cfg]: attribute/cfg.md
[crate]: attribute/crate.md
[lint]: https://en.wikipedia.org/wiki/Lint_%28software%29
