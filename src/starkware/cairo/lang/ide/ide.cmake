python_lib(cairo_syntax_highlighting_lib
    PREFIX starkware/cairo/lang/ide
    FILES
    syntax_highlighting.py

    LIBS
    pip_pygments
)
