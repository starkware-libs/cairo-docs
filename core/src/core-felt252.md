# felt252

`felt252` is the basic field element used in Cairo.It corresponds to an integer in the range 0 ≤ x < P where P is a very large prime number currently equal to 2^251 + 17⋅2^192 + 1.Any operation that uses `felt252` will be computed modulo P.

Fully qualified path: `core::felt252`

<pre><code class="language-rust">pub extern type felt252</code></pre>

