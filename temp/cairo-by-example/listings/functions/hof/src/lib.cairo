fn is_odd(n: u32) -> bool {
    n % 2 == 1
}

fn main() {
    println!("Find the sum of all the squared odd numbers under 1000");
    let upper = 1000;

    // Imperative approach
    // Declare accumulator variable
    let mut acc = 0_u32;
    // Iterate: 0, 1, 2, ... to infinity
    let mut n = 0_u32;
    loop {
        // Square the number
        let n_squared = n * n;

        if n_squared >= upper {
            // Break loop if exceeded the upper limit
            break;
        } else if is_odd(n_squared) {
            // Accumulate value, if it's odd
            acc += n_squared;
        }
        n += 1;
    };
    println!("imperative style: {}", acc);

    // Assumption: we can use the range (0..1000) because we know 1000^2 > 1000
    let sum_of_squared_odd_numbers = (0_usize..1000)
        .into_iter()
        .map(|n| n * n) // Square all numbers
        .filter(|n_squared| *n_squared < upper) // Take only those under 1000
        .filter(|n_squared| is_odd(*n_squared)) // Take only odd numbers
        .sum(); // Sum them all

    println!("functional style: {}", sum_of_squared_odd_numbers);
}
