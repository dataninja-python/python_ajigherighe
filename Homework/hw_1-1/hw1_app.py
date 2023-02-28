#!/usr/bin/env python3

################################################################################################################
# This contains items used in the homework for level 1
################################################################################################################

import hw1_functions

def overview():
    """
    This function introduces this homework section to the grader.
    :return:
    """
    print("")
    print("###########################################################")
    print("This is the Exercise submission for: Level 1: Python Syntax 101")
    print("It contains submissions for: Exercises 1.1 - 1.6")
    print("This is the work of: Akpovogho 'AJ' Igherighe")
    print("Student email: aj@redstonema.com")
    print("Student phone: 404.247.7687")
    print("###########################################################")
    print("###########################################################")
    print("")


# This is the main function that runs each Level 1 homework section
def main_hw1():
    overview()
    hw1_functions.hello_world()


################################################################################################################
# Press the green button in the gutter to run the script.
################################################################################################################
if (__name__ == '__main__'):
    print("This package can be run as a standalone module or imported into a larger program.")
    print("For this homework submission, run.py only allows the selection of this homework assignment.")
    main_hw1()
