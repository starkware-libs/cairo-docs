# range

Range and iteration utilities.
This module provides functionality for creating and iterating over ranges of values.
A range represents an interval of values from a start point to an end point.
# Range Operator Forms

There is currently only a single range operator form: `start..end`, representing a range from
`start` (inclusive) to `end` (exclusive).

Fully qualified path: [core](./core.md)::[ops](./core-ops.md)::[range](./core-ops-range.md)


[Structs](./core-ops-range-structs.md)
 ---
| | |
|:---|:---|
| [Range](./core-ops-range-Range.md) | A (half-open) range bounded inclusively below and exclusively above ( `start..end` ). The range `start..end`  contains all values with `start <= x < end` . It is empty if `start >= end` .[...](./core-ops-range-Range.md) |
| [RangeInclusive](./core-ops-range-RangeInclusive.md) | Represents the range start, end .[...](./core-ops-range-RangeInclusive.md) |
| [RangeInclusiveIterator](./core-ops-range-RangeInclusiveIterator.md) | [...](./core-ops-range-RangeInclusiveIterator.md) |
| [RangeIterator](./core-ops-range-RangeIterator.md) | Represents an iterator located at `cur` , whose end is `end`  ( `cur <= end` ).[...](./core-ops-range-RangeIterator.md) |

[Traits](./core-ops-range-traits.md)
 ---
| | |
|:---|:---|
| [RangeInclusiveTrait](./core-ops-range-RangeInclusiveTrait.md) | [...](./core-ops-range-RangeInclusiveTrait.md) |
| [RangeTrait](./core-ops-range-RangeTrait.md) | [...](./core-ops-range-RangeTrait.md) |
