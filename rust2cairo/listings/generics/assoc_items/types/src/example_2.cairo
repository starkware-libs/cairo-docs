#[derive(Drop)]
struct Container {
    first: i32,
    last: i32,
}

// A trait which checks if 2 items are stored inside of container.
// Also retrieves first or last value.
trait Contains<T> {
    // Define generic types here which methods will be able to utilize.
    type A;
    type B;

    fn contains(self: @T, a: @Self::A, b: @Self::B) -> bool;
    fn first(self: @T) -> i32;
    fn last(self: @T) -> i32;
}

impl ContainerImpl of Contains<Container> {
    // Specify what types `A` and `B` are. If the `input` type
    // is `Container{first: i32, last: i32}`, the `output` types are determined
    // as `i32` and `i32`.
    type A = i32;
    type B = i32;

    // `@Self::A` and `@Self::B` are also valid here.
    fn contains(self: @Container, a: @i32, b: @i32) -> bool {
        self.first == a && self.last == b
    }

    // Grab the first number.
    fn first(self: @Container) -> i32 {
        *self.first
    }

    // Grab the last number.
    fn last(self: @Container) -> i32 {
        *self.last
    }
}

fn difference<T, +Contains<T>>(container: @T) -> i32 {
    container.last() - container.first()
}

fn main() {
    let number_1: i32 = 3;
    let number_2: i32 = 10;

    let container = Container { first: number_1, last: number_2 };

    println!(
        "Does container contain {} and {}: {}",
        number_1,
        number_2,
        container.contains(@number_1, @number_2),
    );
    println!("First number: {}", container.first());
    println!("Last number: {}", container.last());

    println!("The difference is: {}", difference(@container));
}
