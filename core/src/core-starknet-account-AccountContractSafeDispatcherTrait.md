# AccountContractSafeDispatcherTrait

Fully qualified path: `core::starknet::account::AccountContractSafeDispatcherTrait`

<pre><code class="language-rust">pub trait AccountContractSafeDispatcherTrait&lt;T&gt;</code></pre>

## Trait functions

### __validate_declare__

An entry point that is called to check if the account is willing to pay for the declaration of the class with the given hash. The entry point should return `starknet::VALIDATED` if the account is willing to pay for the declaration.

Fully qualified path: `core::starknet::account::AccountContractSafeDispatcherTrait::__validate_declare__`

<pre><code class="language-rust">fn __validate_declare__(self: T, class_hash: felt252) -&gt; starknet::SyscallResult&lt;felt252&gt;</code></pre>


### __validate__

An entry point that is called to check if the account is willing to pay for executing a given set of calls. The entry point should return `starknet::VALIDATED` if the account is willing to pay for the execution, in which case `__execute__` will be called on the same set of calls.

Fully qualified path: `core::starknet::account::AccountContractSafeDispatcherTrait::__validate__`

<pre><code class="language-rust">fn __validate__(self: T, calls: Array&lt;Call&gt;) -&gt; starknet::SyscallResult&lt;felt252&gt;</code></pre>


### __execute__

An entry point that is called to execute a given set of calls. This entry point should block the deprecated v0 invoke transactions as they do not go through the `__validate__` entry point.

Fully qualified path: `core::starknet::account::AccountContractSafeDispatcherTrait::__execute__`

<pre><code class="language-rust">fn __execute__(self: T, calls: Array&lt;Call&gt;) -&gt; starknet::SyscallResult&lt;Array&lt;Span&lt;felt252&gt;&gt;&gt;</code></pre>


