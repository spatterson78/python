#!/usr/bin/env python3

#  Import any necessary modules
import sys


#  Create function to OS Type using a Dictionary
def get_os_type():
    """This Function will return the base Operating System"""
    platforms = {
        "linux1": "Linux",
        "linux2": "Linux",
        "darwin": "OS X",
        "win32": "Windows"
    }

    #  display platform type if not listed above
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]


print(get_os_type())

