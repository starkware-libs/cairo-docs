# Inference

The type inference engine is pretty smart. It does more than looking at the
type of the value expression
during an initialization. It also looks at how the variable is used afterwards
to infer its type. Here's an advanced example of type inference:

```cairo,editable
{{#include ../../listings/types/inference/src/lib.cairo}}
```

No type annotation of variables was needed, the compiler is happy and so is the
programmer!
