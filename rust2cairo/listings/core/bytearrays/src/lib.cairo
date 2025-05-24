fn main() {
    let pangram: ByteArray = "the quick brown fox jumps over the lazy dog";
    println!("Pangram: {}", pangram);

    // This is a simplified example showing iteration
    let mut chars = pangram.clone().into_iter();
    for c in chars {
        println!("ASCII: 0x{:x}", c);
    }

    // ByteArray can be concatenated using the + operator
    let alice: ByteArray = "I like dogs";
    let bob: ByteArray = "I like " + "cats";

    println!("Alice says: {}", alice);
    println!("Bob says: {}", bob);
}
