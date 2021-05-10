from sphinx.highlighting import lexers

from starkware.cairo.lang.ide.syntax_highlighting import CairoLexer


def setup(app):
    lexers['cairo'] = CairoLexer(startinline=True)
