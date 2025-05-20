The Cairo Core library docs are auto-generated from the library's [codebase](https://github.com/starkware-libs/cairo/tree/main/corelib) using [Scarb](https://docs.swmansion.com/scarb/docs/extensions/documentation-generation.html).

To preview the docs, run:
```
mdbook serve --open
```

To update the docs:

1. Verify the latest versions of [Scarb](https://github.com/software-mansion/scarb/releases) and [mdBook](https://github.com/rust-lang/mdBook/releases) are installed:
    ```
    scarb --version && mdbook --version
    ```  

1. Clone the Cairo repository:
    ```
    git clone https://github.com/starkware-libs/cairo.git
    ```

2. Navigate into the `cairo/corelib` directory, delete the `.tool-versions` file, and generate the docs:
    ```
    cd cairo/corelib && rm .tool-versions && scarb doc
    ```

3. Navigate back to the `core` directory, replace the existing docs, and delete the `cairo` directory:
    ```
    cd ../.. && cp -r cairo/corelib/target/doc/core/src/ src/ && rm -rf cairo
    ```

4. Add `intro.md` to the new docs:
    ```
    cp intro.md src/intro.md sed -i "" "1s/.*/- [Introduction](.\/intro.md)/" src/SUMMARY.md
    ```

5. Rebuild the book:
    ```
    mdbook build
    ```
