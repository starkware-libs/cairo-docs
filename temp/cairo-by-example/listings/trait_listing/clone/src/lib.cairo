// An empty unit struct
#[derive(Drop, Copy, Debug)]
struct Unit {}

// A tuple struct that implements the Clone trait
#[derive(Clone, Drop, Debug)]
struct Pair {
    first: Box<u32>,
    second: Box<u32>,
}

fn main() {
    // Instantiate `Unit`
    let unit = Unit {};
    // Copy `Unit`, there are no resources to move
    let copied_unit = unit;

    // Both `Unit`s can be used independently
    println!("original: {:?}", unit);
    println!("copy: {:?}", copied_unit);

    // Instantiate `Pair`
    let pair = Pair { first: BoxTrait::new(1), second: BoxTrait::new(2) };
    println!("original: {:?}", pair);

    // Move `pair` into `moved_pair`
    let moved_pair = pair;
    println!("moved: {:?}", moved_pair);

    // Error! `pair` has been moved
    // println!("original: {:?}", pair);
    // TODO ^ Try uncommenting this line

    // Clone `moved_pair` into `cloned_pair` (resources are included)
    let cloned_pair = moved_pair.clone();

    // Drop the moved original by moving it into a function that takes ownership
    let _d = |_x: Pair| {};
    _d(moved_pair);

    // Error! `moved_pair` has been moved
    // println!("moved and dropped: {:?}", moved_pair);
    // TODO ^ Try uncommenting this line

    // The result from .clone() can still be used!
    println!("clone: {:?}", cloned_pair);
}
