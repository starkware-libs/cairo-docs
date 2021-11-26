from docutils import nodes
from docutils.parsers.rst import Directive


class Container(nodes.Admonition, nodes.Element):
    pass


def visit_container(self, node):
    self.visit_admonition(node)


def depart_container(self, node=None):
    self.depart_admonition(node)


class ToggleDirective(Directive):
    has_content = True
    required_arguments = 1

    def run(self):
        text = "\n".join(self.content)

        node = Container(text)
        self.state.nested_parse(self.content, self.content_offset, node)

        return [
            nodes.raw("", f"<details><summary><a>{self.arguments[0]}</a></summary>", format="html"),
            node,
            nodes.raw("", "</details>", format="html"),
        ]


def setup(app):
    app.add_directive("toggle", ToggleDirective)
    app.add_node(Container, html=(visit_container, depart_container))

    return {"version": "0.1"}
