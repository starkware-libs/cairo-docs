fn function() {
    println!("called `function()`");
}

mod cool {
    pub fn function() {
        println!("called `cool::function()`");
    }
}

mod my {
    fn function() {
        println!("called `my::function()`");
    }

    mod cool {
        pub fn function() {
            println!("called `my::cool::function()`");
        }
    }

    pub fn indirect_call() {
        // Let's access all the functions named `function` from this scope!
        print!("called `my::indirect_call()`, that\n> ");

        function();

        // We can also access another module inside `my`:
        cool::function();

        // The `super` keyword refers to the parent scope (outside the `my` module).
        super::function();
    }
}

fn main() {
    my::indirect_call();
}
