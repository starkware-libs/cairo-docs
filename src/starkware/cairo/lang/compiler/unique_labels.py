from contextlib import contextmanager
from contextvars import ContextVar
from typing import Optional


# Dollar is not a valid identifier character in Cairo, thus we can be sure,
# nobody will try to create colliding identifiers in source code.
ANONYMOUS_LABEL_PREFIX = "$"

counter_ctx_var: ContextVar[Optional[int]] = ContextVar("counter", default=None)


@contextmanager
def unique_labelling_context():
    token = counter_ctx_var.set(0)
    try:
        yield
    finally:
        counter_ctx_var.reset(token)


def unique_name() -> str:
    """
    Returns new compilation-unique name which is guaranteed to be impossible to declare
    by source code.
    """
    counter = counter_ctx_var.get()
    assert counter is not None, "Unique labelling context has not been set up."
    assert counter >= 0
    counter_ctx_var.set(counter + 1)
    return f"{ANONYMOUS_LABEL_PREFIX}{counter}"


def is_anonymous_name(name: str) -> bool:
    """
    Returns ``True`` if the given label seems to have been generated.
    """
    return name.startswith(ANONYMOUS_LABEL_PREFIX)
