Inputs
------

This is a short example of a system that involves a smart contract interacting
with a Cairo program. The example highlights how Cairo programs and their proofs
can interact with the Ethereum blockchain.

The user provides a special number to a Cairo program. A proof is generated and
integrated into the Ethereum blockchain. A smart contract checks the proof and
then accepts the special number and performs an action using that number.

Create an ``input.json`` file in the same directory as the cairo code with the following contents.

.. tested-code:: json example_variables_input

    {
        "current_number": 300,
        "special_number": 556
    }

Create a file called ``MyProgram.cairo`` with the following contents:

.. tested-code:: cairo example_variables_code

    %builtins output
    from starkware.cairo.common.serialize import serialize_word

    func main{output_ptr : felt*}():
        alloc_locals
        local original_number : felt  # A local variable (a felt/integer)
        local a_special_number : felt
        # A hint
        %{
            # Python code that processes the .json file
            num = program_input['current_number']
            ids.original_number = num
            new_num = program_input['special_number']
            ids.a_special_number = new_num
        %}
        serialize_word(original_number)  # Produce number as an output
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

    300
    556

To explore the program structure and debug, visit the tracer at http://localhost:8100/.

Next, the program can be sent to public Ethereum testnet (Ropsten). SHARP
creates the proof and saves it in a compact format in the Fact Registry contract as CALLDATA.

.. tested-code:: none example_variables_sharp

    cairo-sharp submit --source MyProgram.cairo \
    --program_input input.json

Once the transaction has been mined, a solidity contract can be deployed to interact with
the program above. The ``SpecialNumber`` contract below stores a number which can be updated
if a valid proof is provided. The proof must show that the user knew the initial number and
has provided a different number to store. The proof demonstrates that the Cairo program was not
modified and that the program was exectuted properly to produce the two outputs.

.. tested-code:: none special_number_solidity

    pragma solidity ^0.5.2;

    contract IFactRegistry {
        /*
        Returns true if the given fact was previously registered.
        */
        function isValid(bytes32 fact)
            external view
            returns(bool);
    }

    contract SpecialNumber {

        // The current special number
        uint256 currentNumber_;

        // The Cairo program hash.
        uint256 cairoProgramHash_;

        // The Cairo verifier.
        IFactRegistry cairoVerifier_;

        constructor(
            uint256 cairoProgramHash,
            address cairoVerifier,
            uint256 initialNumber)
            public
        {
            currentNumber_ = initialNumber;
            cairoProgramHash_ = cairoProgramHash;
            cairoVerifier_ = IFactRegistry(cairoVerifier);
        }

        function updateNumber(uint256[] memory programOutput)
            public
        {
            // Ensure that a corresponding proof was verified.
            bytes32 outputHash = keccak256(
                abi.encodePacked(programOutput));
            bytes32 fact = keccak256(
                abi.encodePacked(cairoProgramHash_, outputHash));
            require(
                cairoVerifier_.isValid(fact),
                "MISSING_CAIRO_PROOF");

            // Ensure the output consistency with currentstate.
            require(
                programOutput.length == 2,
                "INVALID_PROGRAM_OUTPUT");
            require(
                currentNumber_ == programOutput[0],
                "MISSING_ORIGINAL_NUMBER");
            require(
                currentNumber_ != programOutput[1],
                "NUMBER_MUST_BE_DIFFERENT");

            // Update stored number with new number.
            currentNumber_ = programOutput[1];
        }
    }

A user can now check the current number in the ``SpecialNumber`` contract, run the
``MyProgram.cairo`` contract and using that number and a new number as inputs. After sending
that program to SHARP for proving, they can call the ``updateNumber()`` function, providing
the two numbers from the output of ``MyProgram.cairo`` to the function. The contract will then
call the fact registry contract method ``IsValid()`` and if ``True``, the special number will
be updated.

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
