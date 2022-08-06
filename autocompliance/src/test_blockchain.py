#!/usr/bin/python3

# Author: @andrewk10

# Importing autocompliance_blockchain for blockchain based functionality
import blockchain
# Importing logging to safely log sensitive, error or debug info.
import logging


def test_create_blockchain():
    """
    This function tests the create_blockchain function in the blockchain script.
    It uses example arguments to do this stored in strings.py, but before it does that the
    bad path is checked by passing in a single argument with no value to get a runtime
    error.
    """
    # Creating blockchain itself.
    test_blockchain = blockchain.Blockchain()
    # Testing against the genesis block.
    assert test_blockchain.get_previous_block()["index"] == 1
    assert test_blockchain.get_previous_block()["timestamp"] is not None
    assert test_blockchain.get_previous_block()["proof"] == 1
    assert test_blockchain.get_previous_block()["previous_hash"] == "0"


def test_set_speaker_timeout():
    """
    This function tests the set_speaker_timeout function in the blockchain script.
    """
    # Creating blockchain itself.
    test_blockchain = blockchain.Blockchain()
    test_blockchain.validator = 5
    test_blockchain.speaker_timeout = 5
    test_blockchain.set_speaker_timeout()
    assert test_blockchain.speaker_timeout == 320


def test_set_validator():
    """
    This function tests the set_validator function in the blockchain script. All it does
    really is provide coverage on the function itself.
    TODO: This test could be more robust. try to add random values to the equation.
    """
    test_blockchain = blockchain.Blockchain()
    test_blockchain.validator = 1
    test_blockchain.number_of_validators = 1
    test_blockchain.set_validator()
    assert test_blockchain.validator == 0


def test_initialise_consensus_information():
    """
    This function tests the set_validator function in the blockchain script. It does this
    by changing the blockchain's values for number of validators to some abstract value.
    TODO: Make this number random to avoid coincidences.
    """
    test_blockchain = blockchain.Blockchain()
    test_blockchain.number_of_validators = 25
    test_blockchain.initialise_consensus_information()
    assert test_blockchain.consensus_context == 17
