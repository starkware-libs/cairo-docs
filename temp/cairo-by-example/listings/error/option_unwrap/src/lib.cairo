// The adult has seen it all, and can handle any drink well.
// All drinks are handled explicitly using `match`.
fn give_adult(drink: Option<ByteArray>) {
    // Specify a course of action for each case.
    match drink {
        Option::Some(inner) => println!("{}? How nice.", inner),
        Option::None => println!("No drink? Oh well."),
    }
}

// Others will `panic` before drinking sugary drinks.
// All drinks are handled implicitly using `unwrap`.
fn drink(drink: Option<ByteArray>) {
    // `unwrap` returns a `panic` when it receives a `None`.
    let inside = drink.unwrap();
    if inside == "lemonade" {
        panic!("AAAaaaaa!!!!")
    }

    println!("I love {}s!!!!!", inside);
}

fn main() {
    let water = Option::Some("water");
    let lemonade = Option::Some("lemonade");
    let void = Option::None;

    give_adult(water);
    give_adult(lemonade);
    give_adult(void);

    let coffee = Option::Some("coffee");
    let nothing = Option::None;

    drink(coffee);
    drink(nothing);
}
