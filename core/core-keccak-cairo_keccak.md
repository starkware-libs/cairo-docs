# cairo_keccak

Computes the keccak of `input` + `last_input_num_bytes` LSB bytes of `last_input_word`. To use this function, split the input into words of 64 bits (little endian). For example, to compute keccak('Hello world!'), use:   inputs = [8031924123371070792, 560229490]([8031924123371070792, 560229490]) where:   8031924123371070792 == int.from_bytes(b'Hello wo', 'little')   560229490 == int.from_bytes(b'rld!', 'little')  Returns the hash as a little endian u256.

Fully qualified path: `core::keccak::cairo_keccak`

```rust
pub fn cairo_keccak(
    ref input: Array<u64>, last_input_word: u64, last_input_num_bytes: usize,
) -> u256
```

