#!/usr/bin/env python3
#
#######################################################
#
# Filename: nested_list.py
# Author: Shawn Patterson
# Description: Script to iterate through nested list
# Usage: ./nested_list.py
#
#######################################################

# Import modules
import subprocess
import getpass

# Define nested list
nlist = [["Current working directory:", "pwd"],
         ["Current working directory contents:", "ls -lahtr"],
         ["Current filesystem usage:", "df -h"]]

# Print current user
print()
print("Current user is: " + getpass.getuser())
print()

# Loop through list to provide output
for text, cmd in nlist:
    proc_cmd = subprocess.Popen(
        [cmd],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=True
    )

    cmd_output, cmd_error = proc_cmd.communicate()

    print(text + '\n' + cmd_output + cmd_error)

