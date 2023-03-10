#!/usr/bin/env python3
import copy

# Section:          Level 1
# Exercise:         1.1.6
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
#       - NOTE: non-tested but shared functionality is stored in the 'L1_1_helpers.py' file
#   - PyCharm
#   - Terminal/Shell (optional if using PyCharm)

from python_ajigherighe.homework_ajigherighe.Level1_ajigherighe.L1_1_ajigherighe.L1_1_4.hw1_1_4 import get_user_input
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
# Intent: checks if a number is greater than zero
# Success:
#   - True test_value > 0. False otherwise.
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def is_positive(test_value=1):
    """
    A validation function that checks if a number is positive. A positive number is defined as existing on the number
    line to the right of 0.
    :return: Boolean. True = > 0. False = < 0 (or to the left of 0 on a number line).
    """
    if test_value > 0:
        return True
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
    while True:
        print(f"Please supply a valid value for the triangle's {key_to_fill} (enter 'q' to quit)")
        user_input = get_user_input()
        # allow user to quit the loop by entering 'q' or 'Q'
        # default action is to make the value attached to the current key = 0.0
        # changed from simply breaking out of the function to returning early on quit and
        # returning if the user's input suggest he/she/they want to end the program
        if user_input.lower() == QUIT_CODE.lower():
            tmp_dict[key_to_fill] = 0.0
            tmp_dict["quit"] = True
            return tmp_dict
        # check if the supplied user input can become a floating point number
        if not valid_float(user_input):
            print(f'{user_input} is invalid. Please provide a positive number with or without decimals.')
            continue
        else:
            # to perform the remaining operations we need to convert the input to a float now
            # before putting this here, I had errors in the program
            user_input = float(user_input)
            # validate that the input is not negative or 0
            # NOTE: I confirmed that a collinear triangle can (as I thought) have a zero area
            if not is_positive(user_input) and user_input != 0:
                print(f"{user_input} is negative. This is invalid. Please enter a positive number or 0")
                continue
            print(f"{user_input} is valid and will be the {key_to_fill} of the triangle.")
            # explicitly inserting the now floating point input at the desired key
            tmp_dict[key_to_fill] = user_input
            return tmp_dict


# Structure: function
# Intent: use user inputs to calculate the area of a triangle = base x height
# Success:
#   - calculates triangles area
#   - displays base, height, and area of triangle
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
        "quit": False,
        "complete": False,
    }
    while not triangle_dict["complete"]:
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
        triangle_dict["complete"] = True
        # remembered from videos that comprehension is more efficient than looping
        # thus, to practice, I converted the commented for loop into a list comprehension
        # NOTE: another time I may test with time.time to see which is faster in reality
        # NOTE: I program on a Quad GPU, 256 GB of RAM, AMD Threadripper data science machine running Ubuntu. Thus,
        # I am unclear when sacrificing the clarity of using a for loop makes sense. I would create a virtual
        # machine with production server/machine statistics to properly optimize and configure real code.
        [print(f"The triangle's {key} is {triangle_dict[key]}") for key in triangle_dict if key != "quit" and
            key != "complete"]
        # old print approach using a for loop
        '''for key in triangle_dict:
            if key == "quit":
                continue
            print(f"The triangle's {key} is {triangle_dict[key]}.")'''


# Structure: function
# Intent: calculates a triangles area = base x height
# Success:
#   - successfully calculating and displaying a triangles area
#   - using validation to ensure the user provides data needed
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def hw1_1_6():
    """
    Calculates a triangles area = base x height using inputs from the user. Also, performs validation checks
    against empty entries (as part of the imported get_user_input function) and non integers or floating point
    numbers
    :return: None
    """
    print("The goal of this homework is to calculate a triangle's area using 2 user supplied inputs.")
    print("My definition of this problem (after looking at the next exercise as well) is to use the")
    print("function from 1.1.4 to get inputs, validate each input using try/except, ")
    print("multiply inputs that can be recast as floating point numbers together, and display them.\n")
    calculate_triangle_area()


################################################################################################################
# Putting parentheses around the '__name__ ... ' section allows us to test this as a standalone script
# and to import it as a module alone or as part of the larger package and program
################################################################################################################
if (__name__ == '__main__'):
    # print("This package can be run as a standalone module or imported into a larger program.")
    # print("For this homework submission, run.py only allows the selection of this homework assignment.")
    hw1_1_6()
