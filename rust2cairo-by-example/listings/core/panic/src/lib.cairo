// Re-implementation of integer division (/)
fn division(dividend: i32, divisor: i32) -> i32 {
    if divisor == 0 {
        // Division by zero triggers a panic
        panic!("division by zero")
    } else {
        dividend / divisor
    }
}

// The `main` task
fn main() {
    // This operation will trigger a failure
    division(3, 0);

    println!("This point won't be reached!");
}
