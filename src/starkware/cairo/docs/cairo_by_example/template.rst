Template
========
..
    This page is a demonstration of [...]

This page outlines the structure of the code examples used in Cairo by Example.

..
    **Documentation Development notes:**
    1. Replace the word **template** below with a unique string.
    2. Modify the contents of the ``.json`` code block with custom data using the JSON schema.
    3. Modify the contents of the ``.cairo`` code block with a custom program.
    4. Modify the contents of the output block. The ``.cairo`` code block will be executed during
       documentation testing and will raise an error if the contents of the output block do not
       match the test output exactly.
    5. Check that the path to deploy_notes.rst is correct (../deploy_notes.rst)
    6. Remove this section

**Inputs**

Create an ``input.json`` file in the same directory as the Cairo code with the following contents.

.. tested-code:: json example_TEMPLATE_input

    {
        "input_name": 1234
    }

**Code**

Create a file called ``MyProgram.cairo`` with the following contents:

.. tested-code:: cairo example_TEMPLATE_code

    func main():
        # Cairo code here
        return ()
    end

**Execution**

Now compile the program to produce ``MyProgram_compiled.json``:

.. tested-code:: none example_TEMPLATE_compile

    cairo-compile MyProgram.cairo --output MyProgram_compiled.json

Now run the program, using the compiled ``MyProgram_compiled.json`` file:

.. tested-code:: none example_TEMPLATE_run

    cairo-run \
    --program=MyProgram_compiled.json --print_output \
    --print_info --relocate_prints --tracer

The flags function as follows:

-   ``--program``, the name of the program json file.
-   ``--print_output``, print the program output (if the output builtin is used).
-   ``--print_info``, print information on the execution of the program.
-   ``--relocate_prints``, print memory and info after memory relocation.
-   ``--tracer``, run the tracer.

Confirm that the program output matches the output below:

.. tested-code:: none example_TEMPLATE_output

    Program output:
    ouput_1
    ouput_2

To explore the program structure and to debug, visit the tracer at http://localhost:8100/.

**Submission**

The program can be sent to a public Ethereum testnet (Ropsten) using SHARP. Run the following
command to send the programto SHARP for proof generation and fact registration:

.. tested-code:: none example_TEMPLATE_sharp

    cairo-sharp submit --source MyProgram.cairo \
    --program_input input.json

.. include:: deploy_notes.rst

.. test::

    import os
    import sys
    import subprocess
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        # Change this name for each unique program, e.g. 'iterator'. The name should match
        # that used in the code descriptions above (e.g. 'example_iterator_code')

        unique_name = 'TEMPLATE'  # e.g. 'iterator'

        prog_name = f'example_{unique_name}'  # e.g. 'example_iterator'

        # Define a virtual environment for running both cairo-compile and cairo-run.
        site_dir = os.path.abspath(os.path.join(os.path.dirname(sys.executable), '..')) + '-site'
        path = os.path.join(site_dir, 'starkware/cairo/lang/scripts') + ':' + os.environ['PATH']
        env = {'PATH': path}

        open(os.path.join(tmpdir, 'MyProgram.cairo'), 'w').write(codes[f'{prog_name}_code'])
        open(os.path.join(tmpdir, 'input.json'), 'w').write(codes[f'{prog_name}_input'])
        output = subprocess.check_output(
            'cairo-compile MyProgram.cairo --output MyProgram_compiled.json\n'
            'cairo-run --program=MyProgram_compiled.json --print_output '
            '--program_input=input.json --layout=small',
            shell=True, cwd=tmpdir, env=env).decode('utf8')

        actual_output_lines = [line.strip() for line in output.splitlines() if line.strip()]
        expected_output = codes[f'{prog_name}_output']
        expected_output_lines = [
            line.strip() for line in expected_output.splitlines() if line.strip()
        ]
        assert actual_output_lines == expected_output_lines

**Application Deployment**

A solidity contract ``CairoApplication.sol`` can be deployed to use the fact in the
``FactRegistry`` contract for its logic. That contract may have a function ``updateState()``
which can be called by passing outputs from ``MyProgram.cairo`` as arguments. The function
call would be a transaction that updates the state of the application to reflect the
state changes that the Cairo program created.

**Application Use**

A user, or agent on behalf of a user, can interact with the application by following the steps:

1. Create an ``inputs.json`` file with curstom values.
2. Obtain a copy of ``MyProgram.cairo``.
3. Install Cairo and compile the program.
4. Submit the program to SHARP for proving.
5. Call ``updateState()`` function in the ``CairoApplication`` contract.

These steps can be abstracted away from the user experience with the use of an interface and
server backend.