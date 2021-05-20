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

* ``(`` ``)`` Parentheses: Also known as round brackets. Used in function declaration and in tuple declaration.
* ``{`` ``}`` Braces: Also known as curly braces or curly brackets. Used in declaration of implicit arguments
* ``[`` ``]`` Brackets: Also known as square brackets. Identifies the value at a particular address register, e.g. the allocation pointer ``[ap]``.
* ``*`` Single asterisk. Refers to the pointer of an expression.
* ``**`` Double asterisk. Refers to the pointer of a ``felt*`` expression.
* ``;`` Semicolon. Used to designate an address register instruction, e.g. ``[ap];`` indicates that an operation is being performed on the allocation pointer.
* ``++`` Double plus. An increment on an address register, e.g. ``ap++`` increments the allocation pointer by one.
* ``%`` Percent sign. Used as part of the ``%builtins`` directive.
* ``%[`` ``%]`` Percent sign and brackets block. Identifies python literals.
* ``%{`` ``%}`` Percent sign and braces block. Identifies python hints.
* ``<`` ``>`` Chevrons: Also known as angle brackets. Used in Cairo documentation to identify a single element, as in ``<one placeholder element>``. Not used in Cairo code.
* ``_`` Underscore: Also known as underline. A placeholder to handle values not used, such as an unused function returned value.

.. _syntax_type:

Type system
-----------

Cairo have the following types:

* ``felt`` -- a field element (see :ref:`field_elements`).
* ``MyStruct`` where ``MyStruct`` is a :ref:`struct <syntax_structs>` name.
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

Type declaration
----------------

An expression can be declared to be of a certain :ref:`type <syntax_type>` by using a colon in the
format ``<expression> : <type>``. In the code below, ``a``, ``b`` and ``c`` are declared to be three
different types.

.. tested-code:: cairo syntax_type_declaration

    alloc_locals
    local a : felt # felt
    local b : MyStruct # Struct
    local c : MyStruct* # Pointer to a struct

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

Reference can be rebound, which means that an expression can be reassigned to a different value.
See :ref:`reference_rebinding`.

.. tested-code:: cairo syntax_reference_rebinding

    let a = 7 # A is initially bound to the value 7.
    let a = 8 # A is now bound to the value 8.

References can be revoked, which means that if there is a conflict between the value assigned to an
expression at different points branched code, the reference becomes unavailable. See
:ref:`revoked_references`. for more information.

.. tested-code:: cairo syntax_revoked_references

    func foo():
        let x == 0
        let a = 7 # A is initially bound to the value 7.

        jmp case_2 if x == 0

        case_1:
        let a = 23
        jump common_final_path:

        case_2:
        let a = 8

        common_final_path:
        # A cannot be accessed, because it has conflicting values: 23 vs 8.

        return()
    end

.. _syntax_structs:

Locals
------

Local expressions are defined with the term ``local``. Local variables cannot be revoked, unlike
references. See :ref:`local_vars` for more information.

.. tested-code:: cairo syntax_local

    local a = 3

The instruction ``alloc_locals`` must be placed at the start of any function that uses locals.

.. tested-code:: cairo syntax_alloc_locals

    func foo():
        alloc_locals
        local a = 3
        return ()
    end

Structs
-------

You can define a struct as follows:

.. tested-code:: cairo syntax_structs

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

Tuples
------

Finite ordered lists called tuples contain elements within a pair of parentheses ``(`` ``)``.
Elements may any combination of valid :ref:`types <syntax_type>`, for example, a ``felt`` and two
structs. They cannot be modified after declaration and are defined using a local variable as
follows:

.. tested-code:: cairo syntax_tuples

    # A tuple with two elements
    local TupleOne = (7, 9)

    # A tuple with three elements
    local TupleTwo = (7, 9, 13)

A tuple may be named and defined by the elements it contains. This may be useful where a function
has arguments in the form of a tuple. Below function returns a tuple defined with two ``felt``
expressions.

.. tested-code:: cairo syntax_tuple_empty

    func MyFunc() -> (TupleResult : (felt, felt)):
        alloc_locals
        let a = 3
        let b = 9
        local MyTuple = (a, b)
        return (TupleResult = MyTuple)
    end

Tuple values may be accessed as follows:

.. tested-code:: cairo syntax_tuple_assignment

    local TupleOne = (7, 9)
    let a = TupleOne.0 # Equivalent to: let a = 7.
    let b = TupleOne.1 # Equivalent to: let b = 9.

Pointers
--------

The address of an expression is accessed using a pointer. An address may exist before a value has
been stored at that expression. For example, where a function accepts an argument of a certain type,
a pointer to that type allows the compiler to allocate memory appropriately.

Consider the following expressions defined some Cairo program:

* ``MyFelt``: A field element with a particular value, such as ``7``.
* ``MyStruct``: A struct with defined members (not outlined here)
* ``MyExp``: An expression whose type will be defined with ``MyExp : <type>`` in the examples below. ``MyExp`` may be read as "My Expression".

Expressions, pointers and their interpretation are outlined below:

* ``felt``. A value.
    * ``MyExp : felt`` reads as "``MyExp`` is a ``felt`` and in practice, an integer".
* ``felt*``. A pointer to a value.
    * ``MyExp : felt*`` reads as "``MyExp`` is the location where one or more ``felt`` s are stored, which can be used to define a list".
* ``felt**``. A pointer to a pointer.
    * ``MyExp : felt**`` reads as "``MyExp`` is is the location where one or more pointers are stored, which can be used to define a list of lists".
* ``MyFelt``. A value, in this instance ``7``.
    * The code ``MyExp : MyFelt`` is not used because ``MyExp`` type cannot be assigned to a particular ``felt`` instance.
* ``MyFelt*``. A pointer to the value ``7``.
    * ``MyExp : MyFelt*`` reads as "``MyExp`` is the location where ``MyFelt`` is stored, which may be used if ``MyFelt`` is extended to a list with ``7`` as the first value".
* ``MyFelt**``. A pointer to a pointer.
    * ``MyExp : MyFelt**`` reads as "``MyExp`` is the location where the ``MyFelt*`` pointer is stored, which can be used to construct a list of lists".
* ``[MyFelt]``. A value at address ``MyFelt``.
    * This expression is not used because ``MyFelt`` is a value, not an address.
    * It follows that the expression ``MyExp : [MyFelt]`` is not used.
* ``[MyFelt*]``. A value at the pointer ``MyFelt*``.
    * If MyFelt* is being used to define a list, this statement reads as "The value of the first item in the list which starts at ``Myfelt*``.
    * ``MyExp : [MyFelt*]`` is not used because ``[MyFelt*]`` is a value.
* ``[MyFelt* + 1]``. A value at the pointer one slot after ``MyFelt*``.
    * If ``MyFelt*`` is being used to define a list, this statement reads as "The value of the second item in the list which starts at ``Myfelt*``.
* ``MyStruct``. A value, in this instance a struct with defined values.
    * The code ``MyExp : MyStruct`` is not used because ``MyExp`` type cannot be assigned to a particular struct instance.
* ``MyStruct*``. A pointer to a struct value.
    * ``MyExp : MyStruct*`` reads as "``MyExp`` is of type ``MyStruct``".
    * ``MyExp`` points to where ``MyStruct`` is stored and has the same member structure as ``MyStruct``.
    * ``MyExp`` has members may be populated with values.
* ``MyStruct**`` . A pointer (to a pointer).
    * ``MyExp : MyStruct**`` reads as "``MyExp`` is a pointer to where ``MyStruct*`` pointers are stored, and can be used to represent a list of structs". See :ref:`transaction_loop_list`.
* ``[MyStruct]``. A value at the struct ``MyStruct``.
    * This expression is not used because structs occupy multiple memory slots which can be addressed individually.
* ``[MyStruct*]``. A value at the pointer to the first memory address of ``MyStruct*``.
    * Reads as "The value at the first memory slot that ``MyStruct`` occupies".
    * ``MyExp : [MyStruct*]`` is not used because ``[MyStruct*]`` is a particular value not a type.
* ``[MyStruct* + 1]``. A value at the pointer to the second memory address of ``MyStruct*``.
    * Reads as "The value at the second memory slot that ``MyStruct`` occupies".
* ``[MyStruct**]``. A value at the pointer to the first memory address of the pointer ``MyStruct**``.
    * Reads as "The pointer to the first struct in the list of structs."
    * This pointer can be used to reference the values within that first struct.
    * ``MyExp : [MyStruct**]`` is not used because ``[MyStruct**]`` is a particular value.
* ``[MyStruct** + 1]``. A value at the pointer to the second memory address of the pointer ``MyStruct**``.
    * Reads as "The pointer to the second struct in the list of structs".
    * This pointer can be used to reference the values within that second struct.

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

Function inputs
---------------

A function can accept arguments as inputs. Arguments may be either positional or named, where
positional arguments are identified by the order they appear in the calling function. Positional
arguments must appear before named arguments.

.. tested-code:: cairo syntax_function_inputs

    func my_function(a,b):
        return()
    end

    func main():
        # Permitted
        my_function(2,b=3) # positional, named
        my_function(2,3) # positional, positional
        my_function(a=2,b=3) # named, named

        # Not permitted
        # my_function(a=2,3) # named, positional
        return()
    end

Functions can specify that an input be of a certain type. The function below accepts two arguments,
``a``, a value of type ``felt`` and ``b``, the address of a felt value.

.. tested-code:: cairo syntax_function_inputs_typed

    func my_function(a:felt,b:felt*):

Return statement
----------------

A function must end with a ``return`` statement, which takes the following form:

.. tested-code:: cairo syntax_function_return

   return (ret1=val1, ret2=val2)

Function outputs
----------------

A function can return arguments to the parent function that called it. The arguments expected are
designated by the ``-> ()`` expression. The value of the arguments are defined in the return
statement of the function. Arguments may be either positional or named, where positional arguments
are identified by the order they appear in the calling function. Positional arguments must appear
before named arguments.

.. tested-code:: cairo syntax_function_outputs

    func my_function() -> (a, b):
        # Permitted
        return (2, b=3) # positional, named

        # Not permitted
        # return (a=2, 3) # named, positional
    end

    func main():
        let (val_a, val_b) = my_function()
        return()
    end

Functions can specify that an output be of a certain type. The function below returns two arguments,
``a``, a value of type ``felt`` and ``b``, the address of a felt value.

.. tested-code:: cairo syntax_function_outputs_typed

    func my_function() -> (a : felt, b : felt*):

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

Unpacking
---------

The values returned by a function can be ignored or bound to either a reference or local expression.
The ``_`` character is used to handle returned values that are ignored. Consider function ``foo()``
that returns two values, ``7`` and ``5`` in that order.

.. tested-code:: cairo syntax_unpacking

    let (a, b) = foo() # Two references bound (a=7, b=5).

    let (_, b) = foo() # One reference bound (b=5).

    let (local a, local b) = foo() # Two locals bound (a=7, b=5)

    let (local a, _) = foo() # One local bound (a=7)

For more information see :ref:`return_values_unpacking`.

Literals
--------

Python code can be invoked with the ``%[`` ``%]`` block, where all contained code will be converted
to memory at compile time and cannot be modified during proof construction. See :ref:`literals` for
more information.

.. tested-code:: cairo syntax_literals

    let a = %[ 2 * 2 %] # a = 2 x 2 = 4

    let b = %[ pow(8,2) %] # b = 8 to the power 3 = 512

    let c = %[ len([6,7,8,9] %] # c = length of the list [6,7,8,9] = 4

Hints
-----

Python code can be invoked with the ``%{`` ``%}`` block, where all contained code will be available
to be modified during proof construction. See :ref:`hints` for more information.

.. tested-code:: cairo syntax_hints

    %{ a = 2 * 2 %}

Hints may span multiple lines.

.. tested-code:: cairo syntax_hints_multiline

    %{
        a = 2 * 2
        b = a * 5
    %}

Hints may access and modify Cairo expressions that preceed the hints block with the ``ids.``
expression.

.. tested-code:: cairo syntax_hints_multiline

    let a = 4
    %{
        b = 100 * ids.a # cairo expression a is accessed.
        ids.a = b # cairo expression a is modified.
    %}

Program input
-------------

Program inputs are declared within Hints with the expression program_input['']. The term within
the square brackets is an expression in single quotes that identifies the key of a key/value pair.
Thekey/value pair are specified in the .json document provided when the Cairo program is run.
See :ref:`program_inputs` for more information.

.. tested-code:: cairo syntax_program_inputs

    %{
        # Sets the python varible a to a list of user_ids provided in the .json file.
        a = program_input['user_ids']
    %}

Program output
--------------

Cairo programs can produce outputs that a smart contract can verify. These outputs require the
``output`` builtin. The program can product multiple outputs with calls to the ``serialize_word()``
function. Outputs can also be structs that are saved to an output file.
See :ref:`program_output` for more information.

The following program outputs two values, 7 and 13.

.. tested-code:: cairo syntax_program_output

    %builtins output

    from starkware.cairo.common.serialize import serialize_word

    func main{output_ptr: felt*}():
        let a = 7
        let b = 13
        serialize_word(a)
        serialize_word(b)
        return()
    end

The following program excerpt outlines how a program may output a struct by referencing its size
and location in memory.

.. tested-code:: cairo syntax_program_output_struct

    %builtins output

    # Code defining the struct goes here

    func main{output_ptr: felt*}():
        # Code defining the struct contents goes here

        let output = cast(output_ptr, MyStruct*)
        let output_ptr = output_ptr + Mystruct.SIZE

        return()
    end

Builtins
--------

Builtins are included at the top of the cairo code file. They are invoked with the  ``%builtins``
directive followed by the name of the builtin. Additional builtins can be included on the same
line with each new builtin separated by a space.

.. tested-code:: cairo syntax_builtins

    %builtins output pedersen

    function main():
        return()
    end

For more informaiton about builtins see :ref:`builtins`

Library imports
---------------

Library functions are imported at the top of cairo code file, below ``Builtins`` if they are used. The
statement describes where in the library the function is ``from`` and which function to ``import``.
Multiple functions the same library can be separated by commas. Functions from different libraries
are imported on a new line.

.. tested-code:: cairo syntax_library_imports

    # Builtins would be included here
    from starkware.cairo.common.math import assert_not_zero, assert_not_equal
    from starkware.cairo.common.registers import get_ap

    func main():
        assert_not_zero(10)
        assert_not_equal(2,3)
        let empty_memory_slot = get_ap()
        return ()
    end

Implicit arguments
------------------

Implicit arguments are specified as part of the function expression and are designated by
braces ``{}``. Expressions within the braces are passed between functions. If no implicit
arguments are required the braces can be omitted.

.. tested-code:: cairo syntax_implicit_arguments

    %builtins output

    func main{output_ptr}():
        return ()
    end

For more informaiton about builtins see :ref:`implicit_arguments`

Jumps
-----

Cairo programs can include special branch points in code called jumps. The Prover may choose to
follow the jump instructions to arrive at a valid proof more readily, but they do not necessarily
have to do so. Jumps contain all of the following: A ``jump`` expression, a ``case_not_met`` name,
a ``case_met_name`` and an ``if`` statement.

.. tested-code:: cairo syntax_jumps

    func MyFunction() -> (result):
        let a = 2

        jump case_true if a == 3

        case_false:
        return(result = 0)

        case_true:
        return(result = 1)
    end

See :ref:`non_deterministic_jumps` for more information.

Segments
--------

During debugging, the memory that different components occupy may be exposed. Memory is separated
into different sections called segments. For example, each builtin occupies a different memory
segment. Segments are designated by the colon ``:`` character and some examples are listed below.
See :ref:`segments` for more information.

Memory segments and their interpretation:

* ``0:3``: Memory address 3 within segment 0.
* ``1:7``: Memory address 7 within segment 1.
* ``2:12``: Memory address 12 within segment 2.
* ``3:2``: Memory address 2 within segment 3.
* ``4:0``: Memory address 0 within segment 4.
