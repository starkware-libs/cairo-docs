#[derive(Copy, Drop)]
struct Val {
    val: u64,
}

#[derive(Copy, Drop)]
struct GenVal<T> {
    gen_val: T,
}

// impl of Val
trait ValTrait {
    fn value(self: @Val) -> @u64;
}

impl ValImpl of ValTrait {
    fn value(self: @Val) -> @u64 {
        self.val
    }
}

// impl of GenVal for a generic type `T`
trait GenValTrait<T> {
    fn value(self: @GenVal<T>) -> @T;
}

impl GenValImpl<T> of GenValTrait<T> {
    fn value(self: @GenVal<T>) -> @T {
        self.gen_val
    }
}

fn main() {
    let x = Val { val: 3 };
    let y = GenVal { gen_val: 3_u32 };

    println!("{}, {}", x.value(), y.value());
}
