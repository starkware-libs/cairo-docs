#[derive(Drop)]
struct Book {
    author: ByteArray,
    title: ByteArray,
    year: u32,
}

// This function takes a snapshot of a book
fn borrow_book(book: @Book) {
    println!("I took a snapshot of {} - {} edition", book.title, book.year);
}

// This function takes a reference to a book and changes `year` to 2014
fn new_edition(ref book: Book) {
    book.year = 2014;
    println!("I modified {} - {} edition", book.title, book.year);
}

fn main() {
    // Create a Book
    let mut book = Book { author: "Douglas Hofstadter", title: "Godel, Escher, Bach", year: 1979 };

    // Take a snapshot of the book
    borrow_book(@book);

    // Pass a reference to modify the book
    new_edition(ref book);

    // We can still use book here since ownership was returned
    println!("Book is now from {}", book.year);
}
