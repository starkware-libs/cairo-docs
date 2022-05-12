from starkware.cairo.lang.compiler.identifier_manager import IdentifierManager
from starkware.cairo.lang.compiler.preprocessor.default_pass_manager import ModuleCollector
from starkware.cairo.lang.compiler.preprocessor.for_loop.lowering import ForLoopLoweringStage
from starkware.cairo.lang.compiler.preprocessor.pass_manager import PassManager, PassManagerContext
from starkware.cairo.lang.compiler.preprocessor.preprocessor_test_utils import (
    CAIRO_TEST_MODULES,
    TEST_SCOPE,
)
from starkware.cairo.lang.compiler.test_utils import read_file_from_dict


def lower_and_format(code: str) -> str:
    manager = PassManager()
    manager.add_stage(
        "module_collector",
        ModuleCollector(
            read_module=read_file_from_dict(CAIRO_TEST_MODULES),
            additional_modules=[
                "starkware.cairo.lang.compiler.lib.registers",
            ],
        ),
    )
    manager.add_stage("for_loops_lowering", ForLoopLoweringStage())

    context = PassManagerContext(
        codes=[(code, "")], main_scope=TEST_SCOPE, identifiers=IdentifierManager(), start_codes=[]
    )

    manager.run(context)

    module = context.modules[-1]

    return module.format(allowed_line_length=100)
