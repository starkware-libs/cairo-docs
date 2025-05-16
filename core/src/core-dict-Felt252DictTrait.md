# Felt252DictTrait

Basic trait for the `Felt252Dict` type.

Fully qualified path: `core::dict::Felt252DictTrait`

<pre><code class="language-rust">pub trait Felt252DictTrait&lt;T&gt;</code></pre>

## Trait functions

### insert

Inserts the given value for the given key.  # Examples
```cairo
use core::dict::Felt252Dict;

let mut dict: Felt252Dict<u8> = Default::default();
dict.insert(0, 10);
```

Fully qualified path: `core::dict::Felt252DictTrait::insert`

<pre><code class="language-rust">fn insert&lt;+Destruct&lt;T&gt;&gt;(ref self: Felt252Dict&lt;T&gt;, key: felt252, value: T)</code></pre>


### get

Returns the value stored at the given key. If no value was previously inserted at this key, returns the default value for type T.  # Examples
```cairo
use core::dict::Felt252Dict;

let mut dict: Felt252Dict<u8> = Default::default();
dict.insert(0, 10);
let value = dict.get(0);
assert!(value == 10);
```

Fully qualified path: `core::dict::Felt252DictTrait::get`

<pre><code class="language-rust">fn get&lt;+Copy&lt;T&gt;&gt;(ref self: Felt252Dict&lt;T&gt;, key: felt252) -&gt; T</code></pre>


### squash

Squashes a dictionary and returns the associated `SquashedFelt252Dict`.  # Examples
```cairo
use core::dict::Felt252Dict;

let mut dict: Felt252Dict<u8> = Default::default();
dict.insert(0, 10);
let squashed_dict = dict.squash();
```

Fully qualified path: `core::dict::Felt252DictTrait::squash`

<pre><code class="language-rust">fn squash(self: Felt252Dict&lt;T&gt;) -&gt; SquashedFelt252Dict&lt;T&gt; nopanic</code></pre>


### entry

Retrieves the last entry for a certain key. This method takes ownership of the dictionary and returns the entry to update, as well as the previous value at the given key.  # Examples
```cairo
use core::dict::Felt252Dict;

let mut dict: Felt252Dict<u8> = Default::default();
dict.insert(0, 10);
let (entry, prev_value) = dict.entry(0);
assert!(prev_value == 10);
```

Fully qualified path: `core::dict::Felt252DictTrait::entry`

<pre><code class="language-rust">fn entry(self: Felt252Dict&lt;T&gt;, key: felt252) -&gt; (Felt252DictEntry&lt;T&gt;, T) nopanic</code></pre>


