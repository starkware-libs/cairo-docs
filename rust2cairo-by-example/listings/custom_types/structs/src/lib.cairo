#[derive(Drop, Debug)]
struct Person {
    name: ByteArray,
    age: u8,
}

// An empty struct
#[derive(Drop, Debug)]
struct Unit {}

// A struct with two fields
#[derive(Drop)]
struct Point {
    x: u32,
    y: u32,
}

// Structs can be reused as fields of another struct
#[derive(Drop)]
struct Rectangle {
    // A rectangle can be specified by where the top left and bottom right
    // corners are in space.
    top_left: Point,
    bottom_right: Point,
}

fn main() {
    // Create struct with field init shorthand
    let name: ByteArray = "Peter";
    let age = 27;
    let peter = Person { name, age };

    // Print debug struct
    println!("{:?}", peter);

    // Instantiate a `Point`
    let point: Point = Point { x: 5, y: 0 };
    let another_point: Point = Point { x: 10, y: 0 };

    // Access the fields of the point
    println!("point coordinates: ({}, {})", point.x, point.y);

    // Make a new point by using struct update syntax to use the fields of our
    // other one
    let bottom_right = Point { x: 10, ..another_point };

    // `bottom_right.y` will be the same as `another_point.y` because we used that field
    // from `another_point`
    println!("second point: ({}, {})", bottom_right.x, bottom_right.y);

    // Destructure the point using a `let` binding
    let Point { x: left_edge, y: top_edge } = point;

    let _rectangle = Rectangle {
        // struct instantiation is an expression too
        top_left: Point { x: left_edge, y: top_edge }, bottom_right: bottom_right,
    };

    // Instantiate a unit struct
    let _unit = Unit {};
}
