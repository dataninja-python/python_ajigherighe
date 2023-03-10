#!/usr/bin/env python3

# Section:          Level 1
# Exercise:         1.1.1
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
#       - NOTE: non-tested but shared functionality is stored in the 'L1_1_helpers.py' file
#   - PyCharm
#   - Terminal/Shell (optional if using PyCharm)

from python_ajigherighe.helpers import InvalidImportException


# Structure: function
# Intent: check if is required files are accessible using try/except
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
        # helpers.overview()
        type(InvalidImportException)
        return True
    # function failed. now, we check if it is a common import error
    except ModuleNotFoundError:
        print("It is a common 'module not found error'")
        return False
    # if not a common error, we use our custom import error
    except InvalidImportException:
        print("This case uses a custom general import exception.")
        return False


# Simplest way to display hello world
# Structure: function
# Intent: display 'Hello World!' on screen
# Success:
#   - output the expected message on screen
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def display_hello_world():
    """
    Print 'Hello World!'
    :return: None
    """
    print("The goal of this homework is to display 'Hello World!' on screen.")
    print("Here is the result: ")
    print("Hello World!\n")


# This is the main function that runs each Level 1 homework section
def hw1_1_1():
    """
    If required files are imported, the overview() and display_hello_world() functions are run.
    :return: None
    """
    if were_files_imported():
        # hw1_helpers.overview()
        display_hello_world()
    else:
        print("Unexpected error! Please examine code.")


################################################################################################################
# Putting parentheses around the '__name__ ... ' section allows us to test this as a standalone script
# and to import it as a module alone or as part of the larger package and program
################################################################################################################
if (__name__ == '__main__'):
    # print("This package can be run as a standalone module or imported into a larger program.")
    # print("For this homework submission, run.py only allows the selection of this homework assignment.")
    hw1_1_1()
