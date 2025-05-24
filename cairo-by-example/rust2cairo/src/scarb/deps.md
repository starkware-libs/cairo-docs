# Dependencies

Most programs have dependencies on some libraries. If you have ever managed
dependencies by hand, you know how much of a pain this can be. Luckily, the Cairo
ecosystem comes standard with `scarb`! `scarb` can manage dependencies for a
project.

To create a new Scarb project,

```sh
scarb new foo
```

The CLI will ask whether you want to use `Starknet Foundry` or `Cairo Test` as the test runner. Although `Starknet Foundry` is principally aimed at Starknet development, it presents useful features for pure Cairo development as well. Let's go with `Starknet Foundry` for this example.

After the above commands, you should see a file hierarchy like this:

```txt
foo
├── Scarb.lock
├── Scarb.toml
├── snfoundry.toml
├── src
│   └── lib.cairo
└── tests
    └── test_contract.cairo
```

The `lib.cairo` is the root source file for your new `foo` project -- nothing new there.
The `Scarb.toml` is the config file for `scarb` for this project. If you
look inside it, you should see something like this:

```toml
{{#include ../../listings/scarb/dependencies/Scarb.toml:1:4}}
```

The `name` field under `[package]` determines the name of the project. This is
used by `crates.io` if you publish the crate (more later). It is also the name
of the output binary when you compile.

The `version` field is a crate version number using [Semantic
Versioning](http://semver.org/).

The `[dependencies]` section lets you add dependencies for your project.

In our example, because we chose `Starknet Foundry` as the test runner, we have
`starknet` as a dependency. But we could also add other dependencies.

For example, suppose that we want our program to handle fixed-point arithmetics. You can find
lots of great packages on [scarbs.xyz](https://scarbs.xyz/packages) (the official Scarb package registry). A package choice for that use case would be is [fp](https://scarbs.xyz/packages/fp).
As of this writing, the most recent published version of `fp` is `0.1.4`. To
add a dependency to our program, we can simply add the following to our
`Scarb.toml` under `[dependencies]`: `fp = "0.1.4"`. And that's it! You can start using
`fp` in your program.
We could also use the CLI to add the dependency:

```sh
scarb add fp@0.1.4
```

`scarb` is more than a dependency manager. All of the available
configuration options are listed in the [format specification][manifest] of
`Scarb.toml`.

To build our project we can execute `scarb build` anywhere in the project
directory (including subdirectories!). We can also do `scarb cairo-run` to build and
run. Notice that these commands will resolve all dependencies, download crates
if needed, and build everything, including your crate. (Note that it only
rebuilds what it has not already built, similar to `make`).

Voila! That's all there is to it!

[manifest]: https://docs.swmansion.com/scarb/docs/reference/manifest.html#the-manifest-format
[dependencies]: https://docs.swmansion.com/scarb/docs/guides/dependencies.html
