//ANCHOR:intro
fn next_birthday(current_age: Option<u8>) -> Option<ByteArray> {
    // If `current_age` is `None`, this returns `None`.
    // If `current_age` is `Some`, the inner `u8` value + 1
    // gets assigned to `next_age`
    let next_age: u8 = current_age? + 1;
    Option::Some(format!("Next year I will be {}", next_age))
}
//ANCHOR_END:intro

//ANCHOR:main
#[derive(Copy, Drop)]
struct Person {
    job: Option<Job>,
}

#[derive(Drop, Clone, Copy)]
struct Job {
    phone_number: Option<PhoneNumber>,
}

#[derive(Drop, Clone, Copy)]
struct PhoneNumber {
    area_code: Option<u8>,
    number: u32,
}

#[generate_trait]
impl PersonImpl of PersonTrait {
    // Gets the area code of the phone number of the person's job, if it exists.
    fn work_phone_area_code(self: @Person) -> Option<u8> {
        // This would need many nested `match` statements without the `?` operator.
        // It would take a lot more code - try writing it yourself and see which
        // is easier.
        (*self).job?.phone_number?.area_code
    }
}

fn main() {
    let p = Person {
        job: Option::Some(
            Job {
                phone_number: Option::Some(
                    PhoneNumber { area_code: Option::Some(61), number: 439222222 },
                ),
            },
        ),
    };

    assert!(p.work_phone_area_code() == Option::Some(61));
}
//ANCHOR_END:main


