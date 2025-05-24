//TAG: does_not_compile
fn main() {
    let names: Array<ByteArray> = array!["Bob", "Frank", "Ferris"];

    for name in names.into_iter() {
        if name == "Ferris" {
            println!("There is a caironaute among us!");
        } else {
            println!("Hello {}", name);
        }
    }

    println!("names: {:?}", names);
    // FIXME ^ Comment out this line
}
