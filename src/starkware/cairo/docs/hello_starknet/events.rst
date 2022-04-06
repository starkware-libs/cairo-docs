Events
======

The StarkNet event mechanism allows a contract to output information during its execution
that can later be used outside of StarkNet.
For example, consider a token contract that allows transfers of tokens between users.
By only querying StarkNet storage, a user can only see how much token they have, and not
who transferred those tokens.
An event, emitted by the contract whenever funds are transferred, can be used to allow
the user to get this information.

Consider the contract described in :ref:`user_authentication`.
Let's add an event whenever the ``increase_balance()`` function is called.

Start by defining the event:

.. tested-code:: cairo events_event_def

    # An event emitted whenever increase_balance() is called.
    # current_balance is the balance before it was increased.
    @event
    func increase_balance_called(
        current_balance : felt, amount : felt
    ):
    end

Add the following lines before the ``return()`` statement in ``increase_balance()``:

.. tested-code:: cairo events_emit

    # Emit the event.
    increase_balance_called.emit(current_balance=res, amount=amount)

Save the new contract file as ``events.cairo``.
You can find the full contract `here <../_static/events.cairo>`_.

Compile and deploy the contract:

.. tested-code:: bash events_compile_starknet

    starknet-compile events.cairo \
        --output events_compiled.json \
        --abi events_abi.json

    starknet deploy --contract events_compiled.json

Invoke ``increase_balance()``:

.. _events_increase_balance:

.. tested-code:: bash events_invoke

    starknet invoke \
        --address ${CONTRACT_ADDRESS} \
        --abi events_abi.json \
        --function increase_balance \
        --inputs 4321

Wait for the transaction to be accepted (when its status is PENDING at least)
and run the following line to see the emitted event
(replace ``${TX_HASH}`` with the transaction hash you got from the last command):

.. tested-code:: bash events_get_tx_receipt

    starknet get_transaction_receipt --hash ${TX_HASH}

Consider the ``events`` section of the output. It should resemble:

.. tested-code:: json events_get_tx_receipt_output

    "events": [
        {
            "data": [
                "0x0",
                "0x10e1"
            ],
            "from_address": "0x14acf3b7e92f97adee4d5359a7de3d673582f0ce03d33879cdbdbf03ec7fa5d",
            "keys": [
                "0x3db3da4221c078e78bd987e54e1cc24570d89a7002cefa33e548d6c72c73f9d"
            ]
        }
    ]

The result contains the following fields:

*   ``from_address`` -- the address of the contract emitting the event.
*   ``data`` -- the arguments passed to ``increase_balance_called.emit``:
    the balance before (0) and the amount (4321==0x10e1).
*   ``key`` -- The event's key is derived from the name of the event (``increase_balance_called``).
    If your contract emits more than one type of event, you can use this field to
    distinguish between them. You can use python to get the event key from its name:

    .. tested-code:: python events_key_from_name

        from starkware.starknet.compiler.compile import \
            get_selector_from_name

        print(hex(get_selector_from_name('increase_balance_called')))

Note that StarkNet currently does not have API to fetch all events from a given contract.

.. test::

    import os

    from starkware.cairo.docs.test_utils import reorganize_code

    increase_balance_code = codes['user_auth_increase_balance'].replace(
        "return ()", "\n" + codes['events_emit'] + "\n\n return()")

    code = reorganize_code('\n\n'.join([
        '%lang starknet',
        'from starkware.cairo.common.cairo_builtins import HashBuiltin',
        'from starkware.starknet.common.syscalls import get_caller_address',
        codes['balance_map'],
        codes['events_event_def'],
        increase_balance_code,
        codes['user_auth_get_balance'],
    ]))

    events_filename = os.path.join(
        os.environ['DOCS_SOURCE_DIR'], 'hello_starknet/events.cairo')
    # Uncomment below to fix the file:
    # open(events_filename, 'w').write(code)
    assert open(events_filename).read() == code, 'Please fix events.cairo.'

