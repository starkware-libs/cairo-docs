//TAG: does_not_compile

use core::dict::Felt252Dict;

#[derive(Drop)]
struct ToDrop {}

struct ToDestruct {
    inner: Felt252Dict<u8>,
}

fn main() {
    let _to_drop = ToDrop {};
    let _to_destruct = ToDestruct { inner: Default::default() };
    // TODO: modify the definition of ToDestruct to fix the error.
}
