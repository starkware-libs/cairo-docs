Inputs
------

This is a short example of a system that involves a smart contract interacting
with a Cairo program. The example highlights how Cairo programs and their proofs
can interact with the Ethereum blockchain.

The user provides a special number to a Cairo program. A proof is generated and
integrated into the Ethereum blockchain. A smart contract checks the proof and
then accepts the special number and executes some function using that number.

Create an ``input.json`` file in the same directory as the cairo code with the following contents.

.. tested-code:: json example_variables_input

    {'special_number': 556}

Create a file called ``MyProgram.cairo`` with the following contents:

.. tested-code:: cairo example_variables_code

    %builtins output
    from starkware.cairo.common.serialize import serialize_word

    func main{output_ptr : felt*}():
        alloc_locals
        local a_special_number : felt  # A local variable (a felt/integer)

        # A hint
        %{
            # Python code that processes the .json file
            num = program_input['special_number']
            idx.a_special_number = num
        %}
        serialize_word(a_special_number)  # Produce number as an output
        return ()
    end

Now compile program to produce ``MyProgram_compiled.json``:

.. tested-code:: none example_variables_compile

    cairo-compile MyProgram --output='MyProgram_compiled.json'

Now run the program, using the compiled ``MyProgram_compiled.json`` file:

.. tested-code:: none example_variables_run

    cairo-run \
    --program=MyProgram_compiled.json --print_output \
    --print_info --relocate_prints --tracer

Confirm that the program output matches the output below:

.. tested-code:: none example_variables_output0

    556

To explore the program structure and debug, visit the tracer at http://localhost:8100/.

Finally, programs can be sent to public Ethereum testnet (Ropsten).

.. tested-code:: none example_variables_sharp

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

        open(os.path.join(tmpdir, 'MyProgram.cairo'), 'w').write(codes['example_variables_code'])
        open(os.path.join(tmpdir, 'input.json'), 'w').write(codes['example_variables_input'])
        output = subprocess.check_output(
            'cairo-compile MyProgram.cairo --output MyProgram_compiled.json\n'
            'cairo-run --program=MyProgram_compiled.json --print_output '
            '--program_input=input.json --layout=small',
            shell=True, cwd=tmpdir, env=env).decode('utf8').replace('Program output:','')

        actual_output_lines = [line.strip() for line in output.splitlines() if line.strip()]
        expected_output = '\n'.join([codes[f'example_variables_output{i}'] for i in range(1)])
        expected_output_lines = [
            line.strip() for line in expected_output.splitlines() if line.strip()
        ]

        assert actual_output_lines == expected_output_lines
