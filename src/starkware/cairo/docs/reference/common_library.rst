``find_element`` library
------------------------

``find_element()`` function
***************************

Returns the pointer to an element in an array whose value matches a specified value. The function
uses a hint, whereby the prover arrives at the correct element and then Cairo code verifies that it
is correct. The function has the ability to receive the index of that element, which makes the
operation faster than if the prover has to manually search for the element. The function
requires the implicit argument ``range_check_ptr``.

The function requires four explicit arguments:

- ``array_ptr``, a pointer to an array (e.g., ``my_array``).
- ``elm_size``, the size of each element in the array (e.g., ``3`` memory slots per element).
- ``n_elms``, the number of elements in the array (e.g., ``17``).
- ``key``, the value to look for (e.g., the ``felt`` value ``95``).

The function returns:

- ``elm_ptr``, the pointer to an element whose value is ``key``, in other words an element that
  satisfies ``[elm_ptr] = key``.

In the example below, the element index is ``8``, and that information is provided as a global
variable that the prover can access. This allows the ``find_element()`` function to be run by
the prover in constant, "O(1)", time. This means that increasing the length of the array
does not increase the time to find the element. If the element index is not provided, or is
incorrect, the prover must check every element in the array, which takes linear, "O(n)", time.
That is, the use of ``__find_element_index`` can speed up proof generation through nondeterminism,
and the function otherwise defaults to standard time complexity that normal deterministic
programs operate in.

The function will identify an element whose first field value is equal to ``95``.

.. tested-code:: cairo library_find_element

    from starkware.cairo.common.find_element import find_element

    # Optional submission of the index
    __find_element_index = 8

    let element_pointer = find_element(
        array_ptr=my_array, elm_size=3, n_elms=17, key=95)

Note that if multiple elements in the array have the same value for the first memory cell,
the function may return the index to any of these elements.