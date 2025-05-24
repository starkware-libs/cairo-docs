# RAII

Variables in Cairo do more than just hold data in memory: they also _own_ resources, e.g. `Box<T>`
owns a pointer to memory, `Felt252Dict` owns a memory segment. Cairo enforces [RAII][raii] (Resource
Acquisition Is Initialization), so whenever an object goes out of scope, its destructor is called to
handle the cleanup of its owned resources.

This behavior protects against [_soundness_][soundness] issues and concurrent memory accesses, ensuring that:

1. It would be infeasible for a cheating prover to convince a verifier of a false statement, as some
   resources (like [dictionaries][dictionaries]) require specialized destruction logic.
2. No memory cell is written to twice due to concurrent accesses, which would crash the VM.

Here's a quick showcase:

```cairo,editable
{{#include ../../listings/scope/raii/src/lib.cairo}}
```

## Destructor

The notion of a destructor in Rust is provided through the [`Drop`][drop] and [`Destruct`][destruct] traits. The
destructor is called when the resource goes out of scope. One of the two traits is
required to be implemented for every type:

- If your type does not require any specific destructor logic, implement the [`Drop`][drop] trait, which can trivially be [derived][derive].
- If your type requires does specific destructor logic, applicable to any type containing a [dictionary][dictionaries], implement the [`Destruct`][destruct] trait. It can also be [derived][derive].

Run the below example to see how the [`Drop`][drop] trait works. When the variables in
the `main` function goes out of scope the custom destructor will be invoked. Try to fix the error for the variable of type `ToDestruct`.

```cairo,editable
{{#include ../../listings/scope/raii_2/src/lib.cairo}}
```

### See also:

[Box][box]

[raii]: https://en.wikipedia.org/wiki/Resource_Acquisition_Is_Initialization
[box]: ../core/box.md
[soundness]: https://en.wikipedia.org/wiki/Zero-knowledge_proof#Soundness
[dictionaries]: ../core/dict.md
[derive]: ../trait/derive.md
[drop]: ../trait/drop.md
[destruct]: ../trait/drop.md
