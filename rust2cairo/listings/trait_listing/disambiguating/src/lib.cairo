trait UsernameWidget<T> {
    // Get the selected username out of this widget
    fn get(self: @T) -> ByteArray;
}

trait AgeWidget<T> {
    // Get the selected age out of this widget
    fn get(self: @T) -> u8;
}

// A form with both a UsernameWidget and an AgeWidget
#[derive(Drop)]
struct Form {
    username: ByteArray,
    age: u8,
}

impl FormUsername of UsernameWidget<Form> {
    fn get(self: @Form) -> ByteArray {
        self.username.clone()
    }
}

impl FormAge of AgeWidget<Form> {
    fn get(self: @Form) -> u8 {
        *self.age
    }
}

fn main() {
    let form = Form { username: "caironaute", age: 28 };

    // If you uncomment this line, you'll get an error saying
    // "Ambiguous method call". Because, after all, there are multiple methods
    // named `get`.
    // println!("{}", form.get());

    let username = UsernameWidget::get(@form);
    assert!(username == "caironaute");
    let age = AgeWidget::get(@form);
    assert!(age == 28);
}
