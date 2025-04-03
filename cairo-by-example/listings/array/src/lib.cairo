fn main() {
    // Initialize an empty array
    let mut arr = array![];

    // Append elements to the array
    arr.append(1);
    arr.append(2);
    arr.append(3);

    // Indexing starts at 0.
    println!("First element of the array: {}", *arr[0]);
    println!("Second element of the array: {}", *arr[1]);

    // `len()` returns the number of elements in the array.
    println!("Number of elements in the array: {}", arr.len());

    // A span is a snapshot of the array at a certain state.
    let span = arr.span();

    // `pop_front()` removes the first element from the array.
    let _ = arr.pop_front();

    // But the span is not affected by the pop: it has the same state as when the snapshot was
    // taken.
    println!("First element in span: {}", *span[0]);

    // Fixed-size array type
    let xs: [u32; 3] = [1, 2, 3];

    // All elements can be initialized to the same value.
    let ys: [u32; 3] = [0; 3];

    println!("xs: {:?}", xs);
    println!("ys: {:?}", ys);

    // Fixed-size arrays can be converted to spans for operations.
    println!("ys first element: {}", *xs.span()[0]);
}
