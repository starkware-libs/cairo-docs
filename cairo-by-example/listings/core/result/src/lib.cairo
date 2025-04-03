mod checked {
    use core::num::traits::Sqrt;

    // Mathematical "errors" we want to catch
    #[derive(Drop, Debug)]
    enum MathError {
        DivisionByZero,
        NegativeSquareRoot,
    }

    type MathResult = Result<u32, MathError>;

    pub fn div(x: u32, y: u32) -> MathResult {
        if y == 0 {
            // This operation would `fail`, instead let's return the reason of
            // the failure wrapped in `Err`
            Err(MathError::DivisionByZero)
        } else {
            // This operation is valid, return the result wrapped in `Ok`
            Ok(x / y)
        }
    }

    pub fn sqrt(x: u32) -> MathResult {
        match x {
            0 => Ok(0),
            _ => Ok(x.sqrt().into()),
        }
    }
}

// `op(x, y)` === `sqrt(x / y)`
pub fn op(x: u32, y: u32) -> u32 {
    // This is a two level match pyramid!
    match checked::div(x, y) {
        Err(why) => panic!("{:?}", why),
        Ok(ratio) => match checked::sqrt(ratio) {
            Err(why) => panic!("{:?}", why),
            Ok(sqrt) => sqrt,
        },
    }
}

pub fn main() {
    // Will this fail?
    println!("{}", op(1, 10));
}
