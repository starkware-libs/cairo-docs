# felt252_div

Performs division on `felt252` values in Cairo's finite field. Unlike regular integer division, `felt252` division returns a field element n that satisfies the equation: n * rhs ≡ lhs (mod P), where P is the `felt252` prime.  # Examples
```cairo
use core::felt252_div;

// Division with 0 remainder works the same way as integer division.
assert!(felt252_div(4, 2) == 2);

// Division with non 0 remainder returns a field element n where n * 3 ≡ 4 (mod P)
assert!(felt252_div(4, 3) ==
1206167596222043737899107594365023368541035738443865566657697352045290673495);

```

Fully qualified path: `core::felt252_div`

<pre><code class="language-rust">pub extern fn felt252_div(lhs: felt252, rhs: NonZero&lt;felt252&gt;) -&gt; felt252 nopanic;</code></pre>

