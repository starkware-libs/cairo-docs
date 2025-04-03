# Hello World

This is the source code of the traditional Hello World program.

```cairo,editable
{{#include ../listings/hello/hello/src/lib.cairo}}
```

`println!` is a [_macro_][macros] that prints text to the
console.

A compiled program can be generated using the Cairo compiler through Scarb: `scarb build`.

```bash
$ scarb build
```

`scarb build` will produce a `hello` binary that can be executed.
`scarb cairo-run` will run the program.

```bash
$ scarb cairo-run
```

### Activity

Click 'Run' above to see the expected output. Next, add a new
line with a second `println!` macro so that the output shows:

```text
Hello World!
I'm a Caironaute!
```

[macros]: macros.md
