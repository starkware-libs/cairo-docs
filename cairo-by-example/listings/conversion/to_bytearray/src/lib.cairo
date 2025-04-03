use core::fmt;

#[derive(Drop)]
struct Circle {
    radius: i32,
}

impl CircleDisplay of fmt::Display<Circle> {
    fn fmt(self: @Circle, ref f: fmt::Formatter) -> Result<(), fmt::Error> {
        write!(f, "Circle of radius {}", self.radius)
    }
}

fn main() {
    let circle = Circle { radius: 6 };
    let circle_str: ByteArray = format!("{}", circle);
    println!("{}", circle_str);
}
