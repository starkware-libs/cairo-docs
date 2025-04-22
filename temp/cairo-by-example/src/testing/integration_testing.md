# Integration testing

[Unit tests][unit] are testing one module in isolation at a time: they're small
and can test private code. Integration tests are external to your crate and use
only its public interface in the same way any other code would. Their purpose is
to test that many parts of your library work correctly together.

Scarb looks for integration tests in `tests` directory next to `src`.

File `src/lib.cairo`:

```cairo,noplayground
{{#include ../../listings/testing/integration_testing/src/lib.cairo}}
```

File with test: `tests/integration_test.cairo`:

```cairo,noplayground
{{#include ../../listings/testing/integration_testing/tests/integration_test.cairo}}
```

Running tests with `scarb test` command:

```shell
{{#include ../../listings/testing/integration_testing/output.txt}}
```

If the `tests` directory does not contain a `lib.cairo` file, each Cairo source file in the `tests`
directory is compiled as a separate crate. In order to share some code between integration tests we
can define a `lib.cairo` file in the `tests` directory, which will create a single target named
`{package_name}_tests`, and use its contents within tests by importing it.

File `tests/common.cairo`:

```cairo,noplayground
{{#include ../../listings/testing/integration_testing_2/tests/common.cairo}}
```

File with test: `tests/lib.cairo`

```cairo,noplayground
{{#include ../../listings/testing/integration_testing_2/tests/lib.cairo}}
```

Creating the module as `tests/lib.cairo` is recommended to make the `tests` directory
behave like a regular crate, avoiding each file being compiled as a separate test crate.

[unit]: unit_testing.md
[mod]: ../mod.md
