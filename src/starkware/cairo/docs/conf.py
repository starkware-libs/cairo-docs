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
import re
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


CAIRO_VERSION_FILE = os.path.join(os.path.dirname(__file__), "../lang/VERSION")
CAIRO_VERSION = open(CAIRO_VERSION_FILE).read().strip()

replacements = {
    "VERSION": CAIRO_VERSION,
    "ACCOUNT_ADDRESS": "0x078d796e87cfa496bffad27be9ed42f2709bd6e32a6366f842fdf38664a1412d",
    "ACCOUNT_ADDRESS_TRIMMED": "0x78d796e87cfa496bffad27be9ed42f2709bd6e32a6366f842fdf38664a1412d",
    "ACCOUNT_CLASS_HASH": "0x74acbf20e655c80c4fa16e3574489073e0093fd8b386d9614ab2d6cf5b866bf",
    "INTRO_CONTRACT_CLASS_HASH": (
        "0x1e2208b571b2cb68908f37a196ed5e391c8933a6db23bb3939acedee40d9b8a"
    ),
    "INTRO_CONTRACT_ADDRESS": "0x039564c4f6d9f45a963a6dc8cf32737f0d51a08e446304626173fd838bd70e1c",
    "INTRO_CONTRACT_ADDRESS_TRIMMED": (
        "0x39564c4f6d9f45a963a6dc8cf32737f0d51a08e446304626173fd838bd70e1c"
    ),
}


def substitute_variables(app, docname, source):
    # Allow skipping variable substitution (for example, this is used when generating codes.json).
    if os.environ.get("DONT_SUBSTITUTE_VARIABLES") == "1":
        return

    def replace_variable(match) -> str:
        variable_name = match.group(1)
        assert variable_name in replacements, (
            f"Unexpected variable name '{variable_name}'. "
            "Please make sure it is defined in src/starkware/cairo/docs/conf.py."
        )
        return replacements[variable_name]

    source[0] = re.sub("\$\[([a-zA-Z0-9_]+)\]", replace_variable, source[0])


def setup(app):
    app.connect("source-read", substitute_variables)
