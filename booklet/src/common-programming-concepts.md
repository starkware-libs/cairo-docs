# Common Programming Concepts

This chapter covers concepts that appear in almost every programming language and how they work in Cairo.

## Variables and Mutability

Data can be stored in variables using the `let` keyword. Variables use the `snake_case` by convention and can be type annotated, but their type can also infer types from context. By default, variable are immutable, but this can be overridden using the `mut` modifier. Variables can also be "shadowed" by a declaration of a new variable with the same name.

Data can be stored in constants using the `const` keyword. Unlike variables, constants:
* use the `SCREAMING_SNAKE_CASE` by convention
* must be type annotated
* do not allow the `mut` modifier (i.e., they are *always* immutable)
* must set to a constant expression
* can be declared in the global scope

**Example:** 

```cairo,noplayground
const GLOBAL_CONST: bool = false;

fn main() {
    let immutable_var = GLOBAL_CONST;
    let mut mutable_var = GLOBAL_CONST;
    mutable_var = true;
    let immutable_var = true;
    assert!(mutable_var && immutable_var);
}
```
*Experiment with this example on [the Cairo playground](https://www.cairo-lang.org/cairovm/) or read more in [the Cairo Book](https://book.cairo-lang.org/)!*

## Data Types

The basic data type in Cairo is `felt252`. These are integers in the range `0 ≤ x < P`, where `P` is a large prime equal to:

$$3618502788666131213697322783095070105623107215331596699973092056135872020481$$

`felt252` is the default data type for numerical literals, so in many cases there is no real need to specify the type of numerical variables. Unlike integers, however, adding, subtracting, or multiplying felts is computed modulo `P`, and dividing felts has to be done via the `felt252_div(lhs, rhs)` function, which returns `c` such that `lhs = c * rhs mod P`. 

It is therefore highly recommended to use integer types where possible, which also come with extra protection against potential vulnerabilities in the code, such as overflow checks. Integer types include `i8`, `i16`, `i32`, `i64`, `i128` for signed integers and `u8`, `u16`, `u32`, `u64`, `u128`, `u256` for unsigned integers, and can also be annotated using a suffix. Integer literals can also be written binary, octal, hex, or decimal.

Cairo's third and last scalar data type is the boolean type, which is specified using `bool` and has only two possible values: `true` or `false`. Unlike other programming languages, using integer literals for bool declarations (e.g., `0` instead of `false`) is not allowed.

Note that Cairo doesn't have a native type for strings, and instead uses `felt252` to store the ASCII endoing of strings shorter than 31 characters, which can be written using simple quotes (e.g., `'abc'`) or represented with an hexadecimal value (e.g., `0x616263`). Cairo's Core library provides a `ByteArray` type for handling strings that contain more than 31 characters, which are written using double quotes (e.g., `"abc"`).

Cairo has two compound data types for grouping together a fixed number of values into one compound:

* Tuples, which group together values with different types, and are created by writing a comma-separated list of values inside parentheses
* Fixed-size arrays, which group together values with the same type, and are created by writing a comma-separated list of values or semicolon-separated initial value and length inside square brackets

Both tuples and arrays can be declared with or without specifying the type of each element in them, and deconstructed during or after their declaration.

Cairo addresses conversion between types by using the `try_into` and `into` methods provided by the `TryInto` and `Into` traits from the Core library. Unlike `Into`, the `TryInto` trait is used for fallible conversions, and as such, returns `Option<T>`. To perform the conversion, `into` or `try_into` needs to be called on the source value, and the new variable's type must be explicitly defined.

**Example:** 

```cairo,editable
fn main() {
    let P_minus_1 = 3618502788666131213697322783095070105623107215331596699973092056135872020480;
    let P_plus_1_halved = 1809251394333065606848661391547535052811553607665798349986546028067936010241;
    assert!(2 - 1 == 1);
    assert!(1 - 2 == P_minus_1);
    assert!(felt252_div(2, 1) == 2);
    assert!(felt252_div(1, 2) == P_plus_1_halved); // 1 = (P+1)/2 * 2 (mod P)

    let one: u8 = 1;
    let two = 0b0010_u8;
    assert!(one * one == one);
    assert!(two & two == two);

    let short_string = 'a';
    let long_string: ByteArray = "this is a string which has more than 31 characters";    
    assert!(short_string + 1 == 'b');
    assert!(long_string.len() > 31);

    let tup: (bool, u8) = (true, 1);
    let (t, _) = tup;
    let (_, f) = (0, false);
    assert!(t && !f);
}
```
*Experiment with this example on [the Cairo playground](https://www.cairo-lang.org/cairovm/) or read more in [the Cairo Book](https://book.cairo-lang.org/)!*

## Functions

## Comments

## Control flow

The most common constructs that let you control the flow of execution of Cairo code are if expressions and loops.

All `if` expressions start with the keyword `if`, followed by a condition. Optionally, we can also include an `else` expression. You can use multiple conditions by combining `if` and `else` in an `else if` expression.

Cairo has three kinds of loops:
* The `loop` keyword tells Cairo to loop and execute a block of code until you explicitly told to to stop
* The `while` keyword tells Cairo to loop and execute a block of code as long as a condition is met
* The `for` keyword tells Cairo to loop and execute a block of code over for each item in a collection.

**Example:**
```cairo,editable
fn main() {
    let mut res: u8 = 1;
    loop {
        if res == 5 {
            break;
        }
        res += 1;
    };
    assert!(res == 5);
    while res != 1 {
        res -= 1;
    };
    assert!(res == 1);
    for n in 1..5_u8 { // Range of 1 to 5
        assert!(res == n);
        res += 1;
    };
}
```
*Experiment with this example on [the Cairo playground](https://www.cairo-lang.org/cairovm/) or read more in [the Cairo Book](https://book.cairo-lang.org/)!*
