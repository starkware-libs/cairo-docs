StarkNet and Cairo Documentation
================================

**StarkNet** is a permissionless decentralized ZK-Rollup operating as an L2 network over Ethereum,
where any dApp can achieve unlimited scale for its computation,
without compromising Ethereum's composability and security.

**Cairo** is a programming language for writing provable programs, where one party can prove
to another that a certain computation was executed correctly. **Cairo** and similar proof systems
can be used to provide scalability to blockchains.

StarkNet uses the **Cairo** programming language both for its infrastructure
and for writing StarkNet contracts.

Here we provide three tutorials:

*   :ref:`Hello, StarkNet <hello_starknet>`
*   :ref:`Hello, Cairo <hello_cairo>`
*   :ref:`How Cairo Works <how_cairo_works>`

"Hello, Starknet" is a guide on how to write StarkNet contracts,
and demonstrates the system's basic features.

"Hello, Cairo" describes Cairo for the programmer who wishes to understand what Cairo can do
hands-on, and start writing programs in Cairo.
"How Cairo Works" starts from the low-level assembly-like version of Cairo and
explains the syntactic sugar mechanisms applied by the Cairo compiler,
which turns Cairo to a high-level-like language.

The "Hello, Cairo" tutorial contains several references to "How Cairo Works"
for those who want to get a better understanding of those topics.

**Where should I start?**
If you want to promptly dive into writing StarkNet contracts,
start with "Hello, StarkNet" and jump to "Hello, Cairo"
whenever you need additional clarifications.
If you want to write Cairo programs, independent of StarkNet, start with "Hello, Cairo".
Finally, if you want to understand Cairo's internals from the ground up,
start with "How Cairo Works" and then follow with "Hello, Cairo".

.. toctree::
    :hidden:

    self

.. toctree::
    :maxdepth: 1

    quickstart

.. toctree::
    :maxdepth: 2

    hello_starknet/index
    hello_cairo/index
    how_cairo_works/index
    reference/index
    sharp
