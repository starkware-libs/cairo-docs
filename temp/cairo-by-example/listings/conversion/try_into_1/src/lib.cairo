#[derive(Copy, Drop, Debug)]
struct EvenNumber {
    value: u32,
}

impl U32IntoEvenNumber of TryInto<u32, EvenNumber> {
    fn try_into(self: u32) -> Option<EvenNumber> {
        if self % 2 == 0 {
            Option::Some(EvenNumber { value: self })
        } else {
            Option::None
        }
    }
}

fn main() {
    // Direct conversion with TryInto
    let even: Option<EvenNumber> = 8_u32.try_into();
    println!("{:?}", even);

    let odd: Option<EvenNumber> = 5_u32.try_into();
    println!("{:?}", odd);
}
