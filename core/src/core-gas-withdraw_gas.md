# withdraw_gas

Withdraws gas from the `GasBuiltin` to handle the success case flow. Returns `Some(())` if there is sufficient gas to handle the success case, otherwise returns `None`.  # Examples
```cairo
// The success branch is the following lines, the failure branch is the `panic` caused by the
// `unwrap` call.
withdraw_gas().unwrap();
```

```cairo
// Direct handling of `withdraw_gas`.
match withdraw_gas() {
    Some(()) => success_case(),
    None => cheap_not_enough_gas_case(),
}
```

Fully qualified path: `core::gas::withdraw_gas`

<pre><code class="language-rust">pub extern fn withdraw_gas() -&gt; Option&lt;()&gt; implicits(RangeCheck, GasBuiltin) nopanic;</code></pre>

