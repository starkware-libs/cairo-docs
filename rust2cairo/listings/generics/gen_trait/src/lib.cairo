// Non-copyable types
#[derive(Drop)]
struct Empty {}

#[derive(Drop)]
struct Null {}

// A trait generic over `T, U`.
trait DoubleDrop<T, U> {
    // Define a method on the caller type which takes an
    // additional single parameter `U` and does nothing with it.
    fn double_drop(self: T, _x: U);
}

// Implement `DoubleDrop<T>` for any generic parameter `T` and
// caller `U`.
impl DoubleDropImpl<T, U, +Drop<T>, +Drop<U>> of DoubleDrop<T, U> {
    // This method takes ownership of both passed arguments,
    // deallocating both.
    fn double_drop(self: T, _x: U) {}
}

fn main() {
    let empty = Empty {};
    let null = Empty {};

    // Move `empty` and `null` and drop them.
    empty.double_drop(null);
    // empty.double_drop(null);
// null.double_drop(empty);
// ^ TODO: Try uncommenting these lines.
}
