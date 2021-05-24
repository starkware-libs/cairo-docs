``find_element`` library
------------------------

Import from this library by replacing ``*`` with the function name.

.. tested-code:: cairo library_find_element

    from starkware.cairo.common.find_element import *

``find_element()`` function
***************************

Returns the pointer to an element in array whose value matches a specified value. The function uses
a hint, whereby the Prover arrives at the correct element and then Cairo code verifies that it is
correct. The function has the ability to receive the element_index of that element, which makes the
operation faster than if the Prover has to manually search for the element. The function requires
the implicit argument ``range_check_ptr``.

The function requires four explicit arguments:

- ``array_ptr : felt*``. The pointer to the array. For example, ``my_array*``.
- ``elm_size``. The size of each element in the array. For example, ``3`` memory slots per element.
- ``n_elms``. The number of elements in the array. For example, ``17``.
- ``key``. The first field of the element. For example, the ``felt`` value ``95``.

In the below example, the element index is ``8`` and the value is supplied as a global variable that
the prover can access to find the correct element in constant time. The function will identify the
element that has a first field value of ``95``.

.. tested-code:: cairo library_find_element

    # Optional submission of the index
    __find_element_index = 8

    let element_pointer = find_element(array_ptr=my_array*,
                              elm_size=3,
                              n_elms=17,
                              key=95)

Note that if multiple elements have the same value in as their first field, the function may return
any one of those elements.