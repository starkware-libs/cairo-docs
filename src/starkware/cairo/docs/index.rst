Cairo Documentation
===================

The Cairo documentation consists of two tutorials:
"Hello, Cairo" and "How Cairo Works".

"Hello, Cairo" describes Cairo for the programmer who wishes to understand what Cairo can do
hands-on, and start writing programs in Cairo.
"How Cairo Works" starts from the low-level assembly-like version of Cairo and
explains the syntactic sugar mechanisms applied by the Cairo compiler,
which turns Cairo to a high-level-like language.

The "Hello, Cairo" tutorial contains several references to "How Cairo Works"
for those who want to get a better understanding of those topics.

**Where should I start?**
It depends on whether you want to start writing programs (in which case, start with "Hello, Cairo")
or understand Cairo's internals from the ground up (in which case, start with "How Cairo Works").
If you're still unsure, we recommend that you start from "Hello, Cairo" (and if
at any point you feel you want to get a deeper understanding, jump to the relevant section
of "How Cairo Works").

.. toctree::
    :hidden:

    self

.. toctree::
    :maxdepth: 1

    quickstart

.. toctree::
    :maxdepth: 2

    hello_cairo/index
    how_cairo_works/index
    sharp
