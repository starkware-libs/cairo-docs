# BlockInfo

Information about the current block.

Fully qualified path: `core::starknet::info::BlockInfo`

<pre><code class="language-rust">#[derive(Copy, Drop, Debug, Serde)]
pub struct BlockInfo {
    pub block_number: u64,
    pub block_timestamp: u64,
    pub sequencer_address: ContractAddress,
}</code></pre>

## Members

### block_number

The number, that is, the height, of this block.

Fully qualified path: `core::starknet::info::BlockInfo::block_number`

<pre><code class="language-rust">pub block_number: u64</code></pre>


### block_timestamp

The time at which the sequencer began building the block, in seconds since the Unix epoch.

Fully qualified path: `core::starknet::info::BlockInfo::block_timestamp`

<pre><code class="language-rust">pub block_timestamp: u64</code></pre>


### sequencer_address

The Starknet address of the sequencer that created the block.

Fully qualified path: `core::starknet::info::BlockInfo::sequencer_address`

<pre><code class="language-rust">pub sequencer_address: ContractAddress</code></pre>


