// importing common module.
mod common;

#[test]
fn test_add() {
    // using common code.
    common::setup();
    assert(adder::add(3, 2) == 5, 'addition failed');
}
