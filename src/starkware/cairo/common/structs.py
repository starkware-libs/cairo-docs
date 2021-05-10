from collections import namedtuple
from typing import Dict, List, Optional

from starkware.cairo.lang.compiler.ast.code_elements import CodeElementFunction
from starkware.cairo.lang.compiler.identifier_utils import get_struct_definition
from starkware.cairo.lang.compiler.program import Program
from starkware.cairo.lang.compiler.scoped_name import ScopedName
from starkware.python.utils import WriteOnceDict


class CairoStructFactory:
    """
    Creates a CairoStructFactory that converts Cairo structs to python namedtuples.

    program is the Cairo program where the structs are defined.
    additional_imports is an optional list of additional import to allow using
    structs that are not in the main scope of the program.
    """

    def __init__(self, program: Program, additional_imports: Optional[List[str]] = None):
        self.program = program

        self.resolved_identifiers: Dict[ScopedName, ScopedName] = WriteOnceDict()
        if additional_imports is not None:
            for identifier_path in additional_imports:
                scope_name = ScopedName.from_string(identifier_path)
                # Call get_struct_definition to make sure scope_name is a struct.
                get_struct_definition(
                    struct_name=scope_name,
                    identifier_manager=program.identifiers)
                self.resolved_identifiers[scope_name[-1:]] = scope_name

    def _get_full_name(self, name: ScopedName):
        full_name = self.resolved_identifiers.get(name)
        if full_name is not None:
            return full_name

        return self.program.identifiers.search(
            accessible_scopes=[ScopedName.from_string('__main__'), ScopedName()],
            name=name).get_canonical_name()

    def build_struct(self, name: ScopedName):
        full_name = self._get_full_name(name)
        members = get_struct_definition(full_name, self.program.identifiers).members
        return namedtuple(full_name.path[-1], list(members.keys()))

    def get_struct_size(self, name: ScopedName) -> int:
        full_name = self._get_full_name(name)
        return get_struct_definition(full_name, self.program.identifiers).size

    def build_func_args(self, func: ScopedName):
        """
        Builds a struct the contains both the explicit and the implicit args of 'fund'.
        """
        full_name = self._get_full_name(func)

        implict_args = get_struct_definition(
            full_name + CodeElementFunction.IMPLICIT_ARGUMENT_SCOPE,
            self.program.identifiers).members
        args = get_struct_definition(
            full_name + CodeElementFunction.ARGUMENT_SCOPE, self.program.identifiers).members
        return namedtuple(
            f'{func[-1:]}_full_args', list({**implict_args, **args}))

    @property
    def structs(self):
        return CairoStructProxy(self, ScopedName())


class CairoStructProxy:
    def __init__(self, factory: CairoStructFactory, path: ScopedName):
        self.factory = factory
        self.path = path

    def __getattr__(self, name: str) -> 'CairoStructProxy':
        return CairoStructProxy(self.factory, self.path + name)

    def build(self):
        return self.factory.build_struct(self.path)

    def __call__(self, *args, **kwargs):
        return self.build()(*args, **kwargs)

    @property
    def size(self):
        return self.factory.get_struct_size(self.path)

    def from_ptr(self, runner, addr):
        """
        Interprets addr as a pointer to a struct of type path and creates the corresponding
        namedtuple.
        """
        named_tuple = self.build()

        return named_tuple(**{
            name: runner.vm_memory[addr + index]
            for index, name in enumerate(named_tuple._fields)})
