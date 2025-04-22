# for loops

## for and range

The `for in` construct can be used to iterate through an `Iterator`.
One of the easiest ways to create an iterator is to use the range
notation `a..b`. This yields values from `a` (inclusive) to `b`
(exclusive) in steps of one.

Let's write FizzBuzz using `for` instead of `while`.

```cairo,editable
{{#include ../../listings/flow_control/for_and_range/src/lib.cairo}}
```

Alternatively, `a..=b` can be used for a range that is inclusive on both ends.
The above can be written as:

```cairo,editable
{{#include ../../listings/flow_control/for_and_range_incl/src/lib.cairo}}
```

## for and iterators

The `for in` construct is able to interact with an `Iterator` in several ways.
As discussed in the section on the [Iterator][iter] trait, by default the `for`
loop will apply the `into_iter` function to the collection. However, this is
not the only means of converting collections into iterators.

`into_iter` consumes the collection so that on each iteration the exact
data is provided. Once the collection has been consumed it is no longer
available for reuse as it has been 'moved' within the loop.

<!-- TODO(update): add `iter` example -->
<!-- `into_iter` and `iter` handle the conversion of a collection
into an iterator in different ways, by providing different views on the data
within. -->

<!-- - `iter` - This takes a [snapshot] of each element of the collection through each iteration.
  Thus leaving the collection untouched and available for reuse after the loop.

```cairo,editable
{{#include ../../listings/flow_control/for_and_iter/src/lib.cairo}}
``` -->

- `into_iter` - This consumes the collection so that on each iteration the exact
  data is provided. Once the collection has been consumed it is no longer
  available for reuse as it has been 'moved' within the loop.

```cairo,editable
{{#include ../../listings/flow_control/for_and_into_iter/src/lib.cairo}}
```

> Note: The syntax `for elem in collection` is equivalent to `for elem in collection.into_iter()` and requires the `IntoIter` trait to be implemented for the collection.

In the above snippets note the type of `match` branch, that is the key
difference in the types of iteration. The difference in type then of course
implies differing actions that are able to be performed.

### See also:

[Iterator][iter]

[iter]: ../trait/iter.md
[snapshot]: ../scope/retaining_ownership/snapshots.md
