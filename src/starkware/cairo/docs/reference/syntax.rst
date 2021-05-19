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

Characters
----------

The characters used in Cairo are described below:
    * ``()`` Parentheses: Also known as round brackets. Used in function declaration.
    * ``{}`` Braces: Also known as curly braces or curly brackets. Used in declaration of implicit
        arguments
    * ``[]`` Brackets: Also known as square brackets. Identifies a particular register, e.g.
        the allocation pointer ``[ap]``.
    * ``*`` Single asterisk. Refers to the pointer of an expression.
    * ``**`` Double asterisk. Refers to the pointer of a ``felt*`` expression.
    * ``;`` Semicolon. Used to designate a register instruction, e.g. ``[ap];`` indicates that an
        operation is being performed on the allocation pointer.
    * ``++`` Double plus. An increment on a register, e.g. ``ap++`` increments the allocation
        pointer by one.

Type system
-----------

Cairo have the following types:

* ``felt`` -- a field element (see :ref:`field_elements`).
* ``MyStruct`` where ``MyStruct`` is a :ref:`struct <syntax_structs>` name.
* ``T*`` where ``T`` is any type -- a pointer to type ``T``. For example: ``MyStruct*`` or
  ``felt**``.

.. _syntax_type:

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

Reference can be rebound, which means that TODO.

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

Hints
-----



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

    % builtins output

    func main{output_ptr}():
        return ()
    end

For more informaiton about builtins see :ref:`implicit_arguments`
