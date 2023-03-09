#!/usr/bin/env python3

# Section:          Level 1
# Exercise:         1.1.5
# Testing:          Python Syntax
# Creation Date:    3/6/2023
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

from python_ajigherighe.homework_ajigherighe.Level1_ajigherighe.L1_1_ajigherighe.L1_1_4.hw1_1_4 import get_user_input


# This function returns the type of the returned user input
# Structure: function
# Intent: prints the type of user input
# Success:
#   - displays input type as desired
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def display_input_type():
    """
    Display the type of the user supplied value
    :return: None
    """
    user_input = get_user_input()
    print(f"You entered: {user_input}")
    print(f"Python treats your entry as the following type: {type(user_input)}")
    print("NOTE: Python's input function by default returns a string type.")


# This is the main function that runs each Level 1 homework section
# Structure: function
# Intent: print each item in a list as a line on the console
# Success:
#   - loop through list printing each line
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def hw1_5():
    """
    Gets user input and displays it to the screen.
    :return: None
    """
    print("The goal is to homework is to display the the type of the user's input.")
    print("My definition of this problem (after looking at the next exercise as well) is to use")
    print("the function from 1.1.4 to get an input and print it using the built-in type function.")
    display_input_type()


################################################################################################################
# Putting parentheses around the '__name__ ... ' section allows us to test this as a standalone script
# and to import it as a module alone or as part of the larger package and program
################################################################################################################
if (__name__ == '__main__'):
    # print("This package can be run as a standalone module or imported into a larger program.")
    # print("For this homework submission, run.py only allows the selection of this homework assignment.")
    hw1_5()
