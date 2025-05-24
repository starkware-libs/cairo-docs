mod deeply {
    pub mod nested {
        pub fn my_first_function() {
            println!("called `deeply::nested::my_first_function()`");
        }
        pub fn my_second_function() {
            println!("called `deeply::nested::my_second_function()`");
        }

        pub struct AndAType {}
    }
}

#[allow(unused_imports)]
//ANCHOR:main
use crate::deeply::nested::{my_first_function, my_second_function, AndAType};

fn main() {
    my_first_function();
}
//ANCHOR:main


