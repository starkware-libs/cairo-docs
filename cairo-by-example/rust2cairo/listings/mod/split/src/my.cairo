// Similarly `mod inaccessible` and `mod nested` will locate the `nested.cairo`
// and `inaccessible.cairo` files and insert them here under their respective
// modules
mod inaccessible;
pub mod nested;

pub fn function() {
    println!("called `my::function()`");
}

fn private_function() {
    println!("called `my::private_function()`");
}

pub fn indirect_access() {
    println!("called `my::indirect_access()`, that");
    println!("> ");
    private_function();
}
