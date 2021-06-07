Syntax
======

This page summarizes the syntax of Cairo. For more information, refer to the "Hello, Cairo"
and "How Cairo Works" tutorials.

Comments
--------

Text can be inserted into the body of Cairo programs to document notes about the code.
The commented text is annotated with the ``#`` character. Text after this character is ignored by
the compiler.

.. tested-code:: cairo syntax_comments

    # Comments can be placed before, after or within code blocks.
    func main():
        # The hash character signals that this line is a comment.
        # This line will also not run as code. The next line will.
        let x = 9
        return ()
    end

Each comment spreads until the end of the line. In order to write a multiline comment, prefix all
the comment lines with ``#``.

Punctuation
-----------

The punctuation marks used in Cairo are described below:

*   ``(`` ``)`` (parentheses, round brackets). Used in a function declaration and in a tuple
    declaration.
*   ``{`` ``}`` (braces, curly braces, curly brackets). Used in a declaration of implicit
    arguments.
*   ``[`` ``]`` (brackets, square brackets). Standalone brackets represent the value at a
    particular address location (such as the allocation pointer, ``[ap]``). Brackets following a
    pointer or a tuple act as a subscript operator, where ``x[2]`` represents the element with
    index ``2`` in ``x``.
*   ``*`` Single asterisk. Refers to the pointer of an expression.
*   ``; ap++`` Used to increment the allocation pointer ``ap`` by one after the preceeding
    instruction has finished.
*   ``%`` Percent sign. Appears at the start of a directive, such as ``%builtins`` or ``%lang``.
*   ``%[`` ``%]`` Represents python literals.
*   ``%{`` ``%}`` Represents python hints.
*   ``_`` (underscore, underline). A placeholder to handle values that are not used, such as an
    unused function return value.

.. _syntax_type:

Type system
-----------

Cairo have the following types:

* ``felt`` -- a field element (see :ref:`field_elements`).
* ``MyStruct`` where ``MyStruct`` is a :ref:`struct <syntax_structs>` name.
* A tuple -- For example ``(a, b)`` where ``a`` and ``b`` are types (see :ref:`syntax_tuples`).
* ``T*`` where ``T`` is any type -- a pointer to type ``T``. For example: ``MyStruct*`` or
  ``felt**``.

Expressions
-----------

An expression in Cairo is one of the following:

* An integer literal (e.g., ``5``). Considered as of type ``felt``.
* An identifier (a :ref:`constant <syntax_const>` or a :ref:`reference <syntax_reference>`).
  E.g., ``my_identifier``, ``struct_name.member_name``, ``reference_name.member_name``.
* An address register: ``ap`` or ``fp``. Both have type ``felt``.
* ``x + y``, ``x - y``, ``x * y``, ``x / y``, ``-x`` where ``x`` and ``y`` are expressions.
* ``(x)`` where ``x`` is an expression -- same as ``x``
  (allows to control operator precedence in the expression).
* ``[x]`` where ``x`` is an expression -- represents the value of the member at the address ``x``.
  If ``x`` is of type ``T*`` then ``[x]`` is of type ``T``.
* ``&x`` where ``x`` is an expression -- represents the address of the expression ``x``.
  For example, ``&[x]`` is ``x``.
* ``cast(x, T)`` where ``x`` is an expression and ``T`` is a type -- same as ``x``, except that
  the type is changed to ``T``. For example, ``cast(10, MyStruct*)`` is ``10``, thought as a pointer
  to a ``MyStruct`` instance.

.. _syntax_const:

Constants
---------

You can define a constant value as follows:

.. tested-code:: cairo syntax_consts

    const CONSTANT_NAME = const_value

``const_value`` must be an expression that evaluates to an integer (field element) at compile time.
For example: ``5`` or ``4 + 2 * VAL`` where ``VAL`` is another constant.

.. _syntax_reference:

References
----------

A reference can be defined as follows:

.. tested-code:: cairo syntax_reference

    let ref_name : ref_type = ref_expr

where ``ref_type`` is a type and ``ref_expr`` is some Cairo expression.

A reference can be rebound, which means that different expressions may be assigned to the same
reference. See :ref:`reference_rebinding`. For example:

.. tested-code:: cairo syntax_reference_rebinding

    let a = 7  # a is initially bound to the expression 7.
    let a = 8  # a is now bound to the expression 8.

References can be revoked, which means that either:

*   There is a conflict between the expression assigned to a reference at two different places in
    the code (for example, due to an ``if`` statement. See example below).
*   The reference is ``ap``-based (e.g., temporary variables or return values from a function
    call), and the change in ap (between the definition and usage) cannot be deduced at compile
    time.

See :ref:`revoked_references` for more information.

.. tested-code:: cairo syntax_revoked_references

    func foo():
        let x = 0

        # The Prover may choose to enter the if or the else statement.
        if x == 0:
            let a = 23
        else:
            let a = 8
        end

        # A cannot be accessed, because it has conflicting values: 23 vs 8.

        return ()
    end

Locals
------

Local variables are defined using the keyword ``local``. Cairo places local variables relative to
the frame pointer (fp), and thus their values will not be revoked. See :ref:`local_vars` for more
information.

.. tested-code:: cairo syntax_local

    local a = 3

Any function that uses a local variable, must have the ``alloc_locals`` instruction at the beginning
of the function. This instruction is responsible for allocating the memory cells used by the local
variables.

.. tested-code:: cairo syntax_alloc_locals

    func foo():
        alloc_locals
        local a = 3
        return ()
    end

If the address of a local variable is needed, the value of a reference named ``fp`` must be set to
the value of the frame pointer. This can be done by the statement
``let (__fp__, _) = get_fp_and_pc()``. See :ref:`retrieving_registers` for more information.

.. _syntax_structs:

Structs
-------

You can define a struct as follows:

.. tested-code:: cairo structs

    struct MyStruct:
        member first_member : felt
        member second_member : MyStruct*
    end

Each member is defined using the syntax ``member <member_name> : <member_type>``.

The struct has a size, which is the sum of the sizes of its members.
The size can be retrieved using ``MyStruct.SIZE``.

Each member is assigned an offset from the beginning of the struct.
The first member is assigned offset 0,
the second is assigned offset according to the size of the first member and so on.
The offset can be retrieved using ``MyStruct.member_name``.
For example, ``MyStruct.first_member == 0`` and ``MyStruct.second_member == 1``
(since the size of ``felt`` is 1).

Struct constructor
------------------

Once a struct has been defined, a constructor can be used to declare an instance of that struct as
follows:

.. tested-code:: cairo struct-constructor0

    let struct_instance = MyStruct(
        first_member=value0, second_member=value1)

Members must be declared in order of appearance. Struct constructors may be nested as follows:

.. tested-code:: cairo struct-constructor1

    let struct1 = A(v=value0, w=B(x=value1, y=value2))

Where ``A`` is a struct with members ``v`` and ``w`` and ``B`` is a struct with members ``x`` and
``y``.

.. _syntax_tuples:

Tuples
------

A tuple is a finite, ordered, unchangeable list of elements. It is represented as a
comma-separated list of elements enclosed by parentheses (e.g., ``(3, x)``).
Their elements may be of any combination of valid :ref:`types <syntax_type>`. A tuple
that contains only one element must be defined in one of the two following ways: the element is
a named tuple or has a trailing comma. When a tuple is passed as an argument, the type of each
element may be specified on a per-element basis (e.g., ``my_tuple : (felt, felt, MyStruct)``).
Tuple values may be accessed with a zero-based index in brackets ``[index]``, including access to
nested tuple elements as shown below.

.. tested-code:: cairo syntax_tuples

    # A tuple with three elements.
    local tuple0 : (felt, felt, felt) = (7, 9, 13)
    local tuple1 : (felt) = (5,)  # (5) is not a valid tuple.
    # A named tuple does not require a trailing comma.
    local tuple2 : (felt) = (a=5)
    # Tuple contains another tuple.
    local tuple3 : (felt, (felt, felt, felt), felt) = (1, tuple0, 5)
    local tuple4 : ((felt, (felt, felt, felt), felt), felt, felt) = (
        tuple3, 2, 11)
    let a = tuple0[2]  # let a = 13.
    let b = tuple4[0][1][2]  # let b = 13.

.. test::

    from starkware.cairo.lang.compiler.cairo_compile import compile_cairo

    PRIME = 2**64 + 13
    code = codes['syntax_tuples']
    code = f'func main():\n alloc_locals \n {code}\n ret \n end'
    compile_cairo(code, PRIME)

Functions
---------

You can define a function as follows:

.. tested-code:: cairo syntax_function

    func func_name{implicit_arg1 : felt, implicit_arg2 : felt*}(
            arg1 : felt, arg2 : MyStruct*) -> (
            ret1 : felt, fet2 : felt):
        # Function body.
    end

The implicit argument part ``{implicit_arg1 : felt, implicit_arg2 : felt*}``
and the return value ``(ret1 : felt, fet2 : felt)`` are optional.

For more information about functions see :ref:`functions` and :ref:`implicit_arguments`.

Return statement
----------------

A function must end with a ``return`` statement, which takes the following form:

.. tested-code:: cairo syntax_function_return

    return (ret1=val1, ret2=val2)


Call statement
--------------

You can call a function in the following ways:

.. tested-code:: cairo syntax_function_call

    foo(x=1, y=2)  # (1)
    let x = foo(x=1, y=2)  # (2)
    let (ret1, ret2) = foo(x=1, y=2)  # (3)
    return foo(x=1, y=2)  # (4)

Option (1) can be used when there is no return value or it should be ignored.

Option (2) binds ``x`` to the return value struct.

Option (3) unpacks the return value into ``ret1`` and ``ret2``.

Option (4) is a tail recursion -- after ``foo`` returns, the calling function returns the
same return value.

Library imports
---------------

Library functions are imported at the top of the file or right below the ``%builtins`` directive if
it is used. The statement consists of the module name and the functions to ``import`` from it.
Multiple functions from the same library can be separated by commas. Functions from different libraries
are imported on different lines. Cairo searches each module in a default directory path and in
any additional paths specified at compile time. See :ref:`import_search_path` for more information.

.. tested-code:: cairo syntax_library_imports

    %builtins output pedersen
    from starkware.cairo.common.math import (
        assert_not_zero, assert_not_equal)
    from starkware.cairo.common.registers import get_ap
