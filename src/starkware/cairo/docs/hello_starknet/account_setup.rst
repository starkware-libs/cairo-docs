.. _account_setup:

Setting up a StarkNet account
=============================

Installation
------------

Follow the installation instructions for the ``cairo-lang`` package in :ref:`quickstart`.

Setting up the network
----------------------

In this tutorial we will use the StarkNet CLI (command line interface) to interact with StarkNet.
In order to instruct the CLI to work with the StarkNet testnet you may either
add the ``--network=alpha-goerli`` flag to every command, or simply set the ``STARKNET_NETWORK``
environment variable as follows:

.. tested-code:: bash setup_starknet_env

    export STARKNET_NETWORK=alpha-goerli

Choosing a wallet provider
--------------------------

Unlike Ethereum, which distinguishes between Externally Owned Accounts (EOA) and contracts,
StarkNet doesn't have this distinction.
Instead, an account is represented by a deployed contract that
defines the account's logic -- most notably the signature scheme that controls
who can issue transactions from it.

.. TODO(lior, 01/04/2022): Remove the warning once OZ contract is fixed.

To interact with StarkNet, you will need to deploy an account contract.
In this tutorial, we will use a slightly modified version of OpenZeppelin's standard
for EOA contract (at the moment, the signature is computed differently).
Set the ``STARKNET_WALLET`` environment variable as follows:

.. tested-code:: bash setup_wallet

    export STARKNET_WALLET=starkware.starknet.wallets.open_zeppelin.OpenZeppelinAccount

.. _create_account:

Creating an account
-------------------

Run the following command to create an account:

.. tested-code:: bash setup_deploy_account

    starknet deploy_account

The output should resemble:

.. tested-code:: bash setup_deploy_account_output

    Sent deploy account contract transaction.

    NOTE: This is a modified version of the OpenZeppelin account contract. The signature is computed
    differently.

    Contract address: ...
    Public key: ...
    Transaction hash: ...

You may also specify a name for your account using ``--account=my_account`` if you want to
maintain multiple accounts. If not specified, the default account (named ``__default__``) is used.

The ``STARKNET_WALLET`` environment variable instructs the StarkNet CLI to use your account
in the ``starknet invoke`` and ``starknet call`` commands.
If you want to do a direct call to a contract, without passing through your account contract,
you can pass the ``--no_wallet`` argument to the CLI, which overrides the ``STARKNET_WALLET``
variable.

**Warning**: Using the builtin wallet providers that are part of the ``cairo-lang`` package
(``starkware.starknet.wallets...``) is
**not secure** (for example, the private key may be kept unencrypted and without backup
in your home directory).
You should only use them if you're not overly concerned with losing access to your accounts
(for example, for testing purposes).

Transferring Goerli ETH to the account
--------------------------------------

In order to execute transactions on StarkNet, you'll need to have
ETH in your L2 account (for paying transaction fees).

You can acquire L2 ETH in the following ways:

1.  Use the `StarkNet Faucet <https://faucet.goerli.starknet.io/>`__
    to get small amounts of ETH directly to the account you have just created.
    This should suffice for simple transactions.
2.  Use StarkGate -- the StarkNet L2 bridge
    (`L1 contract <https://goerli.etherscan.io/address/0xc3511006C04EF1d78af4C8E0e74Ec18A6E64Ff9e>`__
    / `Web App <https://goerli.starkgate.starknet.io>`__)
    to transfer your existing Goerli L1 ETH to and from the L2 account.
