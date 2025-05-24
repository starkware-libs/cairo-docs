# File hierarchy

Modules can be mapped to a file/directory hierarchy. Let's break down the
[visibility example][visibility] in files:

```shell
$ tree .
.
├── src
│   ├── my
│   │   ├── inaccessible.cairo
│   │   └── nested.cairo
│   ├── my.cairo
│   └── lib.cairo
└── Scarb.toml
```

In `src/lib.cairo`:

```cairo,noplayground
{{#include ../../listings/mod/split/src/lib.cairo}}
```

In `src/my.cairo`:

```cairo,noplayground
{{#include ../../listings/mod/split/src/my.cairo}}
```

In `src/my/inaccessible.cairo`:

```cairo,noplayground
{{#include ../../listings/mod/split/src/my/inaccessible.cairo}}
```

Let's check that things still work as before:

```shell
{{#include ../../listings/mod/split/output.txt}}
```

[visibility]: visibility.md
