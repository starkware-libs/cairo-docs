#[derive(Copy, Drop, Debug)]
struct Point {
    x: u128,
    y: u128,
}

// A Rectangle can be specified by where its top left and bottom right
// corners are in space
#[derive(Copy, Drop, Debug)]
struct Rectangle {
    top_left: Point,
    bottom_right: Point,
}

fn origin() -> Point {
    Point { x: 0, y: 0 }
}

fn boxed_origin() -> Box<Point> {
    // Allocate this point in the boxed segment, and return a pointer to it
    BoxTrait::new(Point { x: 0, y: 0 })
}

fn main() {
    // Values in execution segment
    let point: Point = origin();
    let _rectangle: Rectangle = Rectangle {
        top_left: origin(), bottom_right: Point { x: 3, y: 4 },
    };

    // Boxed segment allocated rectangle
    let boxed_rectangle: Box<Rectangle> = BoxTrait::new(
        Rectangle { top_left: origin(), bottom_right: Point { x: 3, y: 4 } },
    );

    // The output of functions can be boxed
    let boxed_point: Box<Point> = BoxTrait::new(origin());

    // Double indirection
    let _box_in_a_box: Box<Box<Point>> = BoxTrait::new(boxed_origin());

    // Two ways to access boxed values:
    // 1. Using unbox()
    let unboxed_point: Point = boxed_point.unbox();
    // 2. Using deref() trait
    let _derefed_point: Point = boxed_point.deref();

    // Print some values to demonstrate
    println!("point: {:?}", point);
    println!("unboxed_point: {:?}", unboxed_point);
    println!("boxed_rectangle: {:?}", boxed_rectangle.unbox().top_left);
}
