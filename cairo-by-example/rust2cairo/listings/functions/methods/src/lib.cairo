#[derive(Copy, Drop)]
struct Point {
    x: u64,
    y: u64,
}

// Implementation block, all `Point` associated functions & methods go in here
#[generate_trait]
impl PointImpl of PointTrait {
    // This is an "associated function" because this function is associated with
    // a particular type, that is, Point.
    //
    // Associated functions don't need to be called with an instance.
    // These functions are generally used like constructors.
    fn origin() -> Point {
        Point { x: 0, y: 0 }
    }

    // Another associated function, taking two arguments:
    fn new(x: u64, y: u64) -> Point {
        Point { x, y }
    }
}

#[derive(Copy, Drop)]
struct Rectangle {
    p1: Point,
    p2: Point,
}

#[generate_trait]
impl RectangleImpl of RectangleTrait {
    // This is a method
    // `self: @Rectangle` means we're taking a snapshot of the Rectangle instance. Because
    // `@Rectangle` is associated to the `self` keyword, it's the expected caller object.
    fn area(self: @Rectangle) -> u64 {
        // `self` gives access to the struct fields via the dot operator
        let Point { x: x1, y: y1 } = *self.p1;
        let Point { x: x2, y: y2 } = *self.p2;

        // Calculate absolute value using if/else since Cairo doesn't have abs()
        let width = if x1 >= x2 {
            x1 - x2
        } else {
            x2 - x1
        };
        let height = if y1 >= y2 {
            y1 - y2
        } else {
            y2 - y1
        };
        width * height
    }

    fn perimeter(self: @Rectangle) -> u64 {
        let Point { x: x1, y: y1 } = *self.p1;
        let Point { x: x2, y: y2 } = *self.p2;

        let width = if x1 >= x2 {
            x1 - x2
        } else {
            x2 - x1
        };
        let height = if y1 >= y2 {
            y1 - y2
        } else {
            y2 - y1
        };
        2 * (width + height)
    }

    // This method requires the caller object to be mutable
    // `ref self` means we're taking a reference to modify the Rectangle instance and return it to
    // the calling context.
    fn translate(ref self: Rectangle, x: u64, y: u64) {
        self.p1.x += x;
        self.p2.x += x;
        self.p1.y += y;
        self.p2.y += y;
    }
}

fn main() {
    let rectangle = Rectangle { // Associated functions are called using double colons
        p1: PointTrait::origin(), p2: PointTrait::new(3, 4),
    };

    // Methods are called using the dot operator
    // Note that the snapshot is implicitly passed
    println!("Rectangle perimeter: {}", rectangle.perimeter());
    println!("Rectangle area: {}", rectangle.area());

    let mut square = Rectangle { p1: PointTrait::origin(), p2: PointTrait::new(1, 1) };

    // Error! `rectangle` is immutable, but this method requires a mutable object
    // because `self` is taken by `ref`.
    // rectangle.translate(1, 0);
    // TODO ^ Try uncommenting this line

    // Okay! Mutable objects can call mutable methods
    square.translate(1, 1);
}
