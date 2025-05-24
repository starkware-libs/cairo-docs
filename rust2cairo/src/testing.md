# Testing

Cairo is a programming language that cares a lot about correctness and it includes support for
writing software tests within the language itself through two testing frameworks: `Cairo Test`
and `Starknet Foundry`. While `Starknet Foundry` is principally aimed at Starknet development, it
presents useful features for pure Cairo development as well, which makes it the preferred choice for
most Cairo developers. The examples presented here will use `Starknet Foundry`.

Testing comes in two styles:

- [Unit][unit] testing.
- [Integration][integration] testing.

Also, Cairo has support for specifying additional dependencies for tests:

- [Dev-dependencies][dev-dependencies]

## See Also

- [The Book][book-testing] chapter on testing

[unit]: testing/unit_testing.md
[integration]: testing/integration_testing.md
[dev-dependencies]: testing/dev_dependencies.md
[book-testing]: https://book.cairo-lang.org/ch10-00-testing-cairo-programs.html
