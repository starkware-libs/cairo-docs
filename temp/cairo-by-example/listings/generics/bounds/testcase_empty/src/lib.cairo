#[derive(Drop)]
struct Cardinal {}

#[derive(Drop)]
struct BlueJay {}

#[derive(Drop)]
struct Turkey {}

trait Red<T> {}
trait Blue<T> {}

impl CardinalRed of Red<Cardinal> {}
impl BlueJayBlue of Blue<BlueJay> {}

// These functions are only valid for types which implement these
// traits. The fact that the traits are empty is irrelevant.
fn red<T, +Red<T>>(t: @T) -> ByteArray {
    "red"
}
fn blue<T, +Blue<T>>(t: @T) -> ByteArray {
    "blue"
}

fn main() {
    let cardinal = Cardinal {};
    let blue_jay = BlueJay {};
    let _turkey = Turkey {};

    // `red()` won't work on a blue jay nor vice versa
    // because of the bounds.
    println!("A cardinal is {}", red(@cardinal));
    println!("A blue jay is {}", blue(@blue_jay));
    //println!("A turkey is {}", red(@_turkey));
// ^ TODO: Try uncommenting this line.
}
