# Event

A trait for handling serialization and deserialization of events.Events in Starknet are stored in transaction receipts as a combination of keys and data fields. This trait provides the methods needed to serialize event data into these fields and deserialize them back into their original form.This trait can easily be derived using the `#[derive(starknet::Event)]` attribute. Fields can be marked as keys using the `#[key]` attribute to serialize them as event keys.  # Examples
```cairo
#[derive(Drop, starknet::Event)]
pub struct Transfer {
    #[key]
    pub from: ContractAddress,
    #[key]
    pub to: ContractAddress,
    pub amount: u256,
}
```

Fully qualified path: `core::starknet::event::Event`

<pre><code class="language-rust">pub trait Event&lt;T&gt;</code></pre>

## Trait functions

### append_keys_and_data

Serializes the keys and data for event emission.The keys array will contain: - The event name selector as the first key - Any fields marked with #[key](key) as subsequent keysThe data array will contain all non-key fields.

Fully qualified path: `core::starknet::event::Event::append_keys_and_data`

<pre><code class="language-rust">fn append_keys_and_data(self: @T, ref keys: Array&lt;felt252&gt;, ref data: Array&lt;felt252&gt;)</code></pre>


### deserialize

Deserializes events keys and data back into the original event structure.Returns `None` if deserialization fails.

Fully qualified path: `core::starknet::event::Event::deserialize`

<pre><code class="language-rust">fn deserialize(ref keys: Span&lt;felt252&gt;, ref data: Span&lt;felt252&gt;) -&gt; Option&lt;T&gt;</code></pre>


