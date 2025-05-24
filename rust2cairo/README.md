# Cairo By Example

Learn Cairo with examples (Live code editor included)

## Using

If you'd like to read Cairo by Example, you can visit <https://docs.cairo-lang.org/cairo-by-example/>
to read it online.

If you'd like to read it locally, [install Rust], and then:

```bash
git clone https://github.com/cairo-book/cairo-by-example
cd cairo-by-example
cargo install mdbook
mdbook build
mdbook serve
```

[install Rust]: https://www.rust-lang.org/tools/install

**The following warnings can be ignored safely.**

```text
[WARN] (mdbook::preprocess::cmd): The command wasn't found, is the "gettext" preprocessor installed?
[WARN] (mdbook::preprocess::cmd):   Command: mdbook-gettext
```

## Development

- Install [cairo-listings](https://github.com/enitrat/cairo-listings)

  ```bash
  cargo install --git https://github.com/enitrat/cairo-listings
  ```

- Install [mdbook-cairo](https://github.com/enitrat/mdbook-cairo)
  ```bash
  cargo install --git https://github.com/enitrat/mdbook-cairo
  ```

### Formatting

```bash
cairo-listings format
```

### Verifying compilation and tests

```bash
cairo-listings verify
```
