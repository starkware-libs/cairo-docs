# StoragePointer

A pointer to an address in storage, can be used to read and write values, if the generic type supports it (e.g. basic types like `felt252`).

Fully qualified path: `core::starknet::storage::StoragePointer`

<pre><code class="language-rust">pub struct StoragePointer&lt;T&gt; {
    pub __storage_pointer_address__: StorageBaseAddress,
    pub __storage_pointer_offset__: u8,
}</code></pre>

## Members

### __storage_pointer_address__

Fully qualified path: `core::starknet::storage::StoragePointer::__storage_pointer_address__`

<pre><code class="language-rust">pub __storage_pointer_address__: StorageBaseAddress</code></pre>


### __storage_pointer_offset__

Fully qualified path: `core::starknet::storage::StoragePointer::__storage_pointer_offset__`

<pre><code class="language-rust">pub __storage_pointer_offset__: u8</code></pre>


