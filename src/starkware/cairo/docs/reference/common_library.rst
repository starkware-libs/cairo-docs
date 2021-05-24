``search_sorted_lower()`` function
**********************************

Returns the pointer to the first element in the array whose first field is at least ``key``. The
array elements must be sorted by first field (from smallest to largest). If no such item exists,
returns a pointer to the end of the array. The function requires the implicit argument ``range_check_ptr``.

The function behaves similarly to ``find_element()`` and accepts the same arguments. In the example
below, the function will identify the fist element that has a first field value of at least ``95``.

.. tested-code:: cairo library_search_sorted_lower

    let smallest_pointer = search_sorted_lower(array_ptr=my_array*,
        elm_size=3,
        n_elms=17,
        key=95)

``search_sorted()`` function
****************************

Returns both the pointer to the first element in the array whose first field is exactly ``key`` and
a value reflecting the success of the search. The array elements must be sorted by first field (from
smallest to largest). If no such item exists, returns an undefined pointer, and ``success=0``. The
function requires the implicit argument ``range_check_ptr``.

The function behaves similarly to ``find_element()`` and accepts the same arguments. In the example
below, the function will identify the fist element that has a first field value of ``95``. If such
an element exists, the second return value will be ``1``, otherwise it will be ``0``.

.. tested-code:: cairo library_search_sorted

    let (first_pointer, success_val) = search_sorted_lower(array_ptr=my_array*,
        elm_size=3,
        n_elms=17,
        key=95)
