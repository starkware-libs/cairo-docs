# Maintaining Cairo By Example

This document outlines the key aspects of maintaining the Cairo By Example (CBE) codebase.

## Project Structure

The CBE website is built using [mdbook](https://rust-lang.github.io/mdBook/index.html). The content is written in Markdown, and the code examples are embedded within the Markdown files.

- `book.toml`: This file configures the mdbook build process. It specifies the book's title, description, authors, and output settings. See lines 1-42.
- `src/`: This directory contains the Markdown files that make up the book's content. The structure of this directory mirrors the table of contents defined in `src/SUMMARY.md`.
- `src/SUMMARY.md`: This file defines the table of contents for the book. It lists the Markdown files in the order they should appear in the book. See lines 1-161.
- `listings/`: This directory contains the Cairo code examples that are embedded in the Markdown files. The structure of this directory mirrors the `src/` directory. Each code example is placed in its own directory with a `Scarb.toml` file and a `src/lib.cairo` file.
- `theme/`: This directory contains the custom theme files for the book.
  - `index.hbs`: This is the main Handlebars template file that defines the structure of the HTML pages. See lines 1-18. It includes the header, sidebar, content, and navigation elements. It also includes the custom CSS and JavaScript files.
  - `js/index.mjs`: This file contains the JavaScript code that runs the Cairo code examples in the browser. See lines 1-49. It uses the `wasm-cairo` package to execute the Cairo code.
  - `highlight.js`: This file defines the Cairo syntax highlighting for the code examples. It comes from [Scarb Doc](https://github.com/software-mansion/scarb/tree/main/extensions/scarb-doc/theme).
  - `css/`: This directory contains the CSS files that define the look and feel of the book.
- `.github/workflows/`: This directory contains the GitHub Actions workflows that automate the build and deployment of the book.
  - `ci.yml`: This workflow runs the tests and builds the book on every pull request.
  - `mdbook.yml`: This workflow builds and deploys the book to GitHub Pages on every push to the `main` branch.
- `.gitignore`: Specifies intentionally untracked files that Git should ignore. See lines 1-12.
- `README.md`: Provides a general overview of the project and instructions on how to use it.
- `_typos.toml`: Configuration file for the [typos](https://github.com/crate-ci/typos) tool, used for automated typo fixes. See lines 1-9.

## Code Examples

The Cairo code examples are stored in the `listings/` directory. Each code example is a separate Scarb package with its own `Scarb.toml` file and `src/lib.cairo` file. This allows the code examples to be compiled and tested independently.

To embed a code example in a Markdown file, use the `{{#include ...}}` syntax. For example:

```cairo,editable
{{#include ../listings/hello/hello/src/lib.cairo}}
```

This will include the contents of the `listings/hello/hello/src/lib.cairo` file in the Markdown file.

## Theme

The custom theme is located in the `theme/` directory. The main template file is `theme/index.hbs`. This file defines the structure of the HTML pages.

The `theme/index.hbs` file includes the following elements:

- Header
- Sidebar
- Content
- Navigation

The `theme/index.hbs` file also includes the custom CSS and JavaScript files.

The `additional_css` and `additional_js` variables in `book.toml` specify the custom CSS and JavaScript files to include in the theme. See lines 9-15.

## Cairo Syntax Highlighting

The Cairo syntax highlighting is defined in the `theme/highlight.js` file. This file is based on the [Highlight.js](https://highlightjs.org/) library. The Cairo syntax highlighting definition is located at the end of the file. See lines 5563-5582.

The Cairo syntax highlighting definition was originally taken from [Scarb](https://github.com/software-mansion/scarb/tree/main/extensions/scarb-doc/theme).

## WASM-Cairo

The CBE website uses [wasm-cairo](https://github.com/cryptonerdcn/wasm-cairo) to run the Cairo code examples in the browser. The `wasm-cairo` package is located in the `theme/wasm-cairo/` directory. The current version of `wasm-cairo` is 2.8.2.

The `wasm-cairo` package and worker are included in the `additional_js` array in `book.toml` so that they are built with the HTML book. However, they are excluded from the built HTML in `theme/index.hbs` because they are only needed in the website source. See lines 10-15 in `book.toml` and lines 20-22 in `theme/index.hbs`.

## Tooling

- [mdbook](https://rust-lang.github.io/mdBook/index.html): Used to build the book.
- [Scarb](https://docs.swmansion.com/scarb/): The Cairo package manager.
- [Starknet Foundry](https://foundry-rs.github.io/starknet-foundry/): A testing framework for Cairo.
- [typos](https://github.com/crate-ci/typos): Used to automatically fix typos in the codebase.

## Updating Dependencies

To update the dependencies, use the `scarb update` command. This will update the dependencies in the `Scarb.toml` files.

## Formatting

To format the code examples, use the `cairo-listings format` command. This command is provided by the [cairo-listings](https://github.com/enitrat/cairo-listings) tool.

## Testing

To test the code examples, use the `cairo-listings verify` command. This command is provided by the [cairo-listings](https://github.com/enitrat/cairo-listings) tool. This command compiles and runs all the code examples in the book.

## Deployment

The CBE website is deployed to GitHub Pages using the `mdbook.yml` workflow. This workflow is triggered on every push to the `main` branch.

## Typos

The `typos` tool is used to automatically fix typos in the codebase. The configuration file for `typos` is `_typos.toml`. See lines 1-9. The `typos` tool is run as part of the CI process.

## Contributing

Contributions to the CBE codebase are welcome! To contribute, please fork the repository and submit a pull request.
