# Display

A trait for standard formatting, using the empty format ("{}").  # Examples
```cairo
let word: ByteArray = "123";
println!("{}", word);
```

Fully qualified path: `core::fmt::Display`

```rust
pub trait Display<T>
```

## Trait functions

### fmt

Fully qualified path: `core::fmt::Display::fmt`

```rust
fn fmt(self: @T, ref f: Formatter) -> Result<(), Error>
```


