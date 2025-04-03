mod my {
    // A public struct with a public field of generic type `T`
    #[derive(Drop)]
    pub struct OpenBox<T> {
        pub contents: T,
    }

    // A public struct with a private field of generic type `T`
    #[derive(Drop)]
    pub struct ClosedBox<T> {
        contents: T,
    }

    #[generate_trait]
    pub impl ClosedBoxImpl<T> of ClosedBoxTrait<T> {
        // Trait methods are public
        fn new(contents: T) -> ClosedBox<T> {
            ClosedBox { contents: contents }
        }
    }
}

fn main() {
    // Public structs with public fields can be constructed as usual
    let open_box = my::OpenBox::<ByteArray> { contents: "public information" };

    // and their fields can be normally accessed.
    println!("The open box contains: {}", open_box.contents);

    // Public structs with private fields cannot be constructed using field names.
    // Error! `ClosedBox` has private fields
    // let closed_box = my::ClosedBox::<ByteArray> { contents: "classified information" };
    // TODO ^ Try uncommenting this line

    // However, structs with private fields can be created using
    // public constructors
    let _closed_box: my::ClosedBox<ByteArray> = my::ClosedBoxTrait::new("classified information");
    // and the private fields of a public struct cannot be accessed.
// Error! The `contents` field is private
// println!("The closed box contains: {}", _closed_box.contents);
// TODO ^ Try uncommenting this line
}
