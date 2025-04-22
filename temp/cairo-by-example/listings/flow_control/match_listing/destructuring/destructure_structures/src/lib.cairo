#[derive(Copy, Drop)]
struct Foo {
    x: (u32, u32),
    y: u32,
}

#[derive(Drop)]
struct Bar {
    foo: Foo,
}


fn main() {
    // Try changing the values in the struct to see what happens
    let _foo = Foo { x: (1, 2), y: 3 };

    let faa = Foo { x: (1, 2), y: 3 };

    // You do not need a match block to destructure structs:
    let Foo { x: x0, y: y0 } = faa;
    println!("Outside: x0 = {x0:?}, y0 = {y0}");

    // Destructuring works with nested structs as well:
    let bar = Bar { foo: faa };
    let Bar { foo: Foo { x: nested_x, y: nested_y } } = bar;
    println!("Nested: nested_x = {nested_x:?}, nested_y = {nested_y:?}");
}
