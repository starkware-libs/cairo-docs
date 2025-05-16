# deploy_syscall

Deploys a new instance of a previously declared class.  # Arguments`class_hash` - The class hash of the contract to be deployed. * `contract_address_salt` - The salt, an arbitrary value provided by the deployer, used in the computation of the contract's address. * `calldata` - Call arguments for the constructor. * `deploy_from_zero` - Deploy the contract from the zero address.  # ReturnsThe address of the deployed contract. * The serialized return value of the constructor.

Fully qualified path: `core::starknet::syscalls::deploy_syscall`

<pre><code class="language-rust">pub extern fn deploy_syscall(
    class_hash: ClassHash,
    contract_address_salt: felt252,
    calldata: Span&lt;felt252&gt;,
    deploy_from_zero: bool,
) -&gt; SyscallResult&lt;(ContractAddress, Span&lt;felt252&gt;)&gt; implicits(GasBuiltin, System) nopanic;</code></pre>

