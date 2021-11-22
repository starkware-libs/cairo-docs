.. proofedDate proof done pre PR approval

.. comment LEAVE-OK pip command (not bash-specific)"To install" in prerequisites -- should this be "Linux install"? OR "To install in Linux"


Writing unit tests
==================

This page demonstrates how to write unit tests for your StarkNet contracts.
The ``cairo-lang`` package provides a set of python classes that simulates the
behavior of the StarkNet system.
We will use `pytest <https://docs.pytest.org/en/6.2.x/>`_ as the unit test infrastructure.


.. topic:: Prerequisites

    Ensure your environment has pytest. To install:

    .. code-block:: bash

        pip install pytest pytest-asyncio

Next we will write a unit test for the contract from :ref:`first_contract`.
Create a file named ``contract.cairo`` and copy the contract code into it.

Now, copy the following code into a python file named ``contract_test.py``:

.. tested-code:: python first_contract_unit_test

    import os
    import pytest

    from starkware.starknet.compiler.compile import (
        compile_starknet_files)
    from starkware.starknet.testing.starknet import Starknet
    from starkware.starknet.testing.contract import StarknetContract

    # The path to the contract source code.
    CONTRACT_FILE = os.path.join(
        os.path.dirname(__file__), "contract.cairo")


    # The testing library uses python's asyncio. So the following
    # decorator and the ``async`` keyword are needed.
    @pytest.mark.asyncio
    async def test_increase_balance():
        # Compile the contract.
        contract_definition = compile_starknet_files(
            [CONTRACT_FILE], debug_info=True)

        # Create a new Starknet class that simulates the StarkNet
        # system.
        starknet = await Starknet.empty()

        # Deploy the contract.
        contract_address = await starknet.deploy(
            contract_definition=contract_definition)
        contract = StarknetContract(
            starknet=starknet,
            abi=contract_definition.abi,
            contract_address=contract_address,
        )

        # Invoke increase_balance() twice.
        await contract.increase_balance(amount=10).invoke()
        await contract.increase_balance(amount=20).invoke()

        # Check the result of get_balance().
        assert await contract.get_balance().call() == (30,)

This test creates an instance of the Starknet testing class.
This class supports the deployment of, and interaction with, StarkNet contracts.
The test deploys our contract and invokes increase_balance twice.
At the end, it verifies that calling the ``get_balance()`` method returns the expected result.

Run the test using pytest:

.. tested-code:: bash first_contract_unit_test_run

    pytest contract_test.py
