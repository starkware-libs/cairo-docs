# Crates

A crate is a single compilation unit. It has a root directory, and a root module defined at the file
`lib.cairo` under this directory. In the case of a scarb package, the root directory is the
`src` directory, and the root module is defined at the file `lib.cairo`.

Whenever `scarb build` is called, the `src/lib.cairo` is treated as the _crate file_. If
`src/lib.cairo` has `mod` declarations in it, then the contents of the module files would be
inserted in places where `mod` declarations in the crate file are found, _before_ running the
compiler over it. In other words, modules do _not_ get compiled individually, only crates get
compiled.

Because Cairo is strongly coupled to Scarb for its build system, we will use the terms "crate" and
"package" interchangeably.

A crate can be compiled into a starknet contract or a library. By default, `scarb build` will
produce a library from a package. This behavior can be overridden by specifying targets in the `Scarb.toml` file.
