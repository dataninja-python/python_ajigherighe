#!/usr/bin/env python3

# Section:          Level 1
# Exercise:         1.2
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
#       - NOTE: non-tested but shared functionality is stored in the 'hw1_helpers.py' file
#   - PyCharm
#   - Terminal/Shell (optional if using PyCharm)

# This function stores a user input in a variable
# Structure: function
# Intent: captures user input in a variable
# Success:
#   - saving user input as desired
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def get_user_input():
    """
    Capture user input
    :return: output
    """
    output = ""
    while True:
        output = input("Please provide an input: ")
        if output == "":
            print("No input detected. Are you sure you typed something? Please try again.")
            continue

        if output != "":
            return output

# This is the main function that runs each Level 1 homework section
# Structure: function
# Intent: print each item in a list as a line on the console
# Success:
#   - loop through list printing each line
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def hw1_4():
    """
    Gets user input and displays it to the screen.
    :return: None
    """
    print("The goal of this homework is to store a user's input in a variable.")
    print("My definition of this problem (after looking at the next exercise as well) is to create a function that")
    print("is able to capture user inputs in a way you can tell the type of the variable (1.5) and")
    print("takes 2 inputs (1.6) to calculate a triangle's area.\n")
    result = get_user_input()
    print(f"You entered: {result}")



################################################################################################################
# Putting parentheses around the '__name__ ... ' section allows us to test this as a standalone script
# and to import it as a module alone or as part of the larger package
################################################################################################################
if (__name__ == '__main__'):
    # print("This package can be run as a standalone module or imported into a larger program.")
    # print("For this homework submission, run.py only allows the selection of this homework assignment.")
    hw1_4()
