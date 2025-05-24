# Documentation

Use `scarb doc` to build documentation in `target/doc`, and running `mdbook
serve` in the output directory will automatically open it in your web browser.

## Doc comments

Doc comments are very useful for big projects that require documentation. When
running `scarb doc`, these are the comments that get compiled into
documentation. They are denoted by a `///`, and support [Markdown].

```cairo,editable
{{#include ../../listings/meta/doc/src/lib.cairo}}
```

For documentation, `scarb doc` is widely used by the community. It's what is used
to generate the [core library docs](https://docs.swmansion.com/scarb/corelib).

### See also:

- [The Cairo Book: Documentation][book]

[markdown]: https://en.wikipedia.org/wiki/Markdown
[book]: https://book.cairo-lang.org/ch02-04-comments.html#item-level-documentation
