// `Centimeters`, a tuple struct that can be equality-compared
#[derive(Copy, Drop, PartialEq)]
struct Centimeters {
    inner: u64,
}

// `Inches`, a tuple struct that can be printed
#[derive(Copy, Drop, Debug)]
struct Inches {
    inner: u64,
}

#[generate_trait]
impl InchesImpl of InchesTrait {
    fn to_centimeters(self: @Inches) -> Centimeters {
        let Inches { inner: inches } = *self;
        Centimeters {
            inner: inches * 254 / 100,
        } // Convert to centimeters (2.54 * 100 to avoid floats)
    }
}

// `Seconds`, a tuple struct with no additional attributes
#[derive(Drop)]
struct Seconds {
    inner: u64,
}

fn main() {
    let _one_second = Seconds { inner: 1 };

    // Error: `Seconds` can't be printed; it doesn't implement the `Debug` trait
    //println!("One second looks like: {:?}", _one_second);
    // TODO ^ Try uncommenting this line

    // Error: `Seconds` can't be compared; it doesn't implement the `PartialEq` trait
    //let _this_is_true = (_one_second == _one_second);
    // TODO ^ Try uncommenting this line

    let foot = Inches { inner: 12 };

    println!("One foot equals {:?}", foot);

    let meter = Centimeters { inner: 100 };

    let cmp: ByteArray = if foot.to_centimeters() == meter {
        "equal"
    } else {
        "not equal"
    };

    println!("One foot is {} to one meter.", cmp);
}
