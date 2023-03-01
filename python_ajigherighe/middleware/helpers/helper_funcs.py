#!/usr/bin/env python3

# import the operating system module to interact with the machine better
import os
# import a call to access the terminal directly
from subprocess import call
# importing sleep function to allow doing something for a period
from time import sleep


# This loop continues until the user enters the proper input to quit
def infinite_loop():
    """
    This function continues looping through a group of options until one is selected or quit.
    :return: None
    """
    quit_code = QUIT_CODE.lower()
    while True:
        print("instructions go here")
        raw_input = input("Enter the homework level you would like to review: (or enter the letter 'q' to quit) ")
        if raw_input == quit_code:
            print("Quiting the loop...")
            break
        else:
            print("")
            print("Making a selection: ")
            print(f"{raw_input}")


def get_valid_options_from_dict(aDict):
    pass


# Input = a string from a list, such as "Hello World!"
# Output = a string with a new character between words, such as "Hello" \n "World!"
def get_modified_string(a_string="", to_replace=" ", replace_with="\n"):
    """
    This function takes a string and replaces one entered thing with another.
    To use this function, you need to pass a string, what you want to replace,
    and what to replace it with. The default settings are supplied for convenience.
    :param a_string: a python string
    :param to_replace: a subset of the supplied python string to replace
    :param replace_with: the item to put in the place of the python string
    :return:
    """
    if not a_string:
        print("You passed an empty string. Please try again.")
        return
    output = a_string.replace(to_replace, replace_with)
    return output


# Input = a list of string phrases with appropriate punctuation.
# Output = each phrase displayed as a new line on the console screen
def print_lines_to_screen(a_list_of_lines=[]):
    """
    This function prints each string as a new line on the console.
    :param a_list_of_lines: variable containing a list of lines. The default is an empty list.
    :return: None
    """
    if not a_list_of_lines:
        print("You passed an empty list. Please try again.")
        return
    # should only reach this point if a non-empty list is passed
    # uses list comprehension to print string as a new line
    [print(line) for line in a_list_of_lines]


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
