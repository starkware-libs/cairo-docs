// A trait which implements the print marker: `{:?}`.
use core::fmt::Debug;

trait HasArea<T> {
    fn area(self: @T) -> u64;
}

#[derive(Debug, Drop)]
struct Rectangle {
    length: u64,
    height: u64,
}

#[derive(Drop)]
struct Triangle {
    length: u64,
    height: u64,
}

impl RectangleArea of HasArea<Rectangle> {
    fn area(self: @Rectangle) -> u64 {
        *self.length * *self.height
    }
}

// The generic `T` must implement `Debug`. Regardless
// of the type, this will work properly.
fn print_debug<T, +Debug<T>>(t: @T) {
    println!("{:?}", t);
}

// `T` must implement `HasArea`. Any type which meets
// the bound can access `HasArea`'s function `area`.
fn area<T, +HasArea<T>>(t: @T) -> u64 {
    HasArea::area(t)
}

fn main() {
    let rectangle = Rectangle { length: 3, height: 4 };
    let _triangle = Triangle { length: 3, height: 4 };

    print_debug(@rectangle);
    println!("Area: {}", area(@rectangle));
    //print_debug(@_triangle);
//println!("Area: {}", area(@_triangle));
// ^ TODO: Try uncommenting these.
// | Error: Does not implement either `Debug` or `HasArea`.
}
