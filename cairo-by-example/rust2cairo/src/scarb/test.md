# Testing

As we know testing is integral to any piece of software! Cairo has
support for unit and integration testing ([see this
chapter](https://book.cairo-lang.org/ch10-00-testing-cairo-programs.html) in The Cairo Book).

Cairo has two different test runners, integrated with `scarb`:

- Starknet Foundry, which is principally aimed at Starknet development, but presents useful features for pure Cairo development as well.
- Cairo Test, which is a lightweight, pure Cairo test runner.

We'll use Starknet Foundry in the rest of these examples.

From the testing chapters linked above, we see how to write unit tests and
integration tests. Organizationally, we can place unit tests in the modules they
test and integration tests in their own `tests/` directory:

```txt
foo
├── Scarb.toml
├── src
│   └── lib.cairo
└── tests
    ├── my_test.cairo
    └── my_other_test.cairo
```

Each file in `tests` is a separate [integration test](https://book.cairo-lang.org/ch10-02-test-organization.html#integration-tests), i.e. a test that is meant to test your library as if it were being called from a dependent crate.

The [Testing][testing] chapter elaborates on the two different testing styles:
[Unit][unit_testing], and [Integration][integration_testing].

`scarb` naturally provides an easy way to run all of your tests!

```shell
$ scarb test
```

You should see output like this:

```shell
{{#include ../../listings/scarb/test/output.txt}}
```

You can also run tests whose name matches a pattern:

```shell
$ scarb test test_foo
```

```shell
{{#include ../../listings/scarb/test/output2.txt}}
```

[testing]: ../testing.md
[unit_testing]: ../testing/unit_testing.md
[integration_testing]: ../testing/integration_testing.md
[doc_testing]: ../testing/doc_testing.md
