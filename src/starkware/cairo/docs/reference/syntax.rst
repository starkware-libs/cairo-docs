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

Pointers
--------

The address of an expression is accessed using a pointer. An address may exist before a value has
been stored at that expression. For example, where a function accepts an argument of a certain type,
a pointer to that type allows the compiler to allocate memory appropriately.

Consider the following expressions defined some Cairo program:

*  ``MyFelt``: A field element with a particular value, such as ``7``.
*  ``MyStruct``: A struct with defined members (not outlined here)
*  ``MyExp``: An expression whose type will be defined with ``MyExp : <type>`` in the examples below.
   ``MyExp`` may be read as "My Expression".

Expressions, pointers and their interpretation are outlined below. While it is usually not necessary
to use the expressions with square brackets, they are included for completeness in the event they
are encountered in documentation elsewhere.

*   ``felt``. A value.
    * ``MyExp : felt`` reads as "``MyExp`` is a ``felt`` and in practice, an integer".
*   ``felt*``. A pointer to a value.
    * ``MyExp : felt*`` reads as "``MyExp`` is the location where one or more ``felt`` expressions
    are stored, which can be used to define a list".
*   ``felt**``. A pointer to a pointer.
    * ``MyExp : felt**`` reads as "``MyExp`` is is the location where one or more pointers are
    stored, which can be used to define a list of lists".
*   ``MyFelt``. A value, in this instance ``7``.
    * The code ``MyExp : MyFelt`` is not used because ``MyExp`` type cannot be assigned to a
    particular ``felt`` instance.
*   ``MyFelt*``. A pointer to the value ``7``.
    * ``MyExp : MyFelt*`` reads as "``MyExp`` is the location where ``MyFelt`` is stored, which may
    be used if ``MyFelt`` is extended to a list with ``7`` as the first value".
*   ``MyFelt**``. A pointer to a pointer.
    * ``MyExp : MyFelt**`` reads as "``MyExp`` is the location where the ``MyFelt*`` pointer is
    stored, which can be used to construct a list of lists".
*   ``[MyFelt]``. A value at address ``MyFelt``.
    * This expression is not used because ``MyFelt`` is a value, not an address.
    * It follows that the expression ``MyExp : [MyFelt]`` is not used.
*   ``[MyFelt*]``. A value at the pointer ``MyFelt*``.
    * If MyFelt* is being used to define a list, this statement reads as "The value of the first
    item in the list which starts at ``Myfelt*``.
    * ``MyExp : [MyFelt*]`` is not used because ``[MyFelt*]`` is a value.
*   ``[MyFelt* + 1]``. A value at the pointer one slot after ``MyFelt*``.
    * If ``MyFelt*`` is being used to define a list, this statement reads as "The value of the
    second item in the list which starts at ``Myfelt*``.
*   ``MyStruct``. A value, in this instance a struct with defined values.
    * The code ``MyExp : MyStruct`` is not used because ``MyExp`` type cannot be assigned to a
    particular struct instance.
*   ``MyStruct*``. A pointer to a struct value.
    * ``MyExp : MyStruct*`` reads as "``MyExp`` is of type ``MyStruct``".
    * ``MyExp`` points to where ``MyStruct`` is stored and has the same member structure as
    ``MyStruct``.
    * ``MyExp`` has members may be populated with values.
*   ``MyStruct**`` . A pointer (to a pointer).
    * ``MyExp : MyStruct**`` reads as "``MyExp`` is a pointer to where ``MyStruct*`` pointers are
    stored, and can be used to represent a list of structs". See :ref:`transaction_loop_list`.
*   ``[MyStruct]``. A value at the struct ``MyStruct``.
    * This expression is not used because structs occupy multiple memory slots which can be
    addressed individually.
*   ``[MyStruct*]``. A value at the pointer to the first memory address of ``MyStruct*``.
    * Reads as "The value at the first memory slot that ``MyStruct`` occupies".
    * ``MyExp : [MyStruct*]`` is not used because ``[MyStruct*]`` is a particular value not a type.
*   ``[MyStruct* + 1]``. A value at the pointer to the second memory address of ``MyStruct*``.
    * Reads as "The value at the second memory slot that ``MyStruct`` occupies".
*   ``[MyStruct**]``. A value at the pointer to the first memory address of the pointer
    ``MyStruct**``.
    * Reads as "The pointer to the first struct in the list of structs."
    * This pointer can be used to reference the values within that first struct.
    * ``MyExp : [MyStruct**]`` is not used because ``[MyStruct**]`` is a particular value.
*   ``[MyStruct** + 1]``. A value at the pointer to the second memory address of the pointer
    ``MyStruct**``.
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
