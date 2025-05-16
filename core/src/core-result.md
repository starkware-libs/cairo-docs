# result

Error handling with the `Result` type.[`Result`](./core-result-Result.md) is the type used for returning and propagating errors. It is an enum with the variants, [`Ok(T)`](`Ok(T)`), representing success and containing a value, and [`Err(E)`](`Err(E)`), representing error and containing an error value.
```cairo
enum Result<T, E> {
   Ok: T,
   Err: E,
}
```
Functions return [`Result`](./core-result-Result.md) whenever errors are expected and recoverable.A simple function returning [`Result`](./core-result-Result.md) might be defined and used like so:
```cairo
fn parse_version(header: felt252) -> Result<felt252, felt252> {
    match header {
        0 => Ok(0),
        1 => Ok(1),
        _ => Err('invalid version'),
    }
}

let version = parse_version(1);
match version {
    Ok(v) => println!("working with version {}", v),
    Err(e) => println!("error parsing version: {:?}", e)
}
```
  # Results must be usedA common problem with using return values to indicate errors is that it is easy to ignore the return value, thus failing to handle the error. [`Result`](./core-result-Result.md) is annotated with the `#[must_use]` attribute, which will cause the compiler to issue a warning when a Result value is ignored.  # Method overviewIn addition to working with pattern matching, [`Result`](./core-result-Result.md) provides a wide variety of different methods.  ## Querying the variantThe [`is_ok`](`is_ok`) and [`is_err`](`is_err`) methods return `true` if the [`Result`](./core-result-Result.md) is [`Ok`](./core-result.md#ok) or [`Err`](./core-result.md#err), respectively.  ## Extracting contained valuesThese methods extract the contained value in a [`Result<T, E>`](`Result<T, E>`) when it is the [`Ok`](./core-result.md#ok) variant. If the [`Result`](./core-result-Result.md) is [`Err`](./core-result.md#err):[`expect`](`expect`) panics with a provided felt252 error message * [`unwrap`](`unwrap`) panics with a generic message * [`unwrap_or`](`unwrap_or`) returns the provided default value * [`unwrap_or_default`](`unwrap_or_default`) returns the default value of the type `T` (which must implement the [`Default`](./core-traits-Default.md) trait) * [`unwrap_or_else`](`unwrap_or_else`) returns the result of evaluating the provided function[`expect`](`expect`): ResultTrait::expect [`unwrap`](`unwrap`): ResultTrait::unwrap [`unwrap_or`](`unwrap_or`): ResultTrait::unwrap_or [`unwrap_or_default`](`unwrap_or_default`): ResultTrait::unwrap_or_default [`unwrap_or_else`](`unwrap_or_else`): ResultTrait::unwrap_or_elseThese methods extract the contained value in a [`Result<T, E>`](`Result<T, E>`) when it is the [`Err`](./core-result.md#err) variant. If the [`Result`](./core-result-Result.md) is [`Ok`](./core-result.md#ok):[`expect_err`](`expect_err`) panics with a provided felt252 error message * [`unwrap_err`](`unwrap_err`) panics with a generic message[`expect_err`](`expect_err`): ResultTrait::expect_err [`unwrap_err`](`unwrap_err`): ResultTrait::unwrap_err  ## Transforming contained valuesThese methods transform [`Result`](./core-result-Result.md) to [`Option`](./core-option-Option.md):[`ok`](`ok`) transforms [`Result<T, E>`](`Result<T, E>`) into [`Option<T>`](`Option<T>`), mapping [`Ok(v)`](`Ok(v)`) to [`Some(v)`](`Some(v)`) and [`Err(e)`](`Err(e)`) to [`None`](./core-option.md#none) * [`err`](`err`) transforms [`Result<T, E>`](`Result<T, E>`) into [`Option<E>`](`Option<E>`), mapping [`Ok(v)`](`Ok(v)`) to [`None`](./core-option.md#none) and [`Err(e)`](`Err(e)`) to [`Some(e)`](`Some(e)`)This method transforms the contained value of the [`Ok`](./core-result.md#ok) variant:[`map`](`map`) transforms [`Result<T, E>`](`Result<T, E>`) into [`Result<U, E>`](`Result<U, E>`) by applying the provided function to the contained value of [`Ok`](./core-result.md#ok) and leaving [`Err`](./core-result.md#err) values unchangedThis method transforms the contained value of the [`Err`](./core-result.md#err) variant:[`map_err`](`map_err`) transforms [`Result<T, E>`](`Result<T, E>`) into [`Result<T, F>`](`Result<T, F>`) by applying the provided function to the contained value of [`Err`](./core-result.md#err) and leaving [`Ok`](./core-result.md#ok) values unchangedThese methods transform a [`Result<T, E>`](`Result<T, E>`) into a value of a possibly different type `U`:[`map_or`](`map_or`) applies the provided function to the contained value of [`Ok`](./core-result.md#ok), or returns the provided default value if the [`Result`](./core-result-Result.md) is [`Err`](./core-result.md#err) * [`map_or_else`](`map_or_else`) applies the provided function to the contained value of [`Ok`](./core-result.md#ok), or applies the provided default fallback function to the contained value of [`Err`](./core-result.md#err)[`map_or`](`map_or`): ResultTrait::map_or [`map_or_else`](`map_or_else`): ResultTrait::map_or_else  ## Boolean operatorsThese methods treat the [`Result`](./core-result-Result.md) as a boolean value, where [`Ok`](./core-result.md#ok) acts like [`true`](`true`) and [`Err`](./core-result.md#err) acts like [`false`](`false`). There are two categories of these methods: ones that take a [`Result`](./core-result-Result.md) as input, and ones that take a function as input.The [`and`](`and`) and [`or`](`or`) methods take another [`Result`](./core-result-Result.md) as input, and produce a [`Result`](./core-result-Result.md) as output. The [`and`](`and`) method can produce a [`Result<U, E>`](`Result<U, E>`) value having a different inner type `U` than [`Result<T, E>`](`Result<T, E>`). The [`or`](`or`) method can produce a [`Result<T, F>`](`Result<T, F>`) value having a different error type `F` than [`Result<T, E>`](`Result<T, E>`).| method  | self     | input     | output   | |---------|----------|-----------|----------| | [`and`](`and`) | `Err(e)` | (ignored) | `Err(e)` | | [`and`](`and`) | `Ok(x)`  | `Err(d)`  | `Err(d)` | | [`and`](`and`) | `Ok(x)`  | `Ok(y)`   | `Ok(y)`  | | [`or`](`or`)  | `Err(e)` | `Err(d)`  | `Err(d)` | | [`or`](`or`)  | `Err(e)` | `Ok(y)`   | `Ok(y)`  | | [`or`](`or`)  | `Ok(x)`  | (ignored) | `Ok(x)`  |[`and`](`and`): ResultTrait::and [`or`](`or`): ResultTrait::orThe [`and_then`](`and_then`) and [`or_else`](`or_else`) methods take a function as input, and only evaluate the function when they need to produce a new value. The [`and_then`](`and_then`) method can produce a [`Result<U, E>`](`Result<U, E>`) value having a different inner type `U` than [`Result<T, E>`](`Result<T, E>`). The [`or_else`](`or_else`) method can produce a [`Result<T, F>`](`Result<T, F>`) value having a different error type `F` than [`Result<T, E>`](`Result<T, E>`).| method       | self     | function input | function result | output   | |--------------|----------|----------------|-----------------|----------| | [`and_then`](`and_then`) | `Err(e)` | (not provided) | (not evaluated) | `Err(e)` | | [`and_then`](`and_then`) | `Ok(x)`  | `x`            | `Err(d)`        | `Err(d)` | | [`and_then`](`and_then`) | `Ok(x)`  | `x`            | `Ok(y)`         | `Ok(y)`  | | [`or_else`](`or_else`)  | `Err(e)` | `e`            | `Err(d)`        | `Err(d)` | | [`or_else`](`or_else`)  | `Err(e)` | `e`            | `Ok(y)`         | `Ok(y)`  | | [`or_else`](`or_else`)  | `Ok(x)`  | (not provided) | (not evaluated) | `Ok(x)`  |[`and_then`](`and_then`): ResultTrait::and_then [`or_else`](`or_else`): ResultTrait::or_else  # The question mark operator, `?`When writing code that calls many functions that return the [`Result`](./core-result-Result.md) type, handling `Ok`/`Err` can be tedious. The question mark operator, `?`, hides some of the boilerplate of propagating errors up the call stack.It replaces this:
```cairo
use core::integer::u8_overflowing_add;

fn add_three_numbers(a: u8, b: u8, c: u8) -> Result<u8, u8> {
    match u8_overflowing_add(a, b) {
        Ok(sum_ab) => {
            match u8_overflowing_add(sum_ab, c) {
                Ok(total) => Ok(total),
                Err(e) => Err(e),
            }
        },
        Err(e) => Err(e),
    }
}
```
With this:
```cairo
use core::integer::u8_overflowing_add;

fn add_three_numbers_2(a: u8, b: u8, c: u8) -> Result<u8, u8> {
    let total = u8_overflowing_add(u8_overflowing_add(a, b)?, c)?;
    Ok(total)
}
```
It's much nicer![`Ok`](./core-result.md#ok): Ok [`Err`](./core-result.md#err): Err  ## Iterating over `Result`A [`Result`](./core-result-Result.md) can be iterated over. This can be helpful if you need an iterator that is conditionally empty. The iterator will either produce a single value (when the [`Result`](./core-result-Result.md) is [`Ok`](./core-result.md#ok)), or produce no values (when the [`Result`](./core-result-Result.md) is [`Err`](./core-result.md#err)). For example, [`into_iter`](`into_iter`) contains [`Some(v)`](`Some(v)`) if the [`Result`](./core-result-Result.md) is [`Ok(v)`](`Ok(v)`), and [`None`](./core-option.md#none) if the [`Result`](./core-result-Result.md) is [`Err`](./core-result.md#err).

Fully qualified path: `core::result`

## Enums

- [Result](./core-result-Result.md)

## Traits

- [ResultTrait](./core-result-ResultTrait.md)

