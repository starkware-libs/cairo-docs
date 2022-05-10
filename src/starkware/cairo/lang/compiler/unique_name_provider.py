import enum
from enum import Enum


@enum.unique
class UniqueNameKind(Enum):
    Label = "Lbl"
    Func = "Func"
    Var = "Var"


class UniqueNameProvider:
    """
    Provides new compilation-unique names.

    The only instance of this class should be maintained by ``PassManagerContext`` and use this
    object to obtain names for any anonymous code elements like labels, variables or functions.
    """

    # Dollar is not a valid identifier character in Cairo, thus we can be sure,
    # nobody will try to create colliding identifiers in source code.
    PREFIX = "$"

    counter: int

    def __init__(self):
        self.counter = 0

    def next(self, kind: UniqueNameKind) -> str:
        """
        Returns new compilation-unique name which is guaranteed to be impossible to declare
        by source code.

        The ``kind`` enum is only used to denote purpose of generated names when debugging.
        All unique names, no matter what kind, use one shared global counter.
        """
        counter = self.counter
        self.counter += 1
        return f"{self.PREFIX}{kind.value}{counter}"

    @classmethod
    def is_name_unique(cls, name: str) -> bool:
        """
        Returns ``True`` if the given label seems to have been generated.
        """
        return name.startswith(cls.PREFIX)
