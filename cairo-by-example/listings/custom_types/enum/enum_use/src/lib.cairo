#[derive(Drop)]
enum Stage {
    Beginner,
    Advanced,
}

#[derive(Drop)]
enum Role {
    Student,
    Teacher,
}

// Explicitly `use` each name so they are available without
// manual scoping.
use Stage::{Beginner, Advanced};

fn main() {
    // Equivalent to `Stage::Beginner`.
    let stage = Beginner;

    match stage {
        // Note the lack of scoping because of the explicit `use` above.
        Beginner => println!("Beginners are starting their learning journey!"),
        Advanced => println!("Advanced learners are mastering their subjects..."),
    }
}
