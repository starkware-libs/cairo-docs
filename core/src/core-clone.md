# clone

The `Clone` trait provides the ability to duplicate instances of types that cannot be
'implicitly copied'.
In Cairo, some simple types are "implicitly copyable": when you assign them or pass them as
arguments, the receiver will get a copy, leaving the original value in place. These types do not
require allocation to copy, and are not at risk of accessing un-allocated memory, so the
compiler considers them cheap and safe to copy. For other types, copies must be made explicitly,
by convention implementing the [`Clone`](./core-clone-Clone.md) trait and calling the `Clone::clone` method.
# Examples

```cairo
let arr = array![1, 2, 3];
let cloned_arr = arr.clone();
assert!(arr == cloned_arr);
```

You can use the `#[derive(Clone)]` attribute to automatically generate the
implementation for your type:
```cairo
#[derive(Clone, Drop)]
struct Sheep {
   name: ByteArray,
   age: u8,
}

fn main() {
   let dolly = Sheep {
       name: "Dolly",
       age: 6,
   };

   let cloned_sheep = dolly.clone();  // Famous cloned sheep!
}
```

Fully qualified path: [core](./core.md)::[clone](./core-clone.md)


[Traits](./core-clone-traits.md)
 ---
| | |
|:---|:---|
| [Clone](./core-clone-Clone.md) | A common trait for the ability to explicitly duplicate an object. Differs from `Copy`  in that `Copy`  is implicit and inexpensive, while `Clone`  is always explicit and may or may not be expensive.[...](./core-clone-Clone.md) |
