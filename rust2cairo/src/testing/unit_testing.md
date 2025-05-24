# Unit testing

Tests are Cairo functions that verify that the non-test code is functioning in
the expected manner. The bodies of test functions typically perform some setup,
run the code we want to test, then assert whether the results are what we
expect.

Most unit tests go into a `tests` [mod][mod] with the `#[cfg(test)]` [attribute][attribute].
Test functions are marked with the `#[test]` attribute.

Tests fail when something in the test function [panics][panic]. There are some
helper [macros][macros]:

- `assert!(expression)` - panics if expression evaluates to `false`.
- `assert_eq!(left, right)` and `assert_ne!(left, right)` - testing left and right expressions for equality.
- `assert_lt!(left, right)` and `assert_gt!(left, right)` - testing left and right expressions for less than and greater than respectively.
- `assert_le!(left, right)` and `assert_ge!(left, right)` - testing left and right expressions for less than or equal to and greater than or equal to respectively.

```cairo
{{#include ../../listings/testing/unit_testing/src/lib.cairo:add}}
```

Tests can be run with `scarb test`. To run specific tests, one may specify the test name to `scarb
test` command. To run multiple tests one may specify part of a test name that matches all the tests
that should be run. Here, we run all the tests in the `add_tests` module.

```shell
{{#include ../../listings/testing/unit_testing/output_add.txt}}
```

## Testing panics

To check functions that should panic under certain circumstances, use attribute
`#[should_panic]`. This attribute accepts optional parameter `expected: ` with
the text of the panic message. If your function can panic in multiple ways, it helps
make sure your test is testing the correct panic.

```cairo
{{#include ../../listings/testing/unit_testing/src/lib.cairo:divide}}
```

Running these tests gives us:

```shell
{{#include ../../listings/testing/unit_testing/output_divide.txt}}
```

## Ignoring tests

Tests can be marked with the `#[ignore]` attribute to exclude some tests. Ignored tests can be run
with command `scarb test -- --ignored`

```cairo
{{#include ../../listings/testing/unit_testing/src/lib.cairo:ignore}}
```

```shell
{{#include ../../listings/testing/unit_testing/output_ignore.txt}}
```

[attribute]: ../attribute.md
[macros]: https://book.cairo-lang.org/ch12-05-macros.html?#macros
[mod]: ../mod.md
[panic]: ../error/panic.md
