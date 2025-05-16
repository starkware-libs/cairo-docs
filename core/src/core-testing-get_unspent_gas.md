# get_unspent_gas

Returns the amount of gas available in the `GasBuiltin`, as well as the amount of gas unused in the local wallet.Useful for asserting that a certain amount of gas used. Note: This function call costs exactly `2300` gas, so this may be ignored in calculations. # Examples
```cairo
use core::testing::get_unspent_gas;

fn gas_heavy_function() {
    // ... some gas-intensive code
}

fn test_gas_consumption() {
    let gas_before = get_unspent_gas();
    gas_heavy_function();
    let gas_after = get_unspent_gas();
    assert!(gas_after - gas_before < 100_000);
}
```

Fully qualified path: `core::testing::get_unspent_gas`

<pre><code class="language-rust">pub extern fn get_unspent_gas() -&gt; u128 implicits(GasBuiltin) nopanic;</code></pre>

