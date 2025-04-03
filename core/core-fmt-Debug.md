# Debug

A trait for debug formatting, using the empty format ("{:?}").  # Examples
```cairo
let word: ByteArray = "123";
println!("{:?}", word);
```

Fully qualified path: `core::fmt::Debug`

```rust
pub trait Debug<T>
```

## Trait functions

### fmt

Fully qualified path: `core::fmt::Debug::fmt`

```rust
fn fmt(self: @T, ref f: Formatter) -> Result<(), Error>
```


