//TAG: tests_fail

//ANCHOR: add
// Basic add example
fn add(a: u32, b: u32) -> u32 {
    a + b
}

// This is a really bad adding function, its purpose is to fail in this
// example.
fn bad_add(a: u32, b: u32) -> u32 {
    a - b
}

#[cfg(test)]
mod add_tests {
    // Note this useful idiom: importing names from outer (for mod tests) scope.
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(1, 2), 3);
    }

    #[test]
    fn test_bad_add() {
        // This assert would fire and test will fail.
        // Please note, that private functions can be tested too!
        assert_eq!(bad_add(1, 2), 3);
    }
}
// ANCHOR_END: add

// ANCHOR: divide
fn divide_non_zero_result(a: u32, b: u32) -> u32 {
    if b == 0 {
        panic!("Divide-by-zero error")
    } else if a < b {
        panic!("Divide result is zero")
    }
    a / b
}

#[cfg(test)]
mod divide_tests {
    use super::*;

    #[test]
    fn test_divide() {
        assert_eq!(divide_non_zero_result(10, 2), 5);
    }

    #[test]
    #[should_panic]
    fn test_any_panic() {
        divide_non_zero_result(1, 0);
    }

    #[test]
    #[should_panic(expected: "Divide result is zero")]
    fn test_specific_panic() {
        divide_non_zero_result(1, 10);
    }
}
// ANCHOR_END: divide

// ANCHOR: ignore
fn add_two(a: u32, b: u32) -> u32 {
    a + b
}

#[cfg(test)]
mod ignore_tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add_two(2, 2), 4);
    }

    #[test]
    fn test_add_hundred() {
        assert_eq!(add_two(100, 2), 102);
        assert_eq!(add_two(2, 100), 102);
    }

    #[test]
    #[ignore]
    fn ignored_test() {
        assert_eq!(add_two(0, 0), 0);
    }
}
// ANCHOR_END: ignore


