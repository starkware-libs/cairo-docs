#[derive(Drop)]
struct Sheep {
    naked: bool,
    name: ByteArray,
}

trait Animal<T> {
    // Associated function signature; `T` refers to the implementor type
    fn new(name: ByteArray) -> T;

    // Method signatures; these will return a ByteArray
    fn name(self: @T) -> ByteArray;
    fn noise(self: @T) -> ByteArray;

    // Traits can provide default method definitions
    fn talk(self: @T) {
        println!("{} says {}", Self::name(self), Self::noise(self));
    }
}


// The `#[generate_trait]` attribute is used to automatically generate a trait from the definition
// of an impl.
// This pattern is often used to define methods on a type.
#[generate_trait]
impl SheepImpl of SheepTrait {
    fn is_naked(self: @Sheep) -> bool {
        *self.naked
    }

    fn shear(ref self: Sheep) {
        if self.is_naked() {
            // Implementor methods can use the implementor's trait methods
            println!("{} is already naked...", self.name());
        } else {
            println!("{} gets a haircut!", self.name);
            self.naked = true;
        }
    }
}

// Implement the `Animal` trait for `Sheep`
impl SheepAnimal of Animal<Sheep> {
    // `T` is the implementor type: `Sheep`
    fn new(name: ByteArray) -> Sheep {
        Sheep { name: name, naked: false }
    }

    fn name(self: @Sheep) -> ByteArray {
        self.name.clone()
    }

    fn noise(self: @Sheep) -> ByteArray {
        if self.is_naked() {
            "baaaaah?" // Questioning
        } else {
            "baaaaah!" // Confident
        }
    }

    // Default trait methods can be overridden
    fn talk(self: @Sheep) {
        // For example, we can add some quiet contemplation
        println!("{} pauses briefly... {}", self.name, self.noise());
    }
}

fn main() {
    // Type annotation is necessary in this case
    let mut dolly: Sheep = Animal::new("Dolly");
    // TODO ^ Try removing the type annotations

    dolly.talk();
    dolly.shear();
    dolly.talk();
}
