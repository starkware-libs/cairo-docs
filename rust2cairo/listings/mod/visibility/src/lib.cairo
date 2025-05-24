// A module named `my_mod`
mod my_mod {
    // Items in modules default to private visibility.
    fn private_function() {
        println!("called `my_mod::private_function()`");
    }

    // Use the `pub` modifier to override default visibility.
    pub fn function() {
        println!("called `my_mod::function()`");
    }

    // Items can access other items in the same module,
    // even when private.
    pub fn indirect_access() {
        print!("called `my_mod::indirect_access()`, that\n> ");
        private_function();
    }

    // Modules can also be nested
    pub mod nested {
        pub fn function() {
            println!("called `my_mod::nested::function()`");
        }

        fn private_function() {
            println!("called `my_mod::nested::private_function()`");
        }

        // Functions declared using `pub(crate)` syntax are only visible
        // within the given crate.
        pub(crate) fn public_function_in_crate() {
            println!("called `my_mod::nested::public_function_in_crate()`");
        }
    }

    // pub(crate) makes functions visible only within the current crate
    pub(crate) fn public_function_in_crate() {
        println!("called `my_mod::public_function_in_crate()`");
    }

    // Nested modules follow the same rules for visibility
    mod private_nested {
        pub fn function() {
            println!("called `my_mod::private_nested::function()`");
        }

        // Private parent items will still restrict the visibility of a child item,
        // even if it is declared as visible within a bigger scope.
        pub(crate) fn restricted_function() {
            println!("called `my_mod::private_nested::restricted_function()`");
        }
    }
}

fn function() {
    println!("called `function()`");
}

fn main() {
    // Modules allow disambiguation between items that have the same name.
    function();
    my_mod::function();

    // Public items, including those inside nested modules, can be
    // accessed from outside the parent module.
    my_mod::indirect_access();
    my_mod::nested::function();

    // pub(crate) items can be called from anywhere in the same crate
    my_mod::public_function_in_crate();
    // Private items of a module cannot be directly accessed, even if
// nested in a public module:

    // Error! `private_function` is private
// my_mod::private_function();
// TODO ^ Try uncommenting this line

    // Error! `private_function` is private
// my_mod::nested::private_function();
// TODO ^ Try uncommenting this line

    // Error! `private_nested` is a private module
// my_mod::private_nested::function();
// TODO ^ Try uncommenting this line

    // Error! `private_nested` is a private module
// my_mod::private_nested::restricted_function();
// TODO ^ Try uncommenting this line
}
