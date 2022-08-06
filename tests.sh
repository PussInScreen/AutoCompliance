#!/usr/bin/env bash
# Pytest local run with coverage and a report exported to HTML
# See; https://coverage.readthedocs.io/en/6.3.2/
cd autocompliance/src
coverage run -m pytest --durations=0 -vv --log-level=debug
coverage report
coverage html

# To test individual test files and check test speeds for pruning see and
# uncomment the following.
#pytest --durations=0 -vv --log-level=debug test_blockchain.py
#pytest --durations=0 -vv --log-level=debug test_blockchain_delegate.py
#pytest --durations=0 -vv  --log-level=debug test_blockchain_functions.py
#pytest --durations=0 -vv  --log-level=debug test_blockchain_speaker.py
#pytest --durations=0 -vv  --log-level=debug test_demo_functions.py
#pytest --durations=0 -vv  --log-level=debug test_file.py
#pytest --durations=0 -vv  --log-level=debug test_net_propagation.py
#pytest --durations=0 -vv  --log-level=debug test_strings_functions.py