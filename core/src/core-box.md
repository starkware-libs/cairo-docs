# box

`Box<T>` is a smart pointer that allows for:
- Storing values of arbitrary size while maintaining a fixed-size pointer
- Enabling recursive types that would otherwise have infinite size
- Moving large data structures efficiently by passing pointers instead of copying values
# Examples

Creating a new box with `BoxTrait::new`:
```cairo
let boxed = BoxTrait::new(42);
let unboxed = boxed.unbox();
```

Working with larger structures:
```cairo
let large_array = array![1, 2, 3, 4, 5];
let boxed_array = BoxTrait::new(large_array);
```

Creating a recursive data structure:
```cairo
#[derive(Copy, Drop, Debug)]
enum BinaryTree {
    Leaf: u32,
    Node: (u32, Box<BinaryTree>, Box<BinaryTree>)
}

let leaf = BinaryTree::Leaf(1);
let node = BinaryTree::Node((2, BoxTrait::new(leaf), BoxTrait::new(leaf)));
println!("{:?}", node);
```

NOTE: A `Box<T>` is a smart pointer type that provides a way to store a value of type `T` in
Cairo VM's boxed segment, leaving only a pointer in the execution segment.

Fully qualified path: [core](./core.md)::[box](./core-box.md)


[Traits](./core-box-traits.md)
 ---
| | |
|:---|:---|
| [BoxTrait](./core-box-BoxTrait.md) | [...](./core-box-BoxTrait.md) |

[Extern types](./core-box-extern_types.md)
 ---
| | |
|:---|:---|
| [Box](./core-box-Box.md) | A `Box`  is a type that points to a wrapped value. It allows for cheap moving around of the value, as its size is small, and may wrap a large size.[...](./core-box-Box.md) |
