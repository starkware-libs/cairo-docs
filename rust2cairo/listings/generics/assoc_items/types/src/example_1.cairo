// `A` and `B` are defined in the trait via the `type` keyword.
// (Note: `type` in this context is different from `type` when used for
// aliases).
trait Contains<T> {
    type A;
    type B;

    // Updated syntax to refer to these new types generically.
    fn contains(self: @T, a: @Self::A, b: @Self::B) -> bool;
}

