# EventEmitter

A trait for emitting Starknet events.  # Examples
```cairo
#[derive(Drop, starknet::Event)]
pub struct NewOwner {
    pub new_owner: ContractAddress,
}

fn emit_event(ref self: ContractState, new_owner: ContractAddress) {
    self.emit(NewOwner { new_owner });
}
```

Fully qualified path: `core::starknet::event::EventEmitter`

<pre><code class="language-rust">pub trait EventEmitter&lt;T, TEvent&gt;</code></pre>

## Trait functions

### emit

Emits an event.

Fully qualified path: `core::starknet::event::EventEmitter::emit`

<pre><code class="language-rust">fn emit&lt;S, +Into&lt;S, TEvent&gt;&gt;(ref self: T, event: S)</code></pre>


