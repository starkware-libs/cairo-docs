// This function only gets compiled if the feature "poseidon" is enabled
#[cfg(feature: "poseidon")]
fn which_hash_function() {
    println!("You are hashing with Poseidon!");
}

// This function only gets compiled if the feature "poseidon" is not enabled
#[cfg(not(feature: "poseidon"))]
fn which_hash_function() {
    println!("You are **not** hashing with Poseidon!");
}

fn main() {
    which_hash_function();
}
