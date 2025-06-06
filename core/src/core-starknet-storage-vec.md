# vec

Vector-like storage collection for persisting data in contract storage.
This module provides a vector-like collection that stores elements in contract storage.
Unlike memory arrays, storage vectors persist data onchain, meaning that values can be retrieved
even after the end of the current context.
# Storage Layout

A storage vector consists of two parts:
- The vector length stored at the base storage address (`sn_keccak(variable_name)`)
- The elements stored at addresses computed as `h(base_address, index)` where:
    - `h` is the Pedersen hash function
    - `index` is the element's position in the vector
# Interacting with [`Vec`](./core-starknet-storage-vec-Vec.md)

Storage vectors can be accessed through two sets of traits:

1. Read-only access using `VecTrait`:
```cairo
// Get length
let len = self.my_vec.len();

// Read element (panics if out of bounds)
let value = self.my_vec.at(0).read();

// Read element (returns Option)
let maybe_value: Option<u256> = self.my_vec.get(0).map(|ptr| ptr.read());
```


2. Mutable access using `MutableVecTrait`:
```cairo
// Append new element using push
self.my_vec.push(value);

// Allocate space for a new element (useful for nested vectors)
let new_slot = self.my_vec.allocate();

// Modify existing element
self.my_vec.at(0).write(new_value);
```

# Examples

Basic usage:
```cairo
use starknet::storage::{Vec, VecTrait, MutableVecTrait, StoragePointerReadAccess,
StoragePointerWriteAccess};

#[storage]
struct Storage {
    numbers: Vec<u256>,
}

fn store_number(ref self: ContractState, number: u256) {
    // Append new number
    self.numbers.push(number);

    // Read first number
    let first = self.numbers[0].read();

    // Get current length
    let size = self.numbers.len();
}
```

Loading the numbers into a memory array:
```cairo
use starknet::storage::{Vec, VecTrait, StoragePointerReadAccess};

fn to_array(self: @ContractState) -> Array<u256> {
    let mut arr = array![];

    let len = self.numbers.len();
    for i in 0..len {
        arr.append(self.numbers[i].read());
    }
    arr
}
```

Fully qualified path: [core](./core.md)::[starknet](./core-starknet.md)::[storage](./core-starknet-storage.md)::[vec](./core-starknet-storage-vec.md)


[Structs](./core-starknet-storage-vec-structs.md)
 ---
| | |
|:---|:---|
| [Vec](./core-starknet-storage-vec-Vec.md) | Represents a dynamic array in contract storage. This type is zero-sized and cannot be instantiated. Vectors can only be used in storage contexts and manipulated using the associated `VecTrait` and[...](./core-starknet-storage-vec-Vec.md) |
| [VecIter](./core-starknet-storage-vec-VecIter.md) | An iterator struct over a `Vec`  in storage.[...](./core-starknet-storage-vec-VecIter.md) |

[Traits](./core-starknet-storage-vec-traits.md)
 ---
| | |
|:---|:---|
| [MutableVecTrait](./core-starknet-storage-vec-MutableVecTrait.md) | Provides mutable access to elements in a storage [`Vec`](./core-starknet-storage-vec-Vec.md) . This trait extends the read functionality with methods to append new elements and modify existing ones.[...](./core-starknet-storage-vec-MutableVecTrait.md) |
| [VecTrait](./core-starknet-storage-vec-VecTrait.md) | Provides read-only access to elements in a storage [`Vec`](./core-starknet-storage-vec-Vec.md) . This trait enables retrieving elements and checking the vector's length without[...](./core-starknet-storage-vec-VecTrait.md) |
