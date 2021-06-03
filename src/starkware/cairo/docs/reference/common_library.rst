Common Library
==============

This page summarizes library functions available in the Cairo common library.
The common library is written in Cairo the code can be found
`here
<https://github.com/starkware-libs/cairo-lang/tree/master/src/starkware/cairo/common>`_. It
provides a a level of abstraction for common and useful components that can be imported
for use in any Cairo program.

The libraries available are listed below, organized alphabetically. The functions
within each library are outlined under the relevant library heading.

-   :ref:`common_library_alloc`.
-   :ref:`common_library_cairo_builtins`
-   :ref:`common_library_default_dict`
-   :ref:`common_library_dict`
-   :ref:`common_library_dict_access`
-   :ref:`common_library_find_element`
-   :ref:`common_library_hash`
-   :ref:`common_library_hash_chain`
-   :ref:`common_library_hash_state`
-   :ref:`common_library_invoke`
-   :ref:`common_library_math`
-   :ref:`common_library_memcpy`
-   :ref:`common_library_merkle_multi_update`
-   :ref:`common_library_merkle_update`
-   :ref:`common_library_registers`
-   :ref:`common_library_serialize`
-   :ref:`common_library_set`
-   :ref:`common_library_signature`
-   :ref:`common_library_small_merkle_tree`
-   :ref:`common_library_squash_dict`
-   :ref:`common_library_uint256`


**A note about implicit arguments**. Some descriptions state that the library function
"requires the implicit argument ``<argument>``". Where this is the case the decision to
pass the the argument follows the the rule: If the parent function has already
passed ``<argument>`` in curly brackets, the curly brackets can be omitted. Example implicit
arguments might be ``range_check_ptr`` or ``dict_ptr``. See :ref:`implicit_arguments`
for more information.

.. tested-code:: cairo library_implicits0

    func function_with_implicit{range_check_ptr}():
        # Implicit argument is not required again
        library_function()
        return ()
    end

    func function_without_implicit():
        # Implicit argument is required
        library_function{range_check_ptr}()
        return ()
    end

.. _common_library_alloc:

``alloc``
---------

This section contains a function from the ``alloc`` library.

``alloc()``
***********

Returns a newly allocated memory segment. This is useful when defining dynamically allocated
arrays. As more elements are added, more memory can be allocated.

.. tested-code:: cairo alloc_alloc

    from starkware.cairo.common.alloc import alloc

    # Allocate a memory segment.
    let new_slot = alloc()

    # Allocate a memory segment for an array of structs.
    let (local my_array : MyStruct) = alloc()

.. _common_library_cairo_builtins:

``cairo_builtins``
------------------

..  TODO (perama, 03 June)
    This section contains functions from the ``cairo_builtins`` library.

.. _common_library_default_dict:

``default_dict``
----------------

..  TODO (perama, 03 June)
   This section contains functions from the ``default_dict`` library.

.. _common_library_dict:

``dict``
--------

..  TODO (perama, 03 June)
    This section contains functions from the ``dict`` library.

.. _common_library_dict_access:

``dict_access``
---------------

..  TODO (perama, 03 June)
    This section contains functions from the ``dict_access`` library.

.. _common_library_find_element:

``find_element``
----------------

..  TODO (perama, 03 June)
    This section contains functions from the ``find_element`` library.

.. _common_library_hash:

``hash``
--------

..  TODO (perama, 03 June)
    This section contains functions from the ``hash`` library.

.. _common_library_hash_chain:

``hash_chain``
--------------

..  TODO (perama, 03 June)
    This section contains functions from the ``hash_chain`` library.

.. _common_library_hash_state:

``hash_state``
--------------

..  TODO (perama, 03 June)
    This section contains functions from the ``hash_state`` library.

.. _common_library_invoke:

``invoke``
----------

..  TODO (perama, 03 June)
    This section contains functions from the ``invoke`` library.

.. _common_library_math:

``math``
--------

..  TODO (perama, 03 June)
    This section contains functions from the ``math`` library.

.. _common_library_memcpy:

``memcpy``
----------

..  TODO (perama, 03 June)
    This section contains functions from the ``memcpy`` library.

.. _common_library_merkle_multi_update:

``merkle_multi_update``
-----------------------

..  TODO (perama, 03 June)
    This section contains functions from the ``merkle_multi_update`` library.

.. _common_library_merkle_update:

``merkle_update``
-----------------

..  TODO (perama, 03 June)
    This section contains functions from the ``merkle_update`` library.

.. _common_library_registers:

``registers``
--------------

..  TODO (perama, 03 June)
    This section contains functions from the ``registers`` library.

.. _common_library_serialize:

``serialize``
-------------

..  TODO (perama, 03 June)
    This section contains functions from the ``serialize`` library.

.. _common_library_set:

``set``
-------

..  TODO (perama, 03 June)
    This section contains functions from the ``set`` library.

.. _common_library_signature:

``signature``
-------------

..  TODO (perama, 03 June)
    This section contains functions from the ``signature`` library.

.. _common_library_small_merkle_tree:

``small_merkle_tree``
---------------------

..  TODO (perama, 03 June)
    This section contains functions from the ``small_merkle_tree`` library.

.. _common_library_squash_dict:

``squash_dict``
---------------

..  TODO (perama, 03 June)
    This section contains functions from the ``squash_dict`` library.

.. _common_library_uint256:

``uint256``
-----------

..  TODO (perama, 03 June)
    This section contains functions from the ``uint256`` library.
