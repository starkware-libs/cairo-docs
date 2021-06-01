import argparse
import json
import sys
from typing import Dict

from starkware.cairo.lang.cairo_constants import DEFAULT_PRIME
from starkware.cairo.lang.compiler.cairo_compile import (
    cairo_compile_add_common_args, cairo_compile_common, compile_cairo_files, get_module_reader)
from starkware.cairo.lang.compiler.error_handling import LocationError
from starkware.cairo.lang.compiler.identifier_definition import FunctionDefinition
from starkware.cairo.lang.compiler.module_reader import ModuleReader
from starkware.cairo.lang.compiler.preprocessor.pass_manager import PassManager
from starkware.cairo.lang.compiler.program import Program
from starkware.starknet.compiler.starknet_pass_manager import starknet_pass_manager
from starkware.starknet.compiler.starknet_preprocessor import (
    WRAPPER_SCOPE, StarknetPreprocessedProgram)
from starkware.starknet.public.abi import starknet_keccak
from starkware.starknet.services.api.contract_definition import (
    ContractDefinition, ContractEntryPoint)


def get_selector_from_name(func_name: str) -> int:
    return starknet_keccak(data=func_name.encode('ascii'))


def get_entry_points(program: Program) -> Dict[str, ContractEntryPoint]:
    """
    Returns a mapping from entry point name to (selector, offset).
    """
    wrapper_scope = program.identifiers.get_scope(WRAPPER_SCOPE)
    return {
        func_name: ContractEntryPoint(
            selector=get_selector_from_name(func_name),
            offset=func_def.pc)
        for func_name, func_def in wrapper_scope.identifiers.items()
        if isinstance(func_def, FunctionDefinition)}


def compile_starknet_files(
        files, debug_info: bool = False,
        disable_hint_validation: bool = False) -> ContractDefinition:
    module_reader = get_module_reader(cairo_path=[])
    program = compile_cairo_files(
        files=files,
        pass_manager=starknet_pass_manager(
            prime=DEFAULT_PRIME, read_module=module_reader.read,
            disable_hint_validation=disable_hint_validation,
        ),
        debug_info=debug_info)
    # Dump and load program, so that it is converted to the canonical form.
    program_schema = program.Schema()
    program = program_schema.load(data=program_schema.dump(obj=program))

    return ContractDefinition(
        program=program, entry_points=list(get_entry_points(program=program).values()))


def main():
    parser = argparse.ArgumentParser(description='A tool to compile StarkNet contracts.')
    parser.add_argument('--abi', type=argparse.FileType('w'), help="Output the contract's ABI.")
    parser.add_argument(
        '--disable_hint_validation', action='store_true', help='Disable the hint validation.')

    def pass_manager_factory(args: argparse.Namespace, module_reader: ModuleReader) -> PassManager:
        return starknet_pass_manager(
            prime=args.prime,
            read_module=module_reader.read,
            disable_hint_validation=args.disable_hint_validation)

    try:
        cairo_compile_add_common_args(parser)
        args = parser.parse_args()
        preprocessed = cairo_compile_common(args=args, pass_manager_factory=pass_manager_factory)
        assert isinstance(preprocessed, StarknetPreprocessedProgram)
        if args.abi is not None:
            json.dump(preprocessed.abi, args.abi, indent=4, sort_keys=True)
            args.abi.write('\n')
    except LocationError as err:
        print(err, file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
