# Conversion

Cairo addresses conversion between types (i.e., integers, felt252, `struct` and `enum`)
by the use of [traits]. The generic
conversions will use the and [`Into`] and [`TryInto`] traits. However there are more
specific ones for the more common cases, in particular when converting to and
from `ByteArray`s.

[traits]: trait.md
[`TryInto`]: https://docs.swmansion.com/scarb/corelib/core-traits-TryInto.html
[`Into`]: https://docs.swmansion.com/scarb/corelib/core-traits-Into.html
