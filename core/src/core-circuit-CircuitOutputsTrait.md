# CircuitOutputsTrait

A trait for retrieving output values from a circuit evaluation.This trait provides methods to access the output values of a circuit after successful evaluation.  # Examples
```cairo
let a = CircuitElement::<CircuitInput<0>> {};
let b = CircuitElement::<CircuitInput<1>> {};
let modulus = TryInto::<_, CircuitModulus>::try_into([2, 0, 0, 0]).unwrap();
let circuit = (a,b).new_inputs()
    .next([10, 0, 0, 0])
    .next([11, 0, 0, 0])
    .done()
    .eval(modulus)
    .unwrap();
let a_mod_2 = circuit.get_output(a); // Returns the output value of `a mod 2`
let b_mod_2 = circuit.get_output(b); // Returns the output value of `b mod 2`
assert!(a_mod_2 == 0.into());
assert!(b_mod_2 == 1.into());
```

Fully qualified path: `core::circuit::CircuitOutputsTrait`

<pre><code class="language-rust">pub trait CircuitOutputsTrait&lt;Outputs, OutputElement&gt;</code></pre>

## Trait functions

### get_output

Gets the output value for a specific circuit element.  # Arguments`output` - The circuit element to get the output for  # ReturnsThe output value as a u384

Fully qualified path: `core::circuit::CircuitOutputsTrait::get_output`

<pre><code class="language-rust">fn get_output(self: Outputs, output: OutputElement) -&gt; u384</code></pre>


