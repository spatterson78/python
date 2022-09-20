#!/usr/bin/env python3
#
###############################################################
#
# Filename: useradd.py
# Author: Shawn Patterson
# Description: Script to collect user input to add a new
#              user to the system.
# Usage: ./useradd.py
#
###############################################################

# Import modules
import getpass
import re
import subprocess

# Pre-defined variables
# regex to verify password meets minimum requirements
regex = r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[-+_!@#$%^&*., ?])"

# Collect new user information
print()
print("Hello " + getpass.getuser() + "," " we will gather the information for the new user account.")
print()
fname = ""
while True:
    fname = input("Please enter new user's first name: ")
    if fname[0].isupper() and fname[1:].islower() and fname.isalpha():
        print(fname + " is valid""\n")
        break
    else:
        print(fname + " is not valid")

lname = ""
while True:
    lname = input("Please enter new user's last name: ")
    if lname[0].isupper() and lname[1].islower() and lname[2].isupper() and lname.isalpha():
        print(lname + " is valid""\n")
        break
    elif lname[0].isupper() and lname[1:].islower() and lname.isalpha():
        print(lname + " is valid""\n")
        break
    else:
        print(lname + " is not valid")

groups = input("Please enter additional groups separated by spaces: ")
groups_list = groups.split()
print(f"Additional groups: {groups_list}")
print()

password = ""
while True:
    password = input("Please enter password: ")
    if len(password) < 14:
        print("Password length needs to be at least 14 characters""\n")
    elif re.search(regex, password):
        print(password + " is valid""\n")
        break
    else:
        print(password + " is not valid""\n")


# Display new user information
username = fname[0].lower() + lname.lower()

print("*************************************************************""\n"
      f"New user's full name: {fname} {lname}""\n"
      f"Username: {username}""\n"
      f"Additional groups: {groups_list}""\n"
      f"New user's password: {password}""\n"
      "*************************************************************""\n"
      + getpass.getuser() + "," " is the following information correct?""\n")

yes_no = ""
while True:
    yes_no = input("Please enter either (y/n): ")
    if yes_no == "y":
        print("Proceeding with the provided information...""\n")
        break
    elif yes_no == "n":
        print("Please re-run script with correct information")
        break
    else:
        print('Was expecting either "y" or "n"')

# Run useradd command to add new user account with provided information
if not groups_list:  # If additional groups is empty, then run the following:
    print("Creating new user account...")
    # useradd -c {full name} {username}
    user_add = subprocess.Popen(
        ['sudo', 'useradd', '-c', f'"{fname} {lname}"', f'{username}'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    user_add_output, user_add_error = user_add.communicate()
    print(user_add_output + user_add_error)

if groups_list:  # If additional groups is not empty, then run the following:
    print("Creating new user account...")
    # useradd -G {additional groups} -c {full name} {username}
    groups_add = ",".join(groups_list)
    user_add = subprocess.Popen(
        ['sudo', 'useradd', '-G', f'{groups_add}', '-c', f'"{fname} {lname}"', f'{username}'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    user_add_output, user_add_error = user_add.communicate()
    print(user_add_output + user_add_error)

# Set password for new user account
print("Setting password for new user account...")
# echo {password} | sudo passwd {username} --stdin
passwd = subprocess.Popen(
    [f'echo {password} | sudo passwd {username} --stdin'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True,
    text=True
)
passwd_output, passwd_error = passwd.communicate()
print(passwd_output + passwd_error)
print()

print(f'New user account "{username}" has been added to the system with the supplied password.')
