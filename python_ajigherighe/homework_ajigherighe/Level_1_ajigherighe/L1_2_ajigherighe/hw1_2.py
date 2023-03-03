#!/usr/bin/env python3

# Section:          Level 1
# Exercise:         1.2
# Testing:          Python Syntax
# Creation Date:    3/2/2023
# Development OS:   Ubuntu 22.04
#   - NOTE: if there is a compatibility issue with windows, macOS, or any other system, please
#   let me know. I may be able to use another language (Go, Rust, Lisp, Haskell, Typescript, C++, Fortran)
#   to make a compatible version.
# Student:          Akpo 'AJ' Igherighe
# Email1:           aj@redstonema.com
# Email2:           akpoigherighe@gmail.com
# Phone:            404.247.7687
# Requirements:
#   - Python 3.9.13
#   - Unzip and open the entire 'python_ajigherighe folder' as a project
#       - NOTE: non-tested but shared functionality is stored in the 'hw1_helpers.py' file
#   - PyCharm
#   - Terminal/Shell (optional if using PyCharm)

from python_ajigherighe.homework_ajigherighe.Level_1_ajigherighe import hw1_helpers
from python_ajigherighe import helpers


# Confirms the required modules/packages were imported
# Structure: function
# Intent: check it is possible to perform hw1_helpers.overview() function
# Success:
#   - 'Thanks for importing my full homework file.' output to the screen
#   - printing the appropriate error message to coincide with the error
# Failure:
#   - !success
#   - unexpected behavior from extra complexity
#   - illogical code that takes longer than 10 seconds to understand
def were_files_imported():
    """
    Function checks whether a specific imported function can be executed
    :return: Boolean. True = function can be run because imported. False = import related error.
    """
    try:
        # attempts to call the desired function within the try section
        # if it works, returns True
        hw1_helpers.overview()
        type(helpers.InvalidImportException)
        return True
    # function failed. now, we check if it is a common import error
    except ModuleNotFoundError:
        print("It is a common 'module not found error'")
        return False
    # if not a common error, we use our custom import error
    except helpers.InvalidImportException:
        print("This case uses a custom general import exception.")
        return False


# This function checks if the string is empty ( x == "" ).
# Structure: function
# Intent: check if the supplied string is empty, which is the default in the parent function
# Success:
#   - return True or False
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def is_empty_string(string_to_check):
    """
    Checks if the supplied list is empty
    :return: Boolean. False = empty list. True = !False.
    """
    if string_to_check:
        return True
    return False


# This function takes the provided string and, if not empty, displays it as desired
# Structure: function
# Intent: print the provided string with a new line or tab where spaces were in the original word
# Success:
#   - displaying the string as desired
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def display_string(a_string="", replace_space_with=' '):
    """
    Replace spaces in the supplied string with the provided ascii code
    :return: None
    """
    print("The goal is to display each word in 'Hello World!' on new line on the screen.")
    print("My definition of this problem (after looking at the next exercise as well) is to create a function that")
    print("replaces the space between 'Hello World!' with the ascii symbols for a new line and tab.")
    print(f"{a_string} is the supplied string. {a_string} is empty = {is_empty_string(a_string)}")
    if is_empty_string(a_string):
        print("We are able to proceed so the string is not empty.")
        print(f"We seek to replace the spaces in {a_string} with {replace_space_with}")
        print("Here is the result to replace the space with a new line: \n")
    print("The supplied string is empty. To proceed, provide a string.")


# This is the main function that runs each Level 1 homework section
# Structure: function
# Intent: print each item in a list as a line on the console
# Success:
#   - loop through list printing each line
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def hw1_2():
    """
    If required files are imported, the overview() and display_hello_world() functions are run.
    :return: None
    """
    if were_files_imported():
        hw1_helpers.overview()
        display_string()
    else:
        print("Unexpected error! Please examine code.")


################################################################################################################
# Putting parentheses around the '__name__ ... ' section allows us to test this as a stand alone script
# and to import it as a module alone or as part of the larger package
################################################################################################################
if (__name__ == '__main__'):
    # print("This package can be run as a standalone module or imported into a larger program.")
    # print("For this homework submission, run.py only allows the selection of this homework assignment.")
    hw1_2()
