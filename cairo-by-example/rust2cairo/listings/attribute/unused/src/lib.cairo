// `#[allow(unused_imports)]` is an attribute that disables the `unused_imports` lint
use core::num::traits::ops::checked::CheckedAdd;
#[allow(unused_imports)]
use core::num::traits::ops::checked::CheckedSub;
use core::num::traits::ops::wrapping::WrappingMul;
// FIXME ^ Add an attribute to suppress the warning

fn main() {
    2_u8.checked_add(1).unwrap();
}
