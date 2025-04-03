# u384

A 384-bit unsigned integer, used for circuit values.

Fully qualified path: `core::circuit::u384`

```rust
#[derive(Copy, Drop, Debug, PartialEq)]
pub struct u384 {
    pub limb0: u96,
    pub limb1: u96,
    pub limb2: u96,
    pub limb3: u96,
}
```

