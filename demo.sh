#!/usr/bin/env bash
# For demo purposes only, runs demo.py

# Running the propagation script across numerous services (SSH, Web)
echo "Running the propagation script across numerous services (SSH, Web)"
sudo ./autocompliance/src/demo.py -t autocompliance/src/test_files/ip_list_short.txt -p \
22,25,80 -u admin -f autocompliance/src/test_files/passwords_list_short.txt

# Running the propagation script just across SSH
echo "Running the propagation script just across SSH"
sudo ./autocompliance/src/demo.py -t autocompliance/src/test_files/ip_list_short.txt -p \
22 -u root -f autocompliance/src/test_files/passwords_list_short.txt

# Running the propagation script just across SSH and spreading a specific file.
echo "Running the propagation script just across SSH and spreading a specific file"
sudo ./autocompliance/src/demo.py -t autocompliance/src/test_files/ip_list_short.txt -p \
22 -u root -f autocompliance/src/test_files/passwords_list_short.txt -d \
src/test_files/file.txt

# Running the propagation script across SSH but acquiring IPs through a local
# scan and then subsequently self propagating.
echo "Running the propagation script across SSH but acquiring IPs through a \
local scan and then subsequently self propagating."
sudo ./autocompliance/src/demo.py -L -p 22 -u root -f autocompliance/src/test_files/\
passwords_list_short.txt -P
