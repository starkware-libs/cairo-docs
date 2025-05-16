# option

Optional values.The [`Option`](./core-option-Option.md) type represents an optional value: every [`Option`](./core-option-Option.md) is either [`Some`](./core-option.md#some) and contains a value, or [`None`](./core-option.md#none), and does not. [`Option`](./core-option-Option.md) types are very common in Cairo code, as they have a number of uses:Initial values * Return values for functions that are not defined over their entire input range (partial functions) * Return value for otherwise reporting simple errors, where [`None`](./core-option.md#none) is returned on error * Optional struct fields * Optional function argumentsOptions are commonly paired with pattern matching to query the presence of a value and take action, always accounting for the `None` case.
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
  # The question mark operator, `?`Similar to the [`Result`](./core-result-Result.md) type, when writing code that calls many functions that return the [`Option`](./core-option-Option.md) type, handling `Some`/`None` can be tedious. The question mark operator, `?`, hides some of the boilerplate of propagating values up the call stack.It replaces this:
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
It's much nicer!Ending the expression with `?` will result in the [`Some`](./core-option.md#some)'s unwrapped value, unless the result is [`None`](./core-option.md#none), in which case [`None`](./core-option.md#none) is returned early from the enclosing function. `?` can be used in functions that return [`Option`](./core-option-Option.md) because of the early return of [`None`](./core-option.md#none) that it provides.[`Some`](./core-option.md#some): Some [`None`](./core-option.md#none): None  # Method overviewIn addition to working with pattern matching, [`Option`](./core-option-Option.md) provides a wide variety of different methods.  ## Querying the variantThe [`is_some`](`is_some`) and [`is_none`](`is_none`) methods return `true` if the [`Option`](./core-option-Option.md) is [`Some`](./core-option.md#some) or [`None`](./core-option.md#none), respectively.[`is_none`](`is_none`): OptionTrait::is_none [`is_none_or`](`is_none_or`): OptionTrait::is_none_or [`is_some`](`is_some`): OptionTrait::is_some [`is_some_and`](`is_some_and`): OptionTrait::is_some_and  ## Extracting the contained valueThese methods extract the contained value in an [`Option<T>`](`Option<T>`) when it is the [`Some`](./core-option.md#some) variant. If the [`Option`](./core-option-Option.md) is [`None`](./core-option.md#none):[`expect`](`expect`) panics with a provided custom message * [`unwrap`](`unwrap`) panics with a generic message * [`unwrap_or`](`unwrap_or`) returns the provided default value * [`unwrap_or_default`](`unwrap_or_default`) returns the default value of the type `T` (which must implement the [`Default`](./core-traits-Default.md) trait) * [`unwrap_or_else`](`unwrap_or_else`) returns the result of evaluating the provided function[`expect`](`expect`): OptionTrait::expect [`unwrap`](`unwrap`): OptionTrait::unwrap [`unwrap_or`](`unwrap_or`): OptionTrait::unwrap_or [`unwrap_or_default`](`unwrap_or_default`): OptionTrait::unwrap_or_default [`unwrap_or_else`](`unwrap_or_else`): OptionTrait::unwrap_or_else  ## Transforming contained valuesThese methods transform [`Option`](./core-option-Option.md) to [`Result`](./core-result-Result.md):[`ok_or`](`ok_or`) transforms [`Some(v)`](`Some(v)`) to [`Ok(v)`](`Ok(v)`), and [`None`](./core-option.md#none) to [`Err(err)`](`Err(err)`) using the provided default `err` value. * [`ok_or_else`](`ok_or_else`) transforms [`Some(v)`](`Some(v)`) to [`Ok(v)`](`Ok(v)`), and [`None`](./core-option.md#none) to a value of [`Err`](./core-result.md#err) using the provided function[`Err(err)`](`Err(err)`): Err [`Ok(v)`](`Ok(v)`): Ok [`Some(v)`](`Some(v)`): Some [`ok_or`](`ok_or`): OptionTrait::ok_or [`ok_or_else`](`ok_or_else`): OptionTrait::ok_or_elseThese methods transform the [`Some`](./core-option.md#some) variant:[`map`](`map`) transforms [`Option<T>`](`Option<T>`) to [`Option<U>`](`Option<U>`) by applying the provided function to the contained value of [`Some`](./core-option.md#some) and leaving [`None`](./core-option.md#none) values unchangedThese methods transform [`Option<T>`](`Option<T>`) to a value of a possibly different type `U`:[`map_or`](`map_or`) applies the provided function to the contained value of [`Some`](./core-option.md#some), or returns the provided default value if the [`Option`](./core-option-Option.md) is [`None`](./core-option.md#none) * [`map_or_else`](`map_or_else`) applies the provided function to the contained value of [`Some`](./core-option.md#some), or returns the result of evaluating the provided fallback function if the [`Option`](./core-option-Option.md) is [`None`](./core-option.md#none)[`map_or`](`map_or`): OptionTrait::map_or [`map_or_else`](`map_or_else`): OptionTrait::map_or_else  ## Boolean operatorsThese methods treat the [`Option`](./core-option-Option.md) as a boolean value, where [`Some`](./core-option.md#some) acts like [`true`](`true`) and [`None`](./core-option.md#none) acts like [`false`](`false`). There are two categories of these methods: ones that take an [`Option`](./core-option-Option.md) as input, and ones that take a function as input (to be lazily evaluated).The [`and`](`and`), [`or`](`or`), and [`xor`](`xor`) methods take another [`Option`](./core-option-Option.md) as input, and produce an [`Option`](./core-option-Option.md) as output. Only the [`and`](`and`) method can produce an [`Option<U>`](`Option<U>`) value having a different inner type `U` than [`Option<T>`](`Option<T>`).| method  | self      | input     | output    | |---------|-----------|-----------|-----------| | [`and`](`and`) | `None`    | (ignored) | `None`    | | [`and`](`and`) | `Some(x)` | `None`    | `None`    | | [`and`](`and`) | `Some(x)` | `Some(y)` | `Some(y)` | | [`or`](`or`)  | `None`    | `None`    | `None`    | | [`or`](`or`)  | `None`    | `Some(y)` | `Some(y)` | | [`or`](`or`)  | `Some(x)` | (ignored) | `Some(x)` | | [`xor`](`xor`) | `None`    | `None`    | `None`    | | [`xor`](`xor`) | `None`    | `Some(y)` | `Some(y)` | | [`xor`](`xor`) | `Some(x)` | `None`    | `Some(x)` | | [`xor`](`xor`) | `Some(x)` | `Some(y)` | `None`    |[`and`](`and`): OptionTrait::and [`or`](`or`): OptionTrait::or [`xor`](`xor`): OptionTrait::xorThe [`and_then`](`and_then`) and [`or_else`](`or_else`) methods take a function as input, and only evaluate the function when they need to produce a new value. Only the [`and_then`](`and_then`) method can produce an [`Option<U>`](`Option<U>`) value having a different inner type `U` than [`Option<T>`](`Option<T>`).| method       | self      | function input | function result | output    | |--------------|-----------|----------------|-----------------|-----------| | [`and_then`](`and_then`) | `None`    | (not provided) | (not evaluated) | `None`    | | [`and_then`](`and_then`) | `Some(x)` | `x`            | `None`          | `None`    | | [`and_then`](`and_then`) | `Some(x)` | `x`            | `Some(y)`       | `Some(y)` | | [`or_else`](`or_else`)  | `None`    | (not provided) | `None`          | `None`    | | [`or_else`](`or_else`)  | `None`    | (not provided) | `Some(y)`       | `Some(y)` | | [`or_else`](`or_else`)  | `Some(x)` | (not provided) | (not evaluated) | `Some(x)` |[`and_then`](`and_then`): OptionTrait::and_then [`or_else`](`or_else`): OptionTrait::or_else ## Iterating over `Option`An [`Option`](./core-option-Option.md) can be iterated over. This can be helpful if you need an iterator that is conditionally empty. The iterator will either produce a single value (when the [`Option`](./core-option-Option.md) is [`Some`](./core-option.md#some)), or produce no values (when the [`Option`](./core-option-Option.md) is [`None`](./core-option.md#none)). For example, [`into_iter`](`into_iter`) contains [`Some(v)`](`Some(v)`) if the [`Option`](./core-option-Option.md) is [`Some(v)`](`Some(v)`), and [`None`](./core-option.md#none) if the [`Option`](./core-option-Option.md) is [`None`](./core-option.md#none).

Fully qualified path: `core::option`

## Structs

- [OptionIter](./core-option-OptionIter.md)

## Enums

- [Option](./core-option-Option.md)

## Traits

- [OptionTrait](./core-option-OptionTrait.md)

## Impls

- [DestructOption](./core-option-DestructOption.md)

