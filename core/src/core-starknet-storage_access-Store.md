# Store

Trait for types that can be stored in Starknet contract storage.The `Store` trait enables types to be stored in and retrieved from Starknet's contract storage. Cairo implements `Store` for most primitive types. However, collection types (arrays, dicts, etc.) do not implement `Store` directly. Instead, use specialized storage types, such as [`Vec`](`Vec`) or [`Map`](`Map`).[`Map`](`Map`): starknet::storage::Map [`Vec`](`Vec`): starknet::storage::Vec  # DerivationTo make a type storable in contract storage, simply derive the `Store` trait:
```cairo
#[derive(Drop, starknet::Store)]
struct Sizes {
    tiny: u8,    // 8 bits
    small: u32,  // 32 bits
    medium: u64, // 64 bits
}
```
This allows the `Size` struct to be stored in a contract's storage.There's no real reason to implement this trait yourself, as it can be trivially derived. For efficiency purposes, consider manually implementing [`StorePacking`](./core-starknet-storage_access-StorePacking.md) to optimize storage usage.

Fully qualified path: `core::starknet::storage_access::Store`

<pre><code class="language-rust">pub trait Store&lt;T&gt;</code></pre>

## Trait functions

### read

Reads a value from storage at the given domain and base address.  # Arguments`address_domain` - The storage domain (currently only 0 is supported) * `base` - The base storage address to read from

Fully qualified path: `core::starknet::storage_access::Store::read`

<pre><code class="language-rust">fn read(address_domain: u32, base: StorageBaseAddress) -&gt; SyscallResult&lt;T&gt;</code></pre>


### write

Writes a value to storage at the given domain and base address.  # Arguments`address_domain` - The storage domain (currently only 0 is supported) * `base` - The base storage address to write to * `value` - The value to store

Fully qualified path: `core::starknet::storage_access::Store::write`

<pre><code class="language-rust">fn write(address_domain: u32, base: StorageBaseAddress, value: T) -&gt; SyscallResult&lt;()&gt;</code></pre>


### read_at_offset

Reads a value from storage at a base address plus an offset.  # Arguments`address_domain` - The storage domain (currently only 0 is supported) * `base` - The base storage address * `offset` - The offset from the base address where the value should be read

Fully qualified path: `core::starknet::storage_access::Store::read_at_offset`

<pre><code class="language-rust">fn read_at_offset(address_domain: u32, base: StorageBaseAddress, offset: u8) -&gt; SyscallResult&lt;T&gt;</code></pre>


### write_at_offset

Writes a value to storage at a base address plus an offset.  # Arguments`address_domain` - The storage domain (currently only 0 is supported) * `base` - The base storage address * `offset` - The offset from the base address where the value should be written * `value` - The value to store

Fully qualified path: `core::starknet::storage_access::Store::write_at_offset`

<pre><code class="language-rust">fn write_at_offset(
    address_domain: u32, base: StorageBaseAddress, offset: u8, value: T,
) -&gt; SyscallResult&lt;()&gt;</code></pre>


### size

Returns the size in storage for this type.This is bounded to 255, as the offset is a u8. As such, a single type can only take up to 255 slots in storage.

Fully qualified path: `core::starknet::storage_access::Store::size`

<pre><code class="language-rust">fn size() -&gt; u8</code></pre>


### scrub

Clears the storage area by writing zeroes to it.  # Arguments`address_domain` - The storage domain * `base` - The base storage address to start clearing * `offset` - The offset from the base address where clearing should startThe operation writes zeroes to storage starting from the specified base address and offset, and continues for the size of the type as determined by the `size()` function.

Fully qualified path: `core::starknet::storage_access::Store::scrub`

<pre><code class="language-rust">fn scrub(address_domain: u32, base: StorageBaseAddress, offset: u8) -&gt; SyscallResult&lt;()&gt;</code></pre>


