#[derive(Drop, Debug)]
struct Number {
    value: u32,
}

impl U32IntoNumber of Into<u32, Number> {
    fn into(self: u32) -> Number {
        Number { value: self }
    }
}

fn main() {
    let int: u32 = 30;
    let num: Number = int.into();
    println!("{:?}", num);
}
