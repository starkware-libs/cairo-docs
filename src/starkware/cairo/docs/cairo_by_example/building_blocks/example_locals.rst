.. _example_locals:

Locals
------

This page contains code how locals are used.

Create a file called ``MyProgram.cairo`` with the following contents:

.. tested-code:: cairo example_locals_code

    %builtins output

    from starkware.cairo.common.serialize import serialize_word

    func main{output_ptr : felt*}():
        alloc_locals
        local a : felt
        local b : felt
        %{
            ids.a = 7
            ids.b = program_input['secret']
        %}
        serialize_word(a)
        serialize_word(b)
        return ()
    end

Create an ``input.json`` file in the same directory as the Cairo code with the following contents.

.. tested-code:: json example_locals_input

    {
        "secret": 1234
    }

Now compile the program to produce ``MyProgram_compiled.json``:

.. tested-code:: none example_locals_compile

    cairo-compile MyProgram.cairo --output MyProgram_compiled.json

Now run the program, using the compiled ``MyProgram_compiled.json`` file:

.. tested-code:: none example_locals_run

    cairo-run \
    --program=MyProgram_compiled.json --print_output \
    --print_info --relocate_prints --tracer

Confirm that the program output matches the output below:

.. tested-code:: none example_locals_output

    Program output:
    7
    1234

To explore the program structure and to debug, visit the tracer at http://localhost:8100/.

The program can be sent to a public Ethereum testnet (Ropsten) using SHARP. Run the following
command to send the programto SHARP for proof generation and fact registration:

.. tested-code:: none example_locals_sharp

    cairo-sharp submit --source MyProgram.cairo \
    --program_input input.json

.. include:: ../deploy_notes.rst

.. test::

    import os
    import sys
    import subprocess
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        # Change this name for each unique program, e.g. 'iterator'. The name should match
        # that used in the code descriptions above (e.g. 'example_iterator_code')

        prog_name = 'example_locals'  # e.g. 'iterator'

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
