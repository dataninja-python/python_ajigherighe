#!/usr/bin/env python3

# import the operating system module to interact with the machine better
import os
# import a call to access the terminal directly
from subprocess import call
# importing sleep function to allow doing something for a period
from time import sleep


def sleep_for(secs=1):
    """
    Function that delays console for a set period of time.
    :param secs: amount of time in seconds to delay an action
    :return: None
    """
    sleep(secs)


def clear_screen():
    # clear screen based on what will work with operating system
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


################################################################################################################
# Press the green button in the gutter to run the script.
################################################################################################################
if (__name__ == '__main__'):
    print("Hello")
    sleep_for()
    print("World")
    try:
        clear_screen()
    except:
        print(f"Something went wrong")
