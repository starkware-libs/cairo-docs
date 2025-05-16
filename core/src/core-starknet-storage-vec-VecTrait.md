# VecTrait

Provides read-only access to elements in a storage [`Vec`](./core-starknet-storage-vec-Vec.md).This trait enables retrieving elements and checking the vector's length without modifying the underlying storage.

Fully qualified path: `core::starknet::storage::vec::VecTrait`

<pre><code class="language-rust">pub trait VecTrait&lt;T&gt;</code></pre>

## Trait functions

### get

Returns a storage path to the element at the specified index, or `None` if out of bounds.  # Examples
```cairo
use starknet::storage::{Vec, VecTrait, StoragePointerReadAccess};

#[storage]
struct Storage {
    numbers: Vec<u256>,
}

fn maybe_number(self: @ContractState, index: u64) -> Option<u256> {
    self.numbers.get(index).map(|ptr| ptr.read())
}
```

Fully qualified path: `core::starknet::storage::vec::VecTrait::get`

<pre><code class="language-rust">fn get(self: T, index: u64) -&gt; Option&lt;StoragePath&lt;Self::ElementType&gt;&gt;</code></pre>


### at

Returns a storage path to access the element at the specified index.  # PanicsPanics if the index is out of bounds.  # Examples
```cairo
use starknet::storage::{Vec, VecTrait, StoragePointerReadAccess};

#[storage]
struct Storage {
    numbers: Vec<u256>,
}

fn get_number(self: @ContractState, index: u64) -> u256 {
    self.numbers.at(index).read()
}
```

Fully qualified path: `core::starknet::storage::vec::VecTrait::at`

<pre><code class="language-rust">fn at(self: T, index: u64) -&gt; StoragePath&lt;Self::ElementType&gt;</code></pre>


### len

Returns the number of elements in the vector.The length is stored at the vector's base storage address and is automatically updated when elements are appended.  # Examples
```cairo
use starknet::storage::{Vec, VecTrait};

#[storage]
struct Storage {
    numbers: Vec<u256>,
}

fn is_empty(self: @ContractState) -> bool {
    self.numbers.len() == 0
}
```

Fully qualified path: `core::starknet::storage::vec::VecTrait::len`

<pre><code class="language-rust">fn len(self: T) -&gt; u64</code></pre>


## Trait types

### ElementType

Fully qualified path: `core::starknet::storage::vec::VecTrait::ElementType`

<pre><code class="language-rust">type ElementType;</code></pre>


