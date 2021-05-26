Template
--------

This page outlines the structure of the code examples used in Cairo by Example.

..

    **Documentation Developer notes:**

 1. Find and replace all instances of the word `template` with a unique string.
 2. Modify the contents of the ``.json`` code block with custom data using the JSON schema.
 3. Modify the contents of the ``.cairo`` code block with a custom program.
 4. Modify the contents of the output block. The ``.cairo`` code block will be executed during
    documentation testing and will raise an error if the contents of the output block do not match
    the test output exactly.
 5. Remove this section

Create an ``input.json`` file in the same directory as the cairo code with the following contents.

.. tested-code:: json example_template_input

    {
        "secret": 1234
    }

Create a file called ``MyProgram.cairo`` with the following contents:

.. tested-code:: cairo example_template_code

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

Now compile program to produce ``MyProgram_compiled.json``:

.. tested-code:: none example_template_compile

    cairo-compile MyProgram --output='MyProgram_compiled.json'

Now run the program, using the compiled ``MyProgram_compiled.json`` file:

.. tested-code:: none example_template_run

    cairo-run \
    --program=MyProgram_compiled.json --print_output \
    --print_info --relocate_prints --tracer

Confirm that the program output matches the output below:

.. tested-code:: none example_template_output0

    7
    1234

To explore the program structure and debug, visit the tracer at http://localhost:8100/.

Finally, programs can be sent to public Ethereum testnet (Ropsten).

.. tested-code:: none example_template_sharp

    cairo-sharp submit --source MyProgram.cairo \
    --program_input input.json

.. test::

    import os
    import sys
    import subprocess
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        # Define a virtual environment for running both cairo-compile and cairo-run.
        site_dir = os.path.abspath(os.path.join(os.path.dirname(sys.executable), '..')) + '-site'
        path = os.path.join(site_dir, 'starkware/cairo/lang/scripts') + ':' + os.environ['PATH']
        env = {'PATH': path}

        open(os.path.join(tmpdir, 'MyProgram.cairo'), 'w').write(codes['example_template_code'])
        open(os.path.join(tmpdir, 'input.json'), 'w').write(codes['example_template_input'])
        output = subprocess.check_output(
            'cairo-compile MyProgram.cairo --output MyProgram_compiled.json\n'
            'cairo-run --program=MyProgram_compiled.json --print_output '
            '--program_input=input.json --layout=small',
            shell=True, cwd=tmpdir, env=env).decode('utf8').replace('Program output:','')

        actual_output_lines = [line.strip() for line in output.splitlines() if line.strip()]
        expected_output = '\n'.join([codes[f'example_template_output{i}'] for i in range(1)])
        expected_output_lines = [
            line.strip() for line in expected_output.splitlines() if line.strip()
        ]

        assert actual_output_lines == expected_output_lines
