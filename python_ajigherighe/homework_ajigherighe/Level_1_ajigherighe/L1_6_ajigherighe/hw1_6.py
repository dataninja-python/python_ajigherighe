#!/usr/bin/env python3
import copy

# Section:          Level 1
# Exercise:         1.6
# Testing:          Python Syntax
# Creation Date:    3/7/2023
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

from python_ajigherighe.homework_ajigherighe.Level_1_ajigherighe.L1_4_ajigherighe import hw1_4
from python_ajigherighe.constants import QUIT_CODE


# Structure: function
# Intent: tests if a supplied parameter can be cast as a float
# Success:
#   - True if parameter can be a float. False otherwise.
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def valid_float(test_value="float"):
    """
    Test if a value can be cast to a float. Approach: use the try/except built-in error checking functionality.
    This is a useful function that likely will be reused in other homeworks and the final case.
    :return: Boolean. True = a float. False = !True.
    """
    # print(f"Testing if {test_value} can be transformed into a float")
    try:
        # recasting user input into a float
        # if this fails the input is not a valid floating point number
        # and the except clause should be triggered
        float(test_value)
        # print("Can become a float. Returning False.")
        return True
    except ValueError:
        # print("Not a valid float.")
        return False


# Structure: function
# Intent: return a dictionary with the specified value filled for the supplied key
# Success:
#   - updated dictionary with desired key-value pairing
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def put_user_float_in_dict(a_dict, key_to_fill):
    """
    Enter valid user input as the value in a dictionary key-value pair. Approach: use a loop that repeats until the
    user provides a decimal
    :return: aDict = a dictionary containing an updated dictionary
    """
    tmp_dict = copy.deepcopy(a_dict)
    quit_now = False
    while True:
        print(f"Please supply a valid value for the triangle's {key_to_fill} (enter 'q' to quit)")
        user_input = hw1_4.get_user_input()
        # allow user to quit the loop by entering 'q' or 'Q'
        # default action is to make the value attached to the current key = 0.0
        # changed from simply breaking out of the function to returning early on quit and
        # returning if the user's input suggest he/she/they want to end the program
        if user_input.lower() == QUIT_CODE.lower():
            tmp_dict[key_to_fill] = 0.0
            tmp_dict["quit"] = True
            return tmp_dict
        # if user does not quit check validity
        valid = valid_float(user_input)
        # check if the supplied user input can become a floating point number
        if not valid:
            print(f'{user_input} is invalid. Please provide a positive number with or without decimals.')
            continue
        else:
            print(f"{user_input} is valid and will be the {key_to_fill} of the triangle.")
            tmp_dict[key_to_fill] = float(user_input)
            return tmp_dict


# This function returns the type of the returned user input
# Structure: function
# Intent: prints the type of user input
# Success:
#   - displays input type as desired
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def calculate_triangle_area():
    """
    Calculates and displays a triangle's area by multiplying base x height supplied by user
    :return: None
    """
    triangle_dict = {
        "base": 0.0,
        "height": 0.0,
        "area": 0.0,
        "quit": False
    }
    # obtaining valid base and height values to calculate area
    # added functionality to allow user to quit the program
    triangle_dict = put_user_float_in_dict(triangle_dict, "base")
    # check if user quit
    if triangle_dict["quit"]:
        print("Exiting before calculating the triangle's area")
        return
    # add height to dictionary or quit
    triangle_dict = put_user_float_in_dict(triangle_dict, "height")
    # check if user quit
    if triangle_dict["quit"]:
        print("Exiting before calculating the triangle's area")
        return
    # the actual multiplications of the base x height values stored in the dictionary as well
    triangle_dict["area"] = triangle_dict["base"] * triangle_dict["height"]
    for key in triangle_dict:
        if key == "quit":
            continue
        print(f"The triangle's {key} is {triangle_dict[key]}.")


# This is the main function that runs each Level 1 homework section
# Structure: function
# Intent: print each item in a list as a line on the console
# Success:
#   - loop through list printing each line
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def hw1_6():
    """
    Gets user input and displays it to the screen.
    :return: None
    """
    print("The goal of this homework is to calculate a triangle's area using 2 user supplied inputs.")
    print("My definition of this problem (after looking at the next exercise as well) is to use the")
    print("function from 1.4 to get inputs, validate each input using try/except, ")
    print("multiply inputs that can be recast at floating point numbers together, and display them.\n")
    calculate_triangle_area()


################################################################################################################
# Putting parentheses around the '__name__ ... ' section allows us to test this as a standalone script
# and to import it as a module alone or as part of the larger package
################################################################################################################
if (__name__ == '__main__'):
    # print("This package can be run as a standalone module or imported into a larger program.")
    # print("For this homework submission, run.py only allows the selection of this homework assignment.")
    hw1_6()
