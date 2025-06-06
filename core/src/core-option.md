# option

Optional values.
The [`Option`](./core-option-Option.md) type represents an optional value: every [`Option`](./core-option-Option.md) is either [`Some`](./core-option.md#some) and
contains a value, or [`None`](./core-option.md#none), and does not. [`Option`](./core-option-Option.md) types are very common in Cairo code, as
they have a number of uses:
- Initial values
- Return values for functions that are not defined
over their entire input range (partial functions)
- Return value for otherwise reporting simple errors, where [`None`](./core-option.md#none) is
returned on error
- Optional struct fields
- Optional function arguments

Options are commonly paired with pattern matching to query the presence of a value and take
action, always accounting for the `None` case.
```cairo
fn divide(numerator: u64, denominator: u64) -> Option<u64> {
    if denominator == 0 {
        None
    } else {
        Some(numerator / denominator)
    }
}

// The return value of the function is an option
let result = divide(2, 3);

// Pattern match to retrieve the value
match result {
    // The division was valid
    Some(x) => println!("Result: {x}"),
    // The division was invalid
    None    => println!("Cannot divide by 0"),
}
```
# The question mark operator, `?`

Similar to the [`Result`](./core-result-Result.md) type, when writing code that calls many functions that return the
[`Option`](./core-option-Option.md) type, handling `Some`/`None` can be tedious. The question mark
operator, `?`, hides some of the boilerplate of propagating values
up the call stack.
It replaces this:
```cairo
fn add_last_numbers(mut array: Array<u32>) -> Option<u32> {
    let a = array.pop_front();
    let b = array.pop_front();

    match (a, b) {
        (Some(x), Some(y)) => Some(x + y),
        _ => None,
    }
}

```

With this:
```cairo
fn add_last_numbers(mut array: Array<u32>) -> Option<u32> {
    Some(array.pop_front()? + array.pop_front()?)
 }
```

It's much nicer!
Ending the expression with `?` will result in the [`Some`](./core-option.md#some)'s unwrapped value, unless the
result is [`None`](./core-option.md#none), in which case [`None`](./core-option.md#none) is returned early from the enclosing function.
`?` can be used in functions that return [`Option`](./core-option-Option.md) because of the
early return of [`None`](./core-option.md#none) that it provides.
# Method overview

In addition to working with pattern matching, [`Option`](./core-option-Option.md) provides a wide
variety of different methods.
## Querying the variant

The `is_some` and `is_none` methods return `true` if the [`Option`](./core-option-Option.md)
is [`Some`](./core-option.md#some) or [`None`](./core-option.md#none), respectively.
## Extracting the contained value

These methods extract the contained value in an `Option<T>` when it
is the [`Some`](./core-option.md#some) variant. If the [`Option`](./core-option-Option.md) is [`None`](./core-option.md#none):
- `expect` panics with a provided custom message
- `unwrap` panics with a generic message
- `unwrap_or` returns the provided default value
- `unwrap_or_default` returns the default value of the type `T`
(which must implement the [`Default`](./core-traits-Default.md) trait)
- `unwrap_or_else` returns the result of evaluating the provided
function
## Transforming contained values

These methods transform [`Option`](./core-option-Option.md) to [`Result`](./core-result-Result.md):
- `ok_or` transforms [`Some(v)`](./core-option.md#some) to [`Ok(v)`](./core-result.md#ok), and [`None`](./core-option.md#none) to
[`Err(err)`](./core-result.md#err) using the provided default `err` value.
- `ok_or_else` transforms [`Some(v)`](./core-option.md#some) to [`Ok(v)`](./core-result.md#ok), and [`None`](./core-option.md#none) to
a value of [`Err`](./core-result.md#err) using the provided function

These methods transform the [`Some`](./core-option.md#some) variant:
- `map` transforms `Option<T>` to `Option<U>` by applying the
provided function to the contained value of [`Some`](./core-option.md#some) and leaving
[`None`](./core-option.md#none) values unchanged

These methods transform `Option<T>` to a value of a possibly
different type `U`:
- `map_or` applies the provided function to the contained value of
[`Some`](./core-option.md#some), or returns the provided default value if the [`Option`](./core-option-Option.md) is
[`None`](./core-option.md#none)
- `map_or_else` applies the provided function to the contained value
of [`Some`](./core-option.md#some), or returns the result of evaluating the provided
fallback function if the [`Option`](./core-option-Option.md) is [`None`](./core-option.md#none)
## Boolean operators

These methods treat the [`Option`](./core-option-Option.md) as a boolean value, where [`Some`](./core-option.md#some)
acts like `true` and [`None`](./core-option.md#none) acts like `false`. There are two
categories of these methods: ones that take an [`Option`](./core-option-Option.md) as input, and
ones that take a function as input (to be lazily evaluated).
The `and`, `or`, and `xor` methods take another [`Option`](./core-option-Option.md) as
input, and produce an [`Option`](./core-option-Option.md) as output. Only the `and` method can
produce an `Option<U>` value having a different inner type `U` than
`Option<T>`.

|method|self|input|output|
|---|---|---|---|
|`and`|`None`|(ignored)|`None`|
|`and`|`Some(x)`|`None`|`None`|
|`and`|`Some(x)`|`Some(y)`|`Some(y)`|
|`or`|`None`|`None`|`None`|
|`or`|`None`|`Some(y)`|`Some(y)`|
|`or`|`Some(x)`|(ignored)|`Some(x)`|
|`xor`|`None`|`None`|`None`|
|`xor`|`None`|`Some(y)`|`Some(y)`|
|`xor`|`Some(x)`|`None`|`Some(x)`|
|`xor`|`Some(x)`|`Some(y)`|`None`|

The `and_then` and `or_else` methods take a function as input, and
only evaluate the function when they need to produce a new value. Only
the `and_then` method can produce an `Option<U>` value having a
different inner type `U` than `Option<T>`.

|method|self|function input|function result|output|
|---|---|---|---|---|
|`and_then`|`None`|(not provided)|(not evaluated)|`None`|
|`and_then`|`Some(x)`|`x`|`None`|`None`|
|`and_then`|`Some(x)`|`x`|`Some(y)`|`Some(y)`|
|`or_else`|`None`|(not provided)|`None`|`None`|
|`or_else`|`None`|(not provided)|`Some(y)`|`Some(y)`|
|`or_else`|`Some(x)`|(not provided)|(not evaluated)|`Some(x)`|
## Iterating over `Option`

An [`Option`](./core-option-Option.md) can be iterated over. This can be helpful if you need an
iterator that is conditionally empty. The iterator will either produce
a single value (when the [`Option`](./core-option-Option.md) is [`Some`](./core-option.md#some)), or produce no values
(when the [`Option`](./core-option-Option.md) is [`None`](./core-option.md#none)). For example, `into_iter`
contains [`Some(v)`](./core-option.md#some) if the [`Option`](./core-option-Option.md) is [`Some(v)`](./core-option.md#some), and [`None`](./core-option.md#none) if the
[`Option`](./core-option-Option.md) is [`None`](./core-option.md#none).

Fully qualified path: [core](./core.md)::[option](./core-option.md)


[Structs](./core-option-structs.md)
 ---
| | |
|:---|:---|
| [OptionIter](./core-option-OptionIter.md) | An iterator over the value in the [`Some`](./core-option.md#some)  variant of an [`Option`](./core-option-Option.md) . The iterator yields one value if the [`Option`](./core-option-Option.md)  is a[...](./core-option-OptionIter.md) |

[Enums](./core-option-enums.md)
 ---
| | |
|:---|:---|
| [Option](./core-option-Option.md) | The `Option<T>`  enum representing either `Some(value)`  or `None` .[...](./core-option-Option.md) |

[Traits](./core-option-traits.md)
 ---
| | |
|:---|:---|
| [OptionTrait](./core-option-OptionTrait.md) | A trait for handling `Option<T>`  related operations.[...](./core-option-OptionTrait.md) |

[Impls](./core-option-impls.md)
 ---
| | |
|:---|:---|
| [DestructOption](./core-option-DestructOption.md) | [...](./core-option-DestructOption.md) |
