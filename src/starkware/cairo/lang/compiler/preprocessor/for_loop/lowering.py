from typing import Optional

from starkware.cairo.lang.compiler.ast.arguments import IdentifierList
from starkware.cairo.lang.compiler.ast.code_elements import (
    CodeElementFor,
    CodeElementFunction,
    CodeBlock,
    CodeElement,
    CodeElementAllocLocals,
)
from starkware.cairo.lang.compiler.preprocessor.code_element_injecting_visitor import (
    CodeElementInjectingVisitor,
)
from starkware.cairo.lang.compiler.preprocessor.for_loop.clauses import (
    InClauseLowering,
    fetch_in_clause,
    fetch_bound_identifiers,
)
from starkware.cairo.lang.compiler.preprocessor.for_loop.errors import ForLoopLoweringError
from starkware.cairo.lang.compiler.preprocessor.pass_manager import PassManagerContext, VisitorStage


class ForLoopLoweringStage(VisitorStage):
    """
    Lowers for loops into calls to recursive functions.

    This stage is relatively high level and should be placed early in the compilation pass chain.
    """

    def __init__(self):
        super().__init__(visitor_factory=ForLoopLoweringVisitor, modify_ast=True)


class ForLoopLoweringVisitor(CodeElementInjectingVisitor):
    def __init__(self, context: PassManagerContext):
        super().__init__()
        self.context = context

    def _visit_default(self, elm):
        return elm

    def visit_CodeElementFor(self, elm: CodeElementFor):
        implicit_arguments = self._borrow_current_implicit_args()

        in_clause = fetch_in_clause(elm)
        bound_identifiers = fetch_bound_identifiers(elm)

        lowering = InClauseLowering(in_clause)

        _check_body_has_no_alloc_locals(elm.code_block)

        raise ForLoopLoweringError("For loops are not supported yet.", location=elm.location)

    def _borrow_current_implicit_args(self) -> Optional[IdentifierList]:
        for parent in reversed(self.parents):
            if isinstance(parent, CodeElementFunction):
                return parent.implicit_arguments
            elif not isinstance(parent, CodeElement):
                # Try our best to avoid jumping to irrelevant function which somehow
                # was put in parents stack.
                break

        return None


def _check_body_has_no_alloc_locals(code_block: CodeBlock):
    elms = code_block.code_elements
    if len(elms) > 0 and isinstance(elms[0].code_elm, CodeElementAllocLocals):
        raise ForLoopLoweringError(
            "alloc_locals is not needed in for loop body.",
            location=elms[0].location,
        )
