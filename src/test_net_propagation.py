#!/usr/bin/python3

# Importing file for file based functionality
import file
# Importing net_propagation for testing.
import net_propagation
# Importing strings for common string resources.
import strings
# Importing strings_functions for string building functions.
import strings_functions


def test_additional_actions():
    """
    This function tests the additional_actions function in the net_propagation
    script. Currently, the function only calls two other functions, so this
    test uses the bad path in both to run through once. Good paths are tested
    in the two functions own tests.
    """
    transfer_file = file.File(strings.RANDOM_STRING)
    propagation_script = file.File(strings.RANDOM_STRING)
    arguments = [strings.ARGUMENT_IP_ADDRESS_FILENAME,
                 strings.ARGUMENT_SPECIFIC_PROPAGATION_FILE]
    ip = strings.TEST_IP
    username = strings.RANDOM_STRING
    ports = [strings.SSH_PORT, strings.WEB_PORT_EIGHTY,
             strings.WEB_PORT_EIGHTY_EIGHTY,
             strings.WEB_PORT_EIGHTY_EIGHT_EIGHTY_EIGHT]
    for port in ports:
        net_propagation.additional_actions(transfer_file, propagation_script,
                                           arguments, ip, port, username)


def test_append_lines_from_file_to_list():
    """
    This function tests the append_lines_from_file_to_list function in the
    net_propagation script. It feeds in a test file, and we check the result it
    returns for validity. Each line is checked independently without a for loop
    for readability in test results i.e. we'll be able to correlate a specific
    line with an error.
    """
    test_file = file.File(strings.FILE)
    lines_list = test_file.append_lines_from_file_to_list()
    assert lines_list[0] == strings.LINES[0]
    assert lines_list[1] == strings.LINES[1]
    assert lines_list[2] == strings.LINES[2]
    assert lines_list[3] == strings.LINES[3]
    assert lines_list[4] == strings.LINES[4]
    assert lines_list[5] == strings.LINES[5]


def test_assigning_values():
    """
    This function tests the assigning_values function in the net_propagation
    script. It uses example arguments to do this stored in strings.py, but
    before it does that the bad path is checked by passing in a single argument
    with no value to get a runtime error.
    """
    num_arguments = 8
    happy_path_range = 4
    for arguments_selection in range(num_arguments):
        if arguments_selection < happy_path_range:
            assert net_propagation.assigning_values(
                strings_functions.arguments_sets(arguments_selection)) is not \
                   None
        else:
            assert net_propagation.assigning_values(
                strings_functions.arguments_sets(arguments_selection)) is None


def test_check_over_ssh():
    """
    This function tests the check_check_over_ssh function, it will always fail
    for now until I figure out how to mock an SSH connection.
    """
    test_file = file.File(strings.FILE)
    assert net_propagation.check_over_ssh(test_file.filename, strings.TEST_IP,
                                          strings.SSH_PORT, strings.ADMIN,
                                          strings.ADMIN) is True


def test_convert_file_to_list():
    """
    This function tests the convert_file_to_list function, it does this by
    passing in one valid filename and one invalid filename.
    """
    test_file = file.File(strings.IP_LIST_SHORT)
    assert test_file.convert_file_to_list() is not None
    test_file = file.File(strings.PWDS_LIST_SHORT)
    assert test_file.convert_file_to_list() is not None
    test_file = file.File(strings.TEST_IP)
    assert test_file.convert_file_to_list() is None


def test_exit_and_show_instructions(capfd):
    """
    This function tests the exit_and_show_instructions function.
    Should just run straight through no problem hence why all this function
    does is run that function and check what shows up in the console, errors or
    exceptions will fail this test for us
    :param capfd: Parameter needed to capture log output.
    """
    net_propagation.exit_and_show_instructions()
    out, err = capfd.readouterr()
    assert out == strings_functions.help_output() + "\n" + strings.EXITING + \
           "\n"


def test_file_error_handler(capfd):
    """
    This function tests the file_error_handler function. Should just run
    straight through no problem hence why all this function does is run that
    function and check what shows up in the console, errors or exceptions will
    fail this test for us
    :param capfd: Parameter needed to capture log output.
    """
    test_file = file.File(strings.FILE)
    test_file.file_error_handler()
    out, err = capfd.readouterr()
    assert out == strings_functions.help_output() + "\n" + strings.EXITING + \
           "\n"
