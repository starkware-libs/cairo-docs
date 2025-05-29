# traits

Core traits for various operations.
This module provides a collection of essential traits that define common behavior patterns
for Cairo types.
# Main Categories
## Memory Management

- [`Copy`](./core-traits-Copy.md): Enables value semantics for types
- [`Drop`](./core-traits-Drop.md): Allows values to be safely discarded
- [`Destruct`](./core-traits-Destruct.md): Provides custom cleanup behavior for non-droppable types
- [`PanicDestruct`](./core-traits-PanicDestruct.md): Handles destruction during panic scenarios
## Arithmetic Operations

- [`Add`](./core-traits-Add.md), [`Sub`](./core-traits-Sub.md), [`Mul`](./core-traits-Mul.md), [`Div`](./core-traits-Div.md), [`Rem`](./core-traits-Rem.md): Standard arithmetic operators (`+`, `-`, `*`,
`/`, `%`)
- [`DivRem`](./core-traits-DivRem.md): Combined division and remainder operation
- [`Neg`](./core-traits-Neg.md): Unary negation (`-`)
## Bitwise Operations

- [`BitAnd`](./core-traits-BitAnd.md), [`BitOr`](./core-traits-BitOr.md), [`BitXor`](./core-traits-BitXor.md): Binary bitwise operations (`&`, `|`, `^`)
- [`BitNot`](./core-traits-BitNot.md): Unary bitwise complement (`~`)
## Comparison

- [`PartialEq`](./core-traits-PartialEq.md): Equality comparison (`==`, `!=`)
- [`PartialOrd`](./core-traits-PartialOrd.md): Ordering comparison (`<`, `<=`, `>`, `>=`)
## Type Conversion

- [`Into`](./core-traits-Into.md): Infallible type conversion
- [`TryInto`](./core-traits-TryInto.md): Fallible type conversion
## Utility Traits

- [`Default`](./core-traits-Default.md): Creation of default values
- [`Felt252DictValue`](./core-traits-Felt252DictValue.md): Support for dictionary value types

Fully qualified path: [core](./core.md)::[traits](./core-traits.md)


[Traits](./core-traits-traits.md)
 ---
| | |
|:---|:---|
| [Copy](./core-traits-Copy.md) | A trait for copying values. By default, variables in Cairo have 'move semantics', meaning they are moved when used. However, types implementing `Copy`  have 'copy semantics', allowing the value to be[...](./core-traits-Copy.md) |
| [Drop](./core-traits-Drop.md) | A trait for types that can be safely dropped. Types implementing `Drop`  can be automatically discarded when they go out of scope.[...](./core-traits-Drop.md) |
| [Add](./core-traits-Add.md) | The addition operator `+` .[...](./core-traits-Add.md) |
| [AddEq](./core-traits-AddEq.md) | [...](./core-traits-AddEq.md) |
| [Sub](./core-traits-Sub.md) | The subtraction operator `-` .[...](./core-traits-Sub.md) |
| [SubEq](./core-traits-SubEq.md) | [...](./core-traits-SubEq.md) |
| [Mul](./core-traits-Mul.md) | The multiplication operator `*` .[...](./core-traits-Mul.md) |
| [MulEq](./core-traits-MulEq.md) | [...](./core-traits-MulEq.md) |
| [Div](./core-traits-Div.md) | The division operator `/` . Types implementing this trait support the division operation via the `/`  operator.[...](./core-traits-Div.md) |
| [DivEq](./core-traits-DivEq.md) | [...](./core-traits-DivEq.md) |
| [Rem](./core-traits-Rem.md) | The remainder operator `%` . Types implementing this trait support the remainder operation via the `%`  operator.[...](./core-traits-Rem.md) |
| [RemEq](./core-traits-RemEq.md) | [...](./core-traits-RemEq.md) |
| [DivRem](./core-traits-DivRem.md) | Performs truncated division and remainder. This trait provides a way to efficiently compute both the quotient and remainder in a single[...](./core-traits-DivRem.md) |
| [PartialEq](./core-traits-PartialEq.md) | Trait for comparisons using the equality operator. Implementing this trait for types provides the `==`  and `!=`  operators for those types.[...](./core-traits-PartialEq.md) |
| [BitAnd](./core-traits-BitAnd.md) | The bitwise AND operator `&` .[...](./core-traits-BitAnd.md) |
| [BitOr](./core-traits-BitOr.md) | The bitwise OR operator `|` .[...](./core-traits-BitOr.md) |
| [BitXor](./core-traits-BitXor.md) | The bitwise XOR operator `^` .[...](./core-traits-BitXor.md) |
| [BitNot](./core-traits-BitNot.md) | The bitwise NOT operator `~` .[...](./core-traits-BitNot.md) |
| [PartialOrd](./core-traits-PartialOrd.md) | Trait for comparing types that form a partialorder . The `lt` , `le` , `gt` , and `ge`  methods of this trait can be called using the `<` , `<=` , `>` , and `>=`  operators, respectively.[...](./core-traits-PartialOrd.md) |
| [Into](./core-traits-Into.md) | A value-to-value conversion that consumes the input value. Note: This trait must not fail . If the conversion can fail, use [`TryInto`](./core-traits-TryInto.md) .[...](./core-traits-Into.md) |
| [TryInto](./core-traits-TryInto.md) | Simple and safe type conversions that may fail in a controlled way under some circumstances. This is useful when you are doing a type conversion that may trivially succeed but may also need[...](./core-traits-TryInto.md) |
| [Neg](./core-traits-Neg.md) | The unary negation operator `-` .[...](./core-traits-Neg.md) |
| [Not](./core-traits-Not.md) | The unary logical negation operator `!` .[...](./core-traits-Not.md) |
| [IndexView](./core-traits-IndexView.md) | [...](./core-traits-IndexView.md) |
| [Index](./core-traits-Index.md) | [...](./core-traits-Index.md) |
| [Destruct](./core-traits-Destruct.md) | A trait that allows for custom destruction behavior of a type. In Cairo, values must be explicitly handled - they cannot be silently dropped. Types can only go out of scope in two ways: 1. Implement[...](./core-traits-Destruct.md) |
| [PanicDestruct](./core-traits-PanicDestruct.md) | A trait that allows for destruction of a value in case of a panic. This trait is automatically implemented from the `Destruct`  implementation for a type.[...](./core-traits-PanicDestruct.md) |
| [Default](./core-traits-Default.md) | A trait for giving a type a useful default value. Cairo implements `Default`  for various primitives types.[...](./core-traits-Default.md) |
| [Felt252DictValue](./core-traits-Felt252DictValue.md) | A trait that must be implemented for any type that will be stored as a value in a `Felt252Dict` . When working with dictionaries in Cairo, we need a way to represent "empty" or "uninitialized"[...](./core-traits-Felt252DictValue.md) |
