# traits

Core traits for various operations.This module provides a collection of essential traits that define common behavior patterns for Cairo types.  # Main Categories  ## Memory Management - [`Copy`](./core-traits-Copy.md): Enables value semantics for types - [`Drop`](./core-traits-Drop.md): Allows values to be safely discarded - [`Destruct`](./core-traits-Destruct.md): Provides custom cleanup behavior for non-droppable types - [`PanicDestruct`](./core-traits-PanicDestruct.md): Handles destruction during panic scenarios  ## Arithmetic Operations - [`Add`](./core-traits-Add.md), [`Sub`](./core-traits-Sub.md), [`Mul`](./core-traits-Mul.md), [`Div`](./core-traits-Div.md), [`Rem`](./core-traits-Rem.md): Standard arithmetic operators (`+`, `-`, `*`, `/`, `%`) - [`DivRem`](./core-traits-DivRem.md): Combined division and remainder operation - [`Neg`](./core-traits-Neg.md): Unary negation (`-`)  ## Bitwise Operations - [`BitAnd`](./core-traits-BitAnd.md), [`BitOr`](./core-traits-BitOr.md), [`BitXor`](./core-traits-BitXor.md): Binary bitwise operations (`&`, `|`, `^`) - [`BitNot`](./core-traits-BitNot.md): Unary bitwise complement (`~`)  ## Comparison - [`PartialEq`](./core-traits-PartialEq.md): Equality comparison (`==`, `!=`) - [`PartialOrd`](./core-traits-PartialOrd.md): Ordering comparison (`<`, `<=`, `>`, `>=`)  ## Type Conversion - [`Into`](./core-traits-Into.md): Infallible type conversion - [`TryInto`](./core-traits-TryInto.md): Fallible type conversion  ## Utility Traits - [`Default`](./core-traits-Default.md): Creation of default values - [`Felt252DictValue`](./core-traits-Felt252DictValue.md): Support for dictionary value types

Fully qualified path: `core::traits`

## Traits

- [Copy](./core-traits-Copy.md)

- [Drop](./core-traits-Drop.md)

- [Add](./core-traits-Add.md)

- [AddEq](./core-traits-AddEq.md)

- [Sub](./core-traits-Sub.md)

- [SubEq](./core-traits-SubEq.md)

- [Mul](./core-traits-Mul.md)

- [MulEq](./core-traits-MulEq.md)

- [Div](./core-traits-Div.md)

- [DivEq](./core-traits-DivEq.md)

- [Rem](./core-traits-Rem.md)

- [RemEq](./core-traits-RemEq.md)

- [DivRem](./core-traits-DivRem.md)

- [PartialEq](./core-traits-PartialEq.md)

- [BitAnd](./core-traits-BitAnd.md)

- [BitOr](./core-traits-BitOr.md)

- [BitXor](./core-traits-BitXor.md)

- [BitNot](./core-traits-BitNot.md)

- [PartialOrd](./core-traits-PartialOrd.md)

- [Into](./core-traits-Into.md)

- [TryInto](./core-traits-TryInto.md)

- [Neg](./core-traits-Neg.md)

- [Not](./core-traits-Not.md)

- [IndexView](./core-traits-IndexView.md)

- [Index](./core-traits-Index.md)

- [Destruct](./core-traits-Destruct.md)

- [PanicDestruct](./core-traits-PanicDestruct.md)

- [Default](./core-traits-Default.md)

- [Felt252DictValue](./core-traits-Felt252DictValue.md)

