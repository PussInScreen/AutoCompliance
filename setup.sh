#!/usr/bin/env bash
# Linux setup for running the scripts locally, mostly needed for demos.
# TODO: Need to figure out why Paramiko has to be installed natively too, and Scapy
# sudo dnf install python3-paramiko pytest

python3 -m pip install --upgrade pip ipykernel paramiko scapy pytest requests coverage
