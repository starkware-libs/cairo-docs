``search_sorted_lower()`` function
**********************************

Returns the pointer to the first element in the array whose first field is at least ``key``.
The array elements must be sorted by first field in ascending order. For an array containing
structs, the first field of each element corresponds to the first member. If no such item exists,
returns a pointer to the end of the array. The function requires the implicit argument
``range_check_ptr``.

The function accepts the arguments:

-  ``array_ptr``, the pointer to a sorted array.
-  ``elm_size``, the size of each element in the array (e.g., ``MyStruct.SIZE`` for an array with
   ``MyStruct`` elements).
-  ``n_elms``, the number of elements in the array.
-  ``key``, the ``felt`` value of the ``key`` element being searched for.

The function returns:

-  ``elm_ptr``, the pointer to an element, where ``[elm_ptr]`` is the value of the element.

This function behaves similarly to ``find_element()``, and accepts the same arguments, except the
key is used in a slightly different way. In the example below, the function identifies the first
element that has a first field value of at least ``95``.

.. tested-code:: cairo library_search_sorted_lower

    let smallest_pointer = search_sorted_lower(array_ptr=my_array*,
        elm_size=3,
        n_elms=17,
        key=95)

``search_sorted()`` function
****************************

Returns both the pointer to the first element in the array whose first field is exactly ``key`` and
a value reflecting the success of the search. The array elements must be sorted by first field in
ascending order. For an array containing structs, the first field of each element corresponds to
the first member.  If no such item exists, returns an undefined pointer, and ``success=0``. The
function requires the implicit argument ``range_check_ptr``.

The function accepts the arguments:

-  ``array_ptr``, the pointer to a sorted array.
-  ``elm_size``, the size of each element in the array (e.g., ``MyStruct.SIZE`` for an array with
   ``MyStruct`` elements).
-  ``n_elms``, the number of elements in the array.
-  ``key``, the ``felt`` value of the ``key`` element being searched for.

The function returns:

-  ``elm_ptr``, the pointer to an element, where ``[elm_ptr]`` is the value of the element.
-  ``success``, a ``felt`` value where ``1`` indicates that the array contains an element whose
   first field matches ``key``, and ``0`` indicates that it does not.

This function behaves similarly to ``find_element()``, and accepts the same arguments, except the
key is used in a slightly different way. In the example below, the function will identify the
first element that has a first field value of ``95``. If such an element exists, the second
return value is ``1``, otherwise it is ``0``.

.. tested-code:: cairo library_search_sorted

    let (first_pointer, success_val) = search_sorted_lower(array_ptr=my_array*,
        elm_size=3,
        n_elms=17,
        key=95)
