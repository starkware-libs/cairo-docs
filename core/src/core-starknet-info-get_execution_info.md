# get_execution_info

Returns the execution info for the current execution.  # Examples
```cairo
use starknet::get_execution_info;

let execution_info = get_execution_info().unbox();

// Access various execution context information
let caller = execution_info.caller_address;
let contract = execution_info.contract_address;
let selector = execution_info.entry_point_selector;
```

Fully qualified path: `core::starknet::info::get_execution_info`

<pre><code class="language-rust">pub fn get_execution_info() -&gt; Box&lt;v2::ExecutionInfo&gt;</code></pre>

