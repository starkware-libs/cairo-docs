# Summary

[Introduction](index.md)

- [Hello World](hello.md)

  - [Comments](hello/comment.md)
  - [Formatted print](hello/print.md)
    - [Debug](hello/print/print_debug.md)
    - [Display](hello/print/print_display.md)
      - [Testcase: List](hello/print/print_display/testcase_list.md)
    - [Formatting](hello/print/fmt.md)

- [Primitives](primitives.md)

  - [Literals and operators](primitives/literals.md)
  - [Tuples](primitives/tuples.md)
  - [Arrays and Slices](primitives/array.md)

- [Custom Types](custom_types.md)

  - [Structures](custom_types/structs.md)
  - [Enums](custom_types/enum.md)
    - [use](custom_types/enum/enum_use.md)
    - [Testcase: linked-list](custom_types/enum/testcase_linked_list.md)
  - [constants](custom_types/constants.md)

- [Variable Bindings](variable_bindings.md)

  - [Mutability](variable_bindings/mut.md)
  - [Scope and Shadowing](variable_bindings/scope.md)
  - [Freezing](variable_bindings/freeze.md)

- [Types](types.md)

  - [Literals](types/literals.md)
  - [Inference](types/inference.md)
  - [Aliasing](types/alias.md)

- [Conversion](conversion.md)

  - [`From` and `Into`](conversion/into.md)
  - [`TryFrom` and `TryInto`](conversion/try_into.md)
  - [To and from `String`s](conversion/bytearray.md)

- [Expressions](expression.md)

- [Flow of Control](flow_control.md)

  - [if/else](flow_control/if_else.md)
  - [loop](flow_control/loop.md)
    - [Returning from loops](flow_control/loop/return.md)
  - [while](flow_control/while.md)
  - [for and range](flow_control/for.md)
  - [match](flow_control/match.md)
    - [Destructuring](flow_control/match/destructuring.md)
      - [enums](flow_control/match/destructuring/destructure_enum.md)
      - [structs](flow_control/match/destructuring/destructure_structures.md)
  - [if let](flow_control/if_let.md)
  - [while let](flow_control/while_let.md)

- [Functions](fn.md)

  - [Methods](fn/methods.md)
  - [Closures](fn/closures.md)
    - [Capturing](fn/closures/capture.md)
    - [As input parameters](fn/closures/input_parameters.md)
    - [Type anonymity](fn/closures/anonymity.md)
    - [Input functions](fn/closures/input_functions.md)
    - [Examples in `core`](fn/closures/closure_examples.md)
      - [Iterator::sum](fn/closures/closure_examples/iter_sum.md)
      - [Searching through iterators](fn/closures/closure_examples/iter_find.md)
  - [Higher Order Functions](fn/hof.md)

- [Modules](mod.md)

  - [Visibility](mod/visibility.md)
  - [Struct visibility](mod/struct_visibility.md)
  - [The `use` declaration](mod/use.md)
  - [`super` and `self`](mod/super.md)
  - [File hierarchy](mod/split.md)

- [Crates](crates.md)

- [Scarb](scarb.md)

  - [Dependencies](scarb/deps.md)
  - [Tests](scarb/test.md)

- [Attributes](attribute.md)

  - [`unused_imports`](attribute/unused.md)
  - [`cfg`](attribute/cfg.md)

- [Generics](generics.md)

  - [Functions](generics/gen_fn.md)
  - [Traits](generics/gen_trait.md)
  - [Implementation](generics/impl.md)
  - [Bounds](generics/bounds.md)
    - [Testcase: empty bounds](generics/bounds/testcase_empty.md)
  - [Multiple bounds](generics/multi_bounds.md)
  - [Associated items](generics/assoc_items.md)
    - [The Problem](generics/assoc_items/the_problem.md)
    - [Associated types](generics/assoc_items/types.md)

- [Scoping rules](scope.md)

  - [RAII](scope/raii.md)
  - [Ownership, and moves](scope/move.md)
    - [Mutability](scope/move/mut.md)
  - [Retaining Ownership](scope/retaining_ownership.md)
    - [Snapshots](scope/retaining_ownership/snapshots.md)
    - [References](scope/retaining_ownership/ref.md)

- [Traits](trait.md)

  - [Derive](trait/derive.md)
  - [Operator Overloading](trait/ops.md)
  - [Drop and Destruct](trait/drop.md)
  - [Iterators](trait/iter.md)
  - [Clone](trait/clone.md)
  - [Disambiguating overlapping traits](trait/disambiguating.md)

- [Error handling](error.md)

  - [`panic`](error/panic.md)
  - [`Option` & `unwrap`](error/option_unwrap.md)
    - [Unpacking options with `?`](error/option_unwrap/question_mark.md)
    - [Combinators: `map`](error/option_unwrap/map.md)
    - [Combinators: `and_then`](error/option_unwrap/and_then.md)
    - [Defaults: `or`, `or_else`](error/option_unwrap/defaults.md)
  - [`Result`](error/result.md)
    - [`map` for `Result`](error/result/result_map.md)
    - [aliases for `Result`](error/result/result_alias.md)
    - [Early returns](error/result/early_returns.md)
    - [Introducing `?`](error/result/enter_question_mark.md)
  - [Multiple error types](error/multiple_error_types.md)
    - [Pulling `Result`s out of `Option`s](error/multiple_error_types/option_result.md)
    - [Defining an error type](error/multiple_error_types/define_error_type.md)

- [Core library types](core.md)

  - [Dictionaries](core/dict.md)
  - [Box and Memory Segments](core/box.md)
  - [ByteArrays](core/bytearrays.md)
  - [`Option`](core/option.md)
  - [`Result`](core/result.md)
    - [`?`](core/result/question_mark.md)
  - [`panic!`](core/panic.md)

- [Testing](testing.md)

  - [Unit testing](testing/unit_testing.md)
  - [Integration testing](testing/integration_testing.md)
  - [Dev-dependencies](testing/dev_dependencies.md)

- [Meta](meta.md)
  - [Documentation](meta/doc.md)
  - [Playground](meta/playground.md)
