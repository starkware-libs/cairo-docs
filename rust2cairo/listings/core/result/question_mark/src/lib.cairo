mod checked {
    use core::num::traits::Sqrt;

    #[derive(Drop)]
    pub enum MathError {
        DivisionByZero,
        NegativeSquareRoot,
    }

    pub type MathResult = Result<u32, MathError>;

    pub fn div(x: u32, y: u32) -> MathResult {
        if y == 0 {
            Err(MathError::DivisionByZero)
        } else {
            Ok(x / y)
        }
    }

    pub fn sqrt(x: u32) -> MathResult {
        match x {
            0 => Ok(0),
            _ => Ok(x.sqrt().into()),
        }
    }

    // Intermediate function
    pub fn op_(x: u32, y: u32) -> MathResult {
        // if `div` "fails", then `DivisionByZero` will be `return`ed
        let ratio = div(x, y)?;

        // if `sqrt` "fails", then `NegativeSquareRoot` will be `return`ed
        sqrt(ratio)
    }

    pub fn op(x: u32, y: u32) {
        match op_(x, y) {
            Err(why) => panic!(
                "{:?}",
                match why {
                    MathError::DivisionByZero => println!("division by zero"),
                    MathError::NegativeSquareRoot => println!("square root of negative number"),
                },
            ),
            Ok(value) => println!("{}", value),
        }
    }
}

fn main() {
    checked::op(1, 10);
}
