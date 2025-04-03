# Expressions

A Cairo program is (mostly) made up of a series of statements:

```cairo,editable
fn main() {
    // statement
    // statement
    // statement
}
```

There are a few kinds of statements in Cairo. The most common two are declaring
a variable binding, and using a `;` with an expression:

```cairo,editable
{{#include ../listings/expression_1/src/lib.cairo}}
```

Blocks are expressions too, so they can be used as values in
assignments. The last expression in the block will be assigned to the
place expression such as a local variable. However, if the last expression of the block ends with a
semicolon, the return value will be `()`.

```cairo,editable
{{#include ../listings/expression_2/src/lib.cairo}}
```
