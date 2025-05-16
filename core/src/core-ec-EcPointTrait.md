# EcPointTrait

Fully qualified path: `core::ec::EcPointTrait`

<pre><code class="language-rust">pub trait EcPointTrait</code></pre>

## Trait functions

### new

Creates a new EC point from its (x, y) coordinates.  # Arguments`x` - The x-coordinate of the point * `y` - The y-coordinate of the point  # ReturnsReturns `None` if the point (x, y) is not on the curve.  # Examples
```cairo
let point = EcPointTrait::new(
    x: 336742005567258698661916498343089167447076063081786685068305785816009957563,
    y: 1706004133033694959518200210163451614294041810778629639790706933324248611779,
).unwrap();
```

Fully qualified path: `core::ec::EcPointTrait::new`

<pre><code class="language-rust">fn new(x: felt252, y: felt252) -&gt; Option&lt;EcPoint&gt;</code></pre>


### new_nz

Creates a new NonZero EC point from its (x, y) coordinates.

Fully qualified path: `core::ec::EcPointTrait::new_nz`

<pre><code class="language-rust">fn new_nz(x: felt252, y: felt252) -&gt; Option&lt;NonZeroEcPoint&gt;</code></pre>


### new_from_x

Creates a new EC point from its x coordinate.  # Arguments`x` - The x-coordinate of the point  # ReturnsReturns `None` if no point with the given x-coordinate exists on the curve.  # PanicsPanics if `x` is 0, as this would be the point at infinity.  # Examples
```cairo
let valid = EcPointTrait::new_from_x(1);
assert!(valid.is_some());
let invalid = EcPointTrait::new_from_x(0);
assert!(invalid.is_none());
```

Fully qualified path: `core::ec::EcPointTrait::new_from_x`

<pre><code class="language-rust">fn new_from_x(x: felt252) -&gt; Option&lt;EcPoint&gt;</code></pre>


### new_nz_from_x

Creates a new NonZero EC point from its x coordinate.

Fully qualified path: `core::ec::EcPointTrait::new_nz_from_x`

<pre><code class="language-rust">fn new_nz_from_x(x: felt252) -&gt; Option&lt;NonZeroEcPoint&gt;</code></pre>


### coordinates

Returns the coordinates of the EC point.  # ReturnsA tuple containing the (x, y) coordinates of the point.  # PanicsPanics if the point is the point at infinity.  # Examples
```cairo
let point_nz = EcPointTrait::new_nz_from_x(1).unwrap();
let (x, _y) = point_nz.coordinates();
assert!(x == 1);
```

Fully qualified path: `core::ec::EcPointTrait::coordinates`

<pre><code class="language-rust">fn coordinates(self: NonZeroEcPoint) -&gt; (felt252, felt252)</code></pre>


### x

Returns the x coordinate of the EC point.  # PanicsPanics if the point is the point at infinity.  # Examples
```cairo
let point_nz = EcPointTrait::new_nz_from_x(1).unwrap();
let x = point_nz.x();
assert!(x == 1);
```

Fully qualified path: `core::ec::EcPointTrait::x`

<pre><code class="language-rust">fn x(self: NonZeroEcPoint) -&gt; felt252</code></pre>


### y

Returns the y coordinate of the EC point.  # PanicsPanics if the point is the point at infinity.  # Examples
```cairo
let gen_point =
EcPointTrait::new_nz_from_x(0x1ef15c18599971b7beced415a40f0c7deacfd9b0d1819e03d723d8bc943cfca).unwrap();
let y = gen_point.y();
assert!(y == 0x5668060aa49730b7be4801df46ec62de53ecd11abe43a32873000c36e8dc1f);
```

Fully qualified path: `core::ec::EcPointTrait::y`

<pre><code class="language-rust">fn y(self: NonZeroEcPoint) -&gt; felt252</code></pre>


### mul

Computes the product of an EC point by the given scalar.  # Arguments`scalar` - The scalar to multiply the point by  # ReturnsThe resulting point after scalar multiplication.

Fully qualified path: `core::ec::EcPointTrait::mul`

<pre><code class="language-rust">fn mul(self: EcPoint, scalar: felt252) -&gt; EcPoint</code></pre>


