// A phantom struct which is generic over `A` and `B`.
#[phantom]
struct PhantomStruct<A, B> {}

trait PhantomTrait<P> {
    fn type_of_a() -> ByteArray;
    fn type_of_b() -> ByteArray;
}

impl ImplU256U128 of PhantomTrait<PhantomStruct<u256, u128>> {
    fn type_of_a() -> ByteArray {
        format!("u256")
    }
    fn type_of_b() -> ByteArray {
        format!("u128")
    }
}

impl ImplI128I32 of PhantomTrait<PhantomStruct<i128, i32>> {
    fn type_of_a() -> ByteArray {
        format!("i128")
    }
    fn type_of_b() -> ByteArray {
        format!("i32")
    }
}

fn main() {
    // The PhantomStruct is never instantiated: it's just used for type checking.
    let a1 = ImplU256U128::type_of_a();
    let b1 = ImplU256U128::type_of_b();
    println!("a: {}", a1);
    println!("b: {}", b1);

    let a2 = ImplI128I32::type_of_a();
    let b2 = ImplI128I32::type_of_b();
    println!("a: {}", a2);
    println!("b: {}", b2);
    // let my_phantom_struct: PhantomStruct<u256, u128> = PhantomStruct {};
// Try uncommenting the above line and see what happens.
}
