# AccountContract

A trait for account contracts that support class declarations (only `__validate__` and `__execute__` are mandatory for an account).This trait assumes that the calldata for invoke transactions is `Array<Call>`. This is the network standard following SNIP6. It is not enforced by Starknet, but deviating from the standard interface may lead to incompatibility with standard tooling.

Fully qualified path: `core::starknet::account::AccountContract`

<pre><code class="language-rust">pub trait AccountContract&lt;TContractState&gt;</code></pre>

## Trait functions

### __validate_declare__

An entry point that is called to check if the account is willing to pay for the declaration of the class with the given hash. The entry point should return `starknet::VALIDATED` if the account is willing to pay for the declaration.

Fully qualified path: `core::starknet::account::AccountContract::__validate_declare__`

<pre><code class="language-rust">fn __validate_declare__(self: @TContractState, class_hash: felt252) -&gt; felt252</code></pre>


### __validate__

An entry point that is called to check if the account is willing to pay for executing a given set of calls. The entry point should return `starknet::VALIDATED` if the account is willing to pay for the execution, in which case `__execute__` will be called on the same set of calls.

Fully qualified path: `core::starknet::account::AccountContract::__validate__`

<pre><code class="language-rust">fn __validate__(ref self: TContractState, calls: Array&lt;Call&gt;) -&gt; felt252</code></pre>


### __execute__

An entry point that is called to execute a given set of calls. This entry point should block the deprecated v0 invoke transactions as they do not go through the `__validate__` entry point.

Fully qualified path: `core::starknet::account::AccountContract::__execute__`

<pre><code class="language-rust">fn __execute__(ref self: TContractState, calls: Array&lt;Call&gt;) -&gt; Array&lt;Span&lt;felt252&gt;&gt;</code></pre>


