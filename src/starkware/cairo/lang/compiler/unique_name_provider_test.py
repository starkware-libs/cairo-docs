from starkware.cairo.lang.compiler.unique_name_provider import UniqueNameProvider, UniqueNameKind


def test_unique_name_provider_next():
    provider = UniqueNameProvider()
    assert provider.next(UniqueNameKind.Label) == "$lbl0"
    assert provider.next(UniqueNameKind.Var) == "$var1"
    assert provider.next(UniqueNameKind.Var) == "$var2"


def test_is_name_unique():
    assert UniqueNameProvider.is_name_unique("$lbl1")
    assert not UniqueNameProvider.is_name_unique("x")

    # This is false positive, but we are okay to live with it.
    assert UniqueNameProvider.is_name_unique("$Hello")
