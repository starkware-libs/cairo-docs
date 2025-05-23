# get_available_gas

Returns the amount of gas available in the `GasBuiltin`.Useful for asserting that a certain amount of gas was consumed. Note: The actual gas consumption observed by calls to `get_available_gas` is only exact immediately before calls to `withdraw_gas`.  # Examples
```cairo
use core::testing::get_available_gas;

fn gas_heavy_function() {
    // ... some gas-intensive code
}

fn test_gas_consumption() {
    let gas_before = get_available_gas();
    // Making sure `gas_before` is exact.
    core::gas::withdraw_gas().unwrap();

    gas_heavy_function();

    let gas_after = get_available_gas();
    // Making sure `gas_after` is exact
    core::gas::withdraw_gas().unwrap();

    assert!(gas_after - gas_before < 100_000);
}
```

Fully qualified path: `core::testing::get_available_gas`

<pre><code class="language-rust">pub extern fn get_available_gas() -&gt; u128 implicits(GasBuiltin) nopanic;</code></pre>

