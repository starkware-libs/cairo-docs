# Hello World

This is the Cairo adaptation of [Chapter 1 of Rust By Example](https://doc.rust-lang.org/rust-by-example/hello.html):

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

### Activity

Click 'Run' above to see the expected output. Next, add a new
line with a second `println!` macro so that the output shows:

```text
Hello World!
I'm a Caironaut!
```

[macros]: https://book.cairo-lang.org/ch12-05-macros.html?#macros
