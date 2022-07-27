#!/usr/bin/env python3
#
############################################
#
# Filename: ping.py
# Author: Shawn Patterson
# Description: Script to ping host
# Usage: ./ping.py
#
#############################################

# Import Modules
import subprocess
import getpass

# Print current user and get host to ping
host = input("Hello " + getpass.getuser() + ", " + "Please enter host you wish to ping: ")
print()

# Define ping process to run
proc_ping = subprocess.Popen(
    ["ping", "-c", "3", host],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Define process output
ping_output, ping_error = proc_ping.communicate()

# Display process output
print(ping_output)
print(ping_error)

