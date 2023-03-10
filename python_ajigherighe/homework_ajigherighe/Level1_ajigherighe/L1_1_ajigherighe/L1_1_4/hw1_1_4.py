#!/usr/bin/env python3

# Section:          Level 1
# Exercise:         1.1.4
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

from python_ajigherighe.homework_ajigherighe.Level1_ajigherighe.L1_1_ajigherighe.L1_1_2.hw1_1_2 import is_empty_string


# Structure: function
# Intent: captures user input in a variable
# Success:
#   - saving user input in a variable as desired
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def get_user_input(input_cmd="Please provide an input:"):
    """
    Capture user input
    :return: output a local variable which contains a non-empty string supplied by the user.
    """
    # an infinite loop is used to collect user inputs
    # loop continues if nothing is entered
    while True:
        # get user's input
        output = input(input_cmd)
        # if empty "return to go and do not collect $200" lol
        # no if the user does not enter anything output or if for some unknown reason we get here output was
        # initialized empty and hitting return without making an entry results in output = an empty string
        # which will put us in the first block of this if statement
        # continue should send the user, after printing, back to the beginning of the while loop to try again
        # for now, the only way to break this loop (other than using Ctrl-C or other shell or OS specific command)
        # is to enter a value
        # NOTE: As a test, I entered "". Interestingly, this does not register as empty which made sense once I thought
        # about it, but initially I thought there may be a chance python's interpreter would see this as empty
        # NOTE: After some research, I now realize if python's input function converted "" to an empty value for the
        # variable, then a user could pass other code to the program as well. This would be a major security issue.
        if is_empty_string(output):
            print("No input detected. Are you sure you typed something? Please try again.")
            continue
        else:
            break
    return output


# This is the main function that runs each Level 1 homework section
# Structure: function
# Intent: print each item in a list as a line on the console
# Success:
#   - loop through list printing each line
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def hw1_1_4():
    """
    Gets user input and displays it to the screen.
    :return: None
    """
    print("The goal of this homework is to store a user's input in a variable.")
    print("My definition of this problem (after looking at the next exercise as well) is to create a function that")
    print("is able to capture user inputs in a variable (1.1.4) to tell the type of the variable's value (1.1.5) and")
    print("takes 2 inputs to calculate a triangle's area (1.1.6).\n")
    result = get_user_input()
    print(f"You entered: {result}")


################################################################################################################
# Putting parentheses around the '__name__ ... ' section allows us to test this as a standalone script
# and to import it as a module alone or as part of the larger package and program
################################################################################################################
if (__name__ == '__main__'):
    # print("This package can be run as a standalone module or imported into a larger program.")
    # print("For this homework submission, run.py only allows the selection of this homework assignment.")
    hw1_1_4()
