# get_tx_info

Returns the transaction information for the current transaction.  # Examples
```cairo
use starknet::get_tx_info;

let tx_info = get_tx_info().unbox();

let account_contract_address = tx_info.account_contract_address;
let chain_id = tx_info.chain_id;
let nonce = tx_info.nonce;
let max_fee = tx_info.max_fee;
let tx_hash = tx_info.transaction_hash;
let signature = tx_info.signature;
let version = tx_info.version;
```

Fully qualified path: `core::starknet::info::get_tx_info`

<pre><code class="language-rust">pub fn get_tx_info() -&gt; Box&lt;v2::TxInfo&gt;</code></pre>

