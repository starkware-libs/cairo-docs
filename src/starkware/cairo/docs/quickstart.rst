.. _quickstart:

Setting up the environment
==========================

Installation
------------

We recommend working inside a python virtual environment, but you can also install
the Cairo package directly.
To create and enter the virtual environment, type::

    python3.7 -m venv ~/cairo_venv
    source ~/cairo_venv/bin/activate

Make sure the venv is activated -- you should see ``(cairo_venv)`` in the command line prompt.

Make sure you can install the following pip packages: ``ecdsa``, ``fastecdsa``, ``sympy``
(using ``pip3 install ecdsa fastecdsa sympy``).
On Ubuntu, for example, you will have to first run::

    sudo apt install -y libgmp3-dev

On Mac, you can use ``brew``::

    brew install gmp

Download the python package (``cairo-lang-0.1.0.zip``) from
https://github.com/starkware-libs/cairo-lang/releases/tag/v0.1.0.
To install it using ``pip``, run::

    pip3 install cairo-lang-0.1.0.zip

Cairo was tested with python3.7.
To make it work with python3.6, you will have to install ``contextvars``::

    pip3 install contextvars

Compiling and running a Cairo program
-------------------------------------

1.  Create a file, named ``test.cairo``, with the following lines:

    .. tested-code:: cairo quickstart_code

        func main():
            [ap] = 1000; ap++
            [ap] = 2000; ap++
            [ap] = [ap - 2] + [ap - 1]; ap++
            ret
        end

2.  Compile: (make sure all commands are executed in the virtual environment)

    .. tested-code:: none compile_cmd

        cairo-compile test.cairo --output test_compiled.json

3.  Run:

    .. tested-code:: none quickstart_run_cmd

        cairo-run \
          --program=test_compiled.json --print_output \
          --print_info --relocate_prints


4.  You can open the Cairo tracer by providing the ``--tracer`` flag to ``cairo-run``.
    Then open it at http://localhost:8100/.


.. test::

    import os
    import subprocess
    import sys
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        # Define a virtual environment for running both cairo-compile and cairo-run.
        site_dir = os.path.abspath(os.path.join(os.path.dirname(sys.executable), '..')) + '-site'
        path = os.path.join(site_dir, 'starkware/cairo/lang/scripts') + ':' + os.environ['PATH']
        env = {'PATH': path}

        open(os.path.join(tmpdir, 'test.cairo'), 'w').write(codes['quickstart_code'])
        subprocess.check_output(codes['compile_cmd'], shell=True, cwd=tmpdir, env=env)
        subprocess.check_output(codes['quickstart_run_cmd'], shell=True, cwd=tmpdir, env=env)

Visual Studio Code setup
------------------------

.. only:: internal

    Install the Cairo Visual Studio Code extension::

        cd src/starkware/cairo/lang/ide/vscode-cairo/
        sudo npm install -g vsce
        npm install
        vsce package
        code --install-extension cairo*.vsix

    Configure vscode settings::

        "cairo.cairoFormatPath": "${workspaceFolder}/src/starkware/cairo/lang/scripts/cairo-format",
        "editor.formatOnSaveTimeout": 1500,

.. only:: not internal

    Download the Cairo Visual Studio Code extension (``cairo-0.1.0.vsix``) from
    https://github.com/starkware-libs/cairo-lang/releases/tag/v0.1.0,
    and install it using::

        code --install-extension cairo-0.1.0.vsix

    Configure Visual Studio Code settings::

        "editor.formatOnSave": true,
        "editor.formatOnSaveTimeout": 1500

    **Note:** You should start Visual Studio Code from the terminal
    *running the virtual environment*, by typing ``code``.
    For instructions for macOS, see
    `here <https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line>`_.

.. only:: internal

    VIM Setup
    ---------

    Install the Cairo VIM extension:

    .. code::

        cp -r src/starkware/cairo/lang/ide/vim/* ~/.vim/

    To use the auto-formatter, type ``:Format`` to format the Cairo code in the current buffer.
