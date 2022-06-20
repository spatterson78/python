#!/usr/bin/env python3
#
#######################################
# Filename: ping.py
# Author: Shawn Patterson
# Description: Script to ping host
#######################################

# import os module
import os  

# Variables
cmd_echo = 'echo'
cmd_get_host = input("Please enter host to ping: ")
cmd_ping = 'ping -c4 ' + cmd_get_host

# System commands
os.system(cmd_echo)
os.system(cmd_ping)

