# Comments

Cairo supports the same comment varieties as [Rust]((https://doc.rust-lang.org/rust-by-example/hello.html)), except for regular block comments:

```cairo,editable
//! This is an example of a module-level doc comment.

/// This is an example of a item-level doc comment.
fn main() { // This is an example of a line comment.
// There are two slashes at the beginning of the line.
// And nothing written after these will be read by the compiler.

// println!("Hello, world!");
}
```

### Activity

Click 'Run' above to see that nothing is outputted. Next, delete the last two slashes, and run it again to see the exepcted output.