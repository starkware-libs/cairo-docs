/// A human being is represented here
#[derive(Drop)]
pub struct Person {
    /// A person must have a name, no matter how much Juliet may hate it
    name: ByteArray,
}

#[generate_trait]
impl PersonImpl of PersonTrait {
    /// Creates a person with the given name.
    ///
    /// # Examples
    ///
    /// ```
    /// // You can have cairo code between fences inside the comments
    /// use doc::Person;
    /// let person = PersonTrait::new("name");
    /// ```
    fn new(name: ByteArray) -> Person {
        Person { name: name }
    }

    /// Gives a friendly hello!
    ///
    /// Says "Hello, [name](Person::name)" to the `Person` it is called on.
    fn hello(self: @Person) {
        println!("Hello, {}!", self.name);
    }
}

fn main() {
    let john = PersonTrait::new("John");

    john.hello();
}
