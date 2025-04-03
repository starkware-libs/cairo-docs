# Box and Memory Segments

Values in Cairo are stored in a memory segment called the _execution segment_ by default. Values can be _boxed_
(allocated in the boxed segment) by creating a `Box<T>`. A box is a smart pointer that provides a way to store a value of type `T` in
Cairo VM's _boxed_ segment, leaving only a pointer in the execution segment.

The main purposes of boxes are to:

- Store values of arbitrary size while maintaining a fixed-size pointer
- Enable recursive types that would otherwise have infinite size
- Move large data structures efficiently by passing pointers instead of copying values

Boxed values can be accessed using the `unbox()` method or through the `Deref` trait, which retrieves the value from the boxed segment.

```cairo
{{#include ../../listings/core/box/src/lib.cairo}}
```

### Working with Recursive Types

One of the most important use cases for `Box<T>` is enabling recursive types. Without boxing, recursive types would have infinite size - as demonstrated in the [Linked List example][linked-list example].

[linked-list example]: ../custom_types/enum/testcase_linked_list.md
