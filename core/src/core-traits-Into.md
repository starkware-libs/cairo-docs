# Into

A value-to-value conversion that consumes the input value.Note: This trait must not fail. If the conversion can fail, use [`TryInto`](./core-traits-TryInto.md).  # Generic Implementations[`Into`](./core-traits-Into.md) is reflexive, which means that `Into<T, T>` is implemented  # ExamplesConverting from RGB components to a packed color value:
```cairo
#[derive(Copy, Drop, PartialEq)]
struct Color {
    // Packed as 0x00RRGGBB
    value: u32,
}

impl RGBIntoColor of Into<(u8, u8, u8), Color> {
    fn into(self: (u8, u8, u8)) -> Color {
        let (r, g, b) = self;
        let value = (r.into() * 0x10000_u32) +
                   (g.into() * 0x100_u32) +
                   b.into();
        Color { value }
    }
}

// Convert RGB(255, 128, 0) to 0x00FF8000
let orange: Color = (255_u8, 128_u8, 0_u8).into();
assert!(orange == Color { value: 0x00FF8000_u32 });
```

Fully qualified path: `core::traits::Into`

<pre><code class="language-rust">pub trait Into&lt;T, S&gt;</code></pre>

## Trait functions

### into

Converts the input type T into the output type S.  # Examples
```cairo
let a: u8 = 1;
let b: u16 = a.into();
```

Fully qualified path: `core::traits::Into::into`

<pre><code class="language-rust">fn into(self: T) -&gt; S</code></pre>


