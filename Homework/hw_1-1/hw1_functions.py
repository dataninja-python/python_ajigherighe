#!/usr/bin/env python3

################################################################################################################
# This contains items used in the homework for level 1
################################################################################################################

# imports from built in and created packages
from hw1_constants import HELLO_LIST as HELLO
from Middlewares import helpers


# this is the solution to 1.1.1
# uses a function that prints every string in a list as a line
# to print 'Hello World' on the screen
# Note: also uses an imported constant to ensure we print the right output
def hello_world():
    """
    This function prints 'Hello World!'
    :return: None
    """
    print("This function prints 'Hello World!' below.")
    print("This is often the 1st exercise when learning a new language.")
    print("Initially, I completed this simply but abstracted the solution to allow it to solve more")
    print("problems in this section.")
    print("")
    print("Printing output:\n")
    helpers.print_lines_to_screen(HELLO)


# This is the main function that runs each Level 1 homework section
def hw1():
    hello_world()


################################################################################################################
# Press the green button in the gutter to run the script.
################################################################################################################
if (__name__ == '__main__'):
    # print("This package can be run as a standalone module or imported into a larger program.")
    # print("For this homework submission, run.py only allows the selection of this homework assignment.")
    hw1()
