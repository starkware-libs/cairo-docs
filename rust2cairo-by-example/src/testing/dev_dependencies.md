# Development dependencies

Sometimes there is a need to have dependencies for tests (or examples,
or benchmarks) only. Such dependencies are added to `Scarb.toml` in the
`[dev-dependencies]` section. These dependencies are not propagated to other
packages which depend on this package.
When you start a new project with `scarb new`, you will notice that the `Scarb.toml` file contains the `assert_macros` dev-dependency. This macro is required to use the `assert_` macros presented in [unit-testing][unit-testing].

File `Scarb.toml`:

```toml
{{#include ../../listings/testing/dev_dependencies/Scarb.toml:1:9}}
```

File `src/lib.cairo`:

```cairo,ignore
{{#include ../../listings/testing/dev_dependencies/src/lib.cairo}}
```

## See Also

[Scarb][scarb] docs on specifying dependencies.

[unit-testing]: ./unit_testing.md
[scarb]: https://docs.swmansion.com/scarb/docs/reference/specifying-dependencies.html
