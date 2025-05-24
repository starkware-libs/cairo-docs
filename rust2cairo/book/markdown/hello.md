# Hello World

The the source code of the traditional Hello World program in Cairo is identical to the one in [Rust](https://doc.rust-lang.org/rust-by-example/hello.html):

```cairo,editable
// This is a comment, and is ignored by the compiler.
// You can test this code by clicking the "Run" button over there ->
// or if you prefer to use your keyboard, you can use the "Ctrl + Enter"
// shortcut.

// This code is editable, feel free to hack it!
// You can always return to the original code by clicking the "Reset" button ->

// This is the main function.
fn main() {
    // Statements here are executed when the compiled binary is called.

    // Print text to the console.
    println!("Hello World!");
}
```

<!-- `println!` is a [_macro_][macros] that prints text to the
console.

A compiled program can be generated using the Cairo compiler through Scarb: `scarb build`.

```bash
$ scarb build
```

`scarb build` will produce a `hello` binary that can be executed.
`scarb cairo-run` will run the program.

```bash
$ scarb cairo-run
``` -->

### Activity

Click 'Run' above to see the expected output. Next, add a new
line with a second `println!` macro so that the output shows:

```text
Hello World!
I'm a Caironaut!
```

[macros]: https://book.cairo-lang.org/ch12-05-macros.html?#macros
