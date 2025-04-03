# cheatcode

A general cheatcode function used to simplify implementation of Starknet testing functions.  This is the base function used by testing utilities to interact with the test environment. External users can implement custom cheatcodes by injecting a custom `CairoHintProcessor` in the runner.  # Arguments  `selector` - The cheatcode identifier. `input` - Input parameters for the cheatcode.  # Returns  * A span containing the cheatcode's output

Fully qualified path: `core::starknet::testing::cheatcode`

```rust
pub extern fn cheatcode<const selector: felt252>(
    input: Span<felt252>,
) -> Span<felt252> implicits() nopanic;
```

