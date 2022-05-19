import dataclasses

import starkware.cairo.lang.compiler.preprocessor.preprocessor_test_utils as utils
from starkware.cairo.lang.compiler.ast.arguments import IdentifierList
from starkware.cairo.lang.compiler.ast.code_elements import (
    CodeBlock,
    CodeElementReference,
    CodeElementLocalVariable,
    CodeElementFunction,
    CodeElementReturn,
)
from starkware.cairo.lang.compiler.ast.expr import ExprIdentifier, ArgList, ExprAssignment
from starkware.cairo.lang.compiler.ast.expr_func_call import ExprFuncCall
from starkware.cairo.lang.compiler.ast.rvalue import RvalueCall, RvalueFuncCall
from starkware.cairo.lang.compiler.ast.types import TypedIdentifier
from starkware.cairo.lang.compiler.identifier_manager import IdentifierManager
from starkware.cairo.lang.compiler.preprocessor.code_element_injecting_visitor import (
    CodeElementInjectingVisitor,
    CodeElementInjection,
)
from starkware.cairo.lang.compiler.preprocessor.default_pass_manager import ModuleCollector
from starkware.cairo.lang.compiler.preprocessor.pass_manager import (
    PassManager,
    PassManagerContext,
    VisitorStage,
)
from starkware.cairo.lang.compiler.test_utils import read_file_from_dict


def visit_and_format(code: str, visitor_factory) -> str:
    manager = PassManager()
    manager.add_stage(
        "module_collector",
        ModuleCollector(
            read_module=read_file_from_dict(utils.CAIRO_TEST_MODULES),
            additional_modules=[
                "starkware.cairo.lang.compiler.lib.registers",
            ],
        ),
    )
    manager.add_stage("injection", VisitorStage(visitor_factory=visitor_factory, modify_ast=True))

    context = PassManagerContext(
        codes=[(code, "")],
        main_scope=utils.TEST_SCOPE,
        identifiers=IdentifierManager(),
        start_codes=[],
    )

    manager.run(context)

    module = context.modules[-1]

    return module.format(allowed_line_length=100)


def test_code_element_injection():
    code = """\
func main():
    alloc_locals
    let x = 5
    local y = 10
    ret
end
"""

    class TestVisitor(CodeElementInjectingVisitor):
        def __init__(self, _context):
            super().__init__()

        def _visit_default(self, obj):
            return obj

        def visit_CodeElementLocalVariable(self, elm: CodeElementLocalVariable):
            typed_identifier = TypedIdentifier(
                identifier=ExprIdentifier(name="foo"),
                expr_type=None,
            )

            return CodeElementInjection.from_code_block(
                CodeBlock.from_code_elements(
                    [
                        CodeElementReference(
                            typed_identifier=typed_identifier,
                            expr=elm.expr,
                        ),
                        CodeElementLocalVariable(
                            typed_identifier=elm.typed_identifier,
                            expr=typed_identifier.identifier,
                        ),
                    ]
                )
            )

    assert (
        visit_and_format(code, TestVisitor)
        == """\
func main():
    alloc_locals
    let x = 5
    let foo = 10
    local y = foo
    ret
end
"""
    )


def test_function_injection():
    code = """\
func main():
    alloc_locals
    let x = 5
    local y = 10
    ret
end
func bar():
    return (99)
end
"""

    class TestVisitor(CodeElementInjectingVisitor):
        def __init__(self, _context):
            super().__init__()

        def _visit_default(self, obj):
            return obj

        def visit_CodeElementLocalVariable(self, elm: CodeElementLocalVariable):
            func_name = ExprIdentifier(name="foo")

            self.inject_function(
                CodeElementFunction(
                    element_type="func",
                    identifier=func_name,
                    arguments=IdentifierList.from_identifiers([]),
                    implicit_arguments=None,
                    returns=None,
                    decorators=[],
                    code_block=CodeBlock.from_code_elements(
                        [
                            CodeElementReturn(
                                exprs=[
                                    ExprAssignment(
                                        identifier=None,
                                        expr=elm.expr,
                                    )
                                ]
                            )
                        ]
                    ),
                )
            )

            return dataclasses.replace(
                elm,
                expr=ExprFuncCall(
                    rvalue=RvalueFuncCall(
                        func_ident=func_name,
                        arguments=ArgList.from_args([]),
                        implicit_arguments=None,
                    )
                ),
            )

    assert (
        visit_and_format(code, TestVisitor)
        == """\
func main():
    alloc_locals
    let x = 5
    local y = foo()
    ret
end
func foo():
    return (10)
end
func bar():
    return (99)
end
"""
    )
