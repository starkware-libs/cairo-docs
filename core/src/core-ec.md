# ec

Functions and constructs related to elliptic curve operations on the STARK curve.
This module provides implementations for various elliptic curve operations tailored for the
STARK curve.
Curve information:
- Curve equation: y² ≡ x³ + α·x + β (mod p)
- α = 1
- β = 0x6f21413efbe40de150e596d72f7a8c5609ad26c15c915c1f4cdfcb99cee9e89
- p = 0x0800000000000011000000000000000000000000000000000000000000000001 = 2^251 + 17 * 2^192 +
1
Generator point:
- x = 0x1ef15c18599971b7beced415a40f0c7deacfd9b0d1819e03d723d8bc943cfca
- y = 0x5668060aa49730b7be4801df46ec62de53ecd11abe43a32873000c36e8dc1f
# Examples

Creating points and basic operations:
```cairo
// Create a point from coordinates
let point = EcPointTrait::new(
    x: 336742005567258698661916498343089167447076063081786685068305785816009957563,
    y: 1706004133033694959518200210163451614294041810778629639790706933324248611779,
).unwrap();

// Perform scalar multiplication
let result = point.mul(2);

// Add points
let sum = point + result;

// Subtract points
let diff = result - point;
```

Using EC state for batch operations:
```cairo
let p = EcPointTrait::new_from_x(1).unwrap();
let p_nz = p.try_into().unwrap();

// Initialize state
let mut state = EcStateTrait::init();

// Add points and scalar multiplications
state.add(p_nz);
state.add_mul(1, p_nz);

// Get the final result
let _result = state.finalize();
```

Fully qualified path: [core](./core.md)::[ec](./core-ec.md)


[Modules](./core-ec-modules.md)
 ---
| | |
|:---|:---|
| [stark_curve](./core-ec-stark_curve.md) | [...](./core-ec-stark_curve.md) |

[Type aliases](./core-ec-type_aliases.md)
 ---
| | |
|:---|:---|
| [NonZeroEcPoint](./core-ec-NonZeroEcPoint.md) | A non-zero point on the STARK curve (cannot be the point at infinity).[...](./core-ec-NonZeroEcPoint.md) |

[Traits](./core-ec-traits.md)
 ---
| | |
|:---|:---|
| [EcStateTrait](./core-ec-EcStateTrait.md) | [...](./core-ec-EcStateTrait.md) |
| [EcPointTrait](./core-ec-EcPointTrait.md) | [...](./core-ec-EcPointTrait.md) |

[Impls](./core-ec-impls.md)
 ---
| | |
|:---|:---|
| [EcStateImpl](./core-ec-EcStateImpl.md) | [...](./core-ec-EcStateImpl.md) |
| [EcPointImpl](./core-ec-EcPointImpl.md) | [...](./core-ec-EcPointImpl.md) |

[Extern types](./core-ec-extern_types.md)
 ---
| | |
|:---|:---|
| [EcOp](./core-ec-EcOp.md) | [...](./core-ec-EcOp.md) |
| [EcPoint](./core-ec-EcPoint.md) | A point on the STARK curve. Points can be created using `EcPointTrait::new`  or `EcPointTrait::new_from_x` . The zero point represents the point at infinity.[...](./core-ec-EcPoint.md) |
| [EcState](./core-ec-EcState.md) | Elliptic curve state. Use this to perform multiple point operations efficiently. Initialize with `EcStateTrait::init` , add points with `EcStateTrait::add` or `EcStateTrait::add_mul`[...](./core-ec-EcState.md) |

[Extern functions](./core-ec-extern_functions.md)
 ---
| | |
|:---|:---|
| [ec_point_unwrap](./core-ec-ec_point_unwrap.md) | Unwraps a non-zero point into its (x, y) coordinates.[...](./core-ec-ec_point_unwrap.md) |
