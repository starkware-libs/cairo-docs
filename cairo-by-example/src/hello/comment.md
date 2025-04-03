# Comments

Any program requires comments, and Cairo supports
a single few different varieties:

- _Regular comments_ which are ignored by the compiler:
  - `// Line comments which go to the end of the line.`
- _Doc comments_ which are parsed into HTML library [documentation][docs]:
  - `/// Generate library docs for the following item.`
  - `//! Generate library docs for the enclosing item.`

```cairo,editable
{{#include ../../listings/hello/comment/src/lib.cairo}}
```
