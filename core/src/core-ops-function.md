# function

Function traits and types.
This module defines traits for function-like types that can be called.
The two main traits are:
- [`FnOnce`](./core-ops-function-FnOnce.md) - For single-use functions that consume their environment
- [`Fn`](./core-ops-function-Fn.md) - For reusable functions that can be called multiple times
# Examples

```cairo
// Using Fn for a reusable operation
fn apply_twice<F, +Drop<F>, +core::ops::Fn<F, (u32,)>[Output: u32]>(f: F, x: u32) -> u32 {
    f(f(x))
}

let double = |x| x * 2;
assert!(apply_twice(double, 2) == 8);
```

Fully qualified path: [core](./core.md)::[ops](./core-ops.md)::[function](./core-ops-function.md)


[Traits](./core-ops-function-traits.md)
 ---
| | |
|:---|:---|
| [Fn](./core-ops-function-Fn.md) | The version of the call operator that takes a by-snapshot receiver. Instances of `Fn`  can be called repeatedly. `Fn`  is implemented automatically by closures whose captured variables are all `Copy`[...](./core-ops-function-Fn.md) |
| [FnOnce](./core-ops-function-FnOnce.md) | The version of the call operator that takes a by-value receiver. Instances of `FnOnce`  can be called, but might not be callable multiple[...](./core-ops-function-FnOnce.md) |
