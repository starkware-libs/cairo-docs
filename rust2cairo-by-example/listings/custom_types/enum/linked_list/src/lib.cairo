use List::{Cons, Nil};

#[derive(Drop)]
enum List {
    // Cons: Tuple struct that wraps an element and a pointer to the next node
    Cons: (u32, Box<List>),
    // Nil: A node that signifies the end of the linked list
    Nil,
}

// Methods can be attached to an enum through a trait implementation
trait ListTrait {
    fn new() -> List;
    fn prepend(self: List, elem: u32) -> List;
    fn len(self: @List) -> u32;
    fn stringify(self: @List) -> ByteArray;
}

impl ListImpl of ListTrait {
    // Create an empty list
    fn new() -> List {
        // `Nil` has type `List`
        Nil
    }

    // Consume a list, and return the same list with a new element at its front
    fn prepend(self: List, elem: u32) -> List {
        // `Cons` also has type List
        Cons((elem, BoxTrait::new(self)))
    }

    // Return the length of the list
    fn len(self: @List) -> u32 {
        // `self` has to be matched, because the behavior of this method
        // depends on the variant of `self`
        match self {
            Cons((_, tail)) => 1 + (tail.as_snapshot().unbox()).len(),
            Nil => 0,
        }
    }

    // Return representation of the list as a string
    fn stringify(self: @List) -> ByteArray {
        match self {
            Cons((
                head, tail,
            )) => {
                let head_str = head.into();
                let tail_str = format!("{}", (tail.as_snapshot().unbox()).stringify());
                format!("{}, {}", head_str, tail_str)
            },
            Nil => { format!("Nil") },
        }
    }
}

fn main() {
    // Create an empty linked list
    let mut list = ListTrait::new();

    // Prepend some elements
    list = list.prepend(1);
    list = list.prepend(2);
    list = list.prepend(3);

    // Show the final state of the list
    println!("linked list has length: {}", list.len());
    println!("{}", list.stringify());
}
