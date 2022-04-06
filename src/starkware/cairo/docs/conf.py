# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html.

# Path setup.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import sys
from typing import List

sys.path.insert(0, os.path.abspath("."))

is_starknet = os.environ.get("GENERATE_STARKNET_DOCS") == "1"

# Project information.

project = "StarkNet" if is_starknet else "Cairo"
copyright = "2021, StarkWare Industries Ltd."
author = "StarkWare Industries Ltd."

# General configuration.
html_show_sourcelink = False
html_copy_source = False

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.ifconfig",
    "cairo_syntax_highlighting",
    "testing",
    "toggle",
]

html_context = {
    "main_url": "https://starknet.io/" if is_starknet else "https://cairo-lang.org/",
    "google_analytics_tag": "G-7Z0075QZ3C" if is_starknet else "G-0ZJLBV4KE2",
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns: List[str] = []


# Options for HTML output.

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "alabaster"
html_favicon = "sn_favicon.png" if is_starknet else "favicon.svg"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_theme_options = {
    "github_user": "starkware-libs",
    "github_repo": "cairo-lang",
    "github_button": "true",
    "github_type": "star",
}

if is_starknet:
    html_css_files = [
        "https://starknet.io/wp-content/themes/starknet/sphinx.css",
    ]
