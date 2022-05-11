from starkware.cairo.lang.compiler.preprocessor.preprocessor_test_utils import PRIME, preprocess_str
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


def test_code_that_uses_unique_name_provider_compiles():
    program = preprocess_str(
        code="""
namespace B:
    func foo(x, y) -> (res):
        if x == 0:
            if y == 0:
                return (res=0)
            else:
                return (res=1)
            end
        else:
            if y == 0:
                return (res=2)
            else:
                return (res=3)
            end
        end
    end
end
func main():
    B.foo(1, 2)
    ret
end
""",
        prime=PRIME,
    )
    assert (
        program.format()
        == """\
jmp rel 10 if [fp + (-4)] != 0
jmp rel 5 if [fp + (-3)] != 0
[ap] = 0; ap++
ret
[ap] = 1; ap++
ret
jmp rel 5 if [fp + (-3)] != 0
[ap] = 2; ap++
ret
[ap] = 3; ap++
ret
[ap] = 1; ap++
[ap] = 2; ap++
call rel -22
ret
"""
    )
