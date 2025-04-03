#[derive(Drop)]
struct Container {
    first: i32,
    last: i32,
}

// A trait which checks if 2 items `A` and `B` are stored inside of container `C`.
// Also retrieves first or last value.
trait Contains<C, A, B> {
    fn contains(self: @C, a: @A, b: @B) -> bool; // Explicitly requires `A` and `B`.
    fn first(self: @C) -> i32; // Doesn't explicitly require `A` or `B`.
    fn last(self: @C) -> i32; // Doesn't explicitly require `A` or `B`.
}

impl ContainsImpl of Contains<Container, i32, i32> {
    // True if the numbers stored are equal.
    fn contains(self: @Container, a: @i32, b: @i32) -> bool {
        (self.first == a) && (self.last == b)
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

// `C` contains `A` and `B`. In light of that, having to express `A` and
// `B` again is a nuisance.
fn difference<A, B, C, +Contains<C, A, B>>(container: @C) -> i32 {
    container.last() - container.first()
}

fn main() {
    let number_1 = 3;
    let number_2 = 10;

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
