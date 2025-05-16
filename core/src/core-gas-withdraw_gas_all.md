# withdraw_gas_all

Same as `withdraw_gas`, but directly receives `BuiltinCosts`, which enables optimizations by removing the need for repeated internal calls for fetching the table of constants that may internally happen in calls to `withdraw_gas`. Should be used with caution.

Fully qualified path: `core::gas::withdraw_gas_all`

<pre><code class="language-rust">pub extern fn withdraw_gas_all(
    costs: BuiltinCosts,
) -&gt; Option&lt;()&gt; implicits(RangeCheck, GasBuiltin) nopanic;</code></pre>

