use core::dict::Felt252Dict;

#[derive(Destruct)]
struct DestructibleType {
    name: ByteArray,
    dict: Felt252Dict<u64>,
}
// Try to derive `Drop` instead of `Destruct` and see what happens.

fn main() {
    let _a = DestructibleType { name: "a", dict: Default::default() };

    // block A
    {
        let _b = DestructibleType { name: "b", dict: Default::default() };

        // block B
        {
            let _c = DestructibleType { name: "c", dict: Default::default() };
            let _d = DestructibleType { name: "d", dict: Default::default() };

            println!("Exiting block B");
        }
        println!("Just exited block B");

        println!("Exiting block A");
    }
    println!("Just exited block A");

    println!("end of the main function");
}
