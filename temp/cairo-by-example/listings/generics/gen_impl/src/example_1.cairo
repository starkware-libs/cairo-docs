struct S {} // Concrete type `S`

trait T {} // Concrete trait `T`
trait GenericValTrait<T> {} // Generic trait `GenericValTrait`

// impl of GenericVal where we explicitly specify type parameters:
impl GenericValU32 of GenericValTrait<u32> {} // Specify `u32`
impl GenericValS of GenericValTrait<S> {} // Specify `S` as defined above

// `<T>` Must precede the type to remain generic
impl GenericValImpl<T> of GenericValTrait<T> {}
