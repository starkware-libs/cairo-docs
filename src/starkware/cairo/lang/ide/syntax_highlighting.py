from pygments import token
from pygments.lexer import RegexLexer, bygroups, using, words
from pygments.lexers.python import PythonLexer

KEYWORDS = [
    "func",
    "struct",
    "namespace",
    "end",
    "call",
    "ret",
    "jmp",
    "if",
    "let",
    "const",
    "import",
    "from",
    "as",
    "abs",
    "rel",
    "static_assert",
    "local",
    "tempvar",
    "felt",
    "return",
    "assert",
    "member",
    "cast",
    "else",
    "alloc_locals",
    "with",
    "with_attr",
    "nondet",
    "dw",
]


class CairoLexer(RegexLexer):
    name = "cairo"

    tokens = {
        "root": [
            (words(KEYWORDS, prefix=r"\b", suffix=r"\b"), token.Keyword),
            (words(("SIZEOF_LOCALS", "SIZE"), prefix=r"\b", suffix=r"\b"), token.Literal),
            (r"%builtins|%lang", token.Keyword),
            (words(("ap", "fp"), prefix=r"\b", suffix=r"\b"), token.Name.Entity),
            (r"!=|->", token.Operator),
            (r"[+\-*/&]", token.Operator),
            (r"[:;,.=\[\]\(\)\{\}]", token.Punctuation),
            (r"-?0x[0-9a-fA-F]+", token.Number),
            (r"-?[0-9]+", token.Number),
            (r"[a-zA-Z_][a-zA-Z_0-9]*", token.Text),
            (r"#.*", token.Comment),
            (
                r"(%\{)((?:.|\n)*?)(%\})",
                bygroups(token.Punctuation, using(PythonLexer), token.Punctuation),
            ),
            (
                r"(%\[)((?:.|\n)*?)(%\])",
                bygroups(token.Punctuation, using(PythonLexer), token.Punctuation),
            ),
            (r"@\w+", token.Keyword),
            (r"<[a-zA-Z0-9 _\-]+>", token.Comment),
            (r" ", token.Text),
            (r"'[^']*'", token.String),
        ]
    }
