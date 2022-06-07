from starkware.cairo.lang.compiler.ast.code_elements import (
    CodeElementFor,
    CodeElement,
    CodeElementAllocLocals,
    CodeElementReturn,
    CodeElementInstruction,
    CodeElementTailCall,
)
from starkware.cairo.lang.compiler.ast.instructions import RetInstruction, InstructionBody
from starkware.cairo.lang.compiler.ast.visitor import Visitor
from starkware.cairo.lang.compiler.preprocessor.for_loop.errors import ForLoopLoweringError


def lint_for_loop(elm: CodeElementFor):
    linter = _ForLoopLinter()
    linter.visit(elm.code_block)


class _ForLoopLinter(Visitor):
    def _visit_default(self, obj):
        assert isinstance(obj, (CodeElement, InstructionBody))

    def visit_CodeElementFor(self, elm: CodeElementFor):
        pass

    def visit_CairoModule(self, module):
        pass

    def visit_CodeElementFunction(self, elm):
        pass

    def visit_CodeElementInstruction(self, elm: CodeElementInstruction):
        self.visit(elm.instruction.body)

    def visit_CodeElementAllocLocals(self, elm: CodeElementAllocLocals):
        raise ForLoopLoweringError(
            "alloc_locals is not allowed in the body of a for loop.",
            location=elm.location,
        )

    def visit_CodeElementReturn(self, elm: CodeElementReturn):
        raise ForLoopLoweringError(
            "return is not allowed in for loop body.",
            location=elm.location,
        )

    def visit_CodeElementTailCall(self, elm: CodeElementTailCall):
        raise ForLoopLoweringError(
            "return is not allowed in for loop body.",
            location=elm.location,
        )

    def visit_RetInstruction(self, instruction: RetInstruction):
        raise ForLoopLoweringError(
            "ret is not allowed in for loop body.",
            location=instruction.location,
        )
