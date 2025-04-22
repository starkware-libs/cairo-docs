use core::dict::Felt252Dict;

fn call(number: felt252) -> ByteArray {
    if number == 7981364 {
        return "We're sorry, the call cannot be completed as dialed. Please hang up and try again.";
    } else if number == 6457689 {
        return "Hello, this is Mr. Awesome's Pizza. My name is Fred. What can I get for you today?";
    } else {
        return "Hi! Who is this again?";
    }
}

fn main() {
    let mut contacts: Felt252Dict<felt252> = Default::default();

    // Insert values for different keys
    contacts.insert('Daniel', 7981364);
    contacts.insert('Ashley', 6457689);
    contacts.insert('Katie', 4358291);
    contacts.insert('Robert', 9561745);

    // Get a value and match on it
    let number = contacts.get('Daniel');
    println!("{}", call(number));

    // Insert a new value for an existing key
    contacts.insert('Daniel', 1646743);

    // Keys not in the dict return the default value - here, 0
    let number = contacts.get('Brandon');
    println!("Brandon's number is {}", number);
}
