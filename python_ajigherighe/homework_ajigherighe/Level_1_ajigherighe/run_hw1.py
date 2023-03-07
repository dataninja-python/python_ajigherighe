#!/usr/bin/env python3

################################################################################################################
# This contains items used in the homework for level 1
################################################################################################################

# import all files in this homework section

from python_ajigherighe.homework_ajigherighe.Level_1_ajigherighe.L1_2_ajigherighe import hw1_2
from python_ajigherighe.homework_ajigherighe.Level_1_ajigherighe.L1_3_ajigherighe import hw1_3
from python_ajigherighe.homework_ajigherighe.Level_1_ajigherighe.L1_4_ajigherighe import hw1_4
from python_ajigherighe.homework_ajigherighe.Level_1_ajigherighe.L1_5_ajigherighe import hw1_5
from python_ajigherighe.homework_ajigherighe.Level_1_ajigherighe.L1_6_ajigherighe import hw1_6
from python_ajigherighe.homework_ajigherighe.Level_1_ajigherighe.hw1_constants import SWITCHER


# Structure: function
# Intent: invokes the main function from the corresponding homework exercise
# Success:
#   - Lets the user run the imported homework's main function
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def one_one():
    """
    Runs the main function for 1.1
    :return: None.
    """
    from python_ajigherighe.homework_ajigherighe.Level_1_ajigherighe.L1_1_ajigherighe import hw1_1
    print("Reviewing Homework 1.1")
    hw1_1.hw1_1()


# Structure: function
# Intent: prints an overview for the grader
# Success:
#   - True if parameter can be a float. False otherwise.
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def overview():
    """
    This function introduces the level 1 homework section.
    :return: None
    """
    print("\n###########################################################")
    print("This is the Exercise submission for: Level 1: Python Syntax 101")
    print("It contains submissions for: Exercises 1.1 - 1.6")
    print("This is the work of: Akpovogho 'AJ' Igherighe")
    print("Student email: aj@redstonema.com")
    print("Student phone: 404.247.7687")
    print("###########################################################")
    print("###########################################################\n")


# Structure: function
# Intent: Homework #1 main function that allows a grader to review each exercise's results
# Success:
#   - Reviewer is able to quickly and easily complete his/her/their job of judging my ability to solve problems
# using Python
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def main_hw1():
    overview()
    one_one()


################################################################################################################
# Press the green button in the gutter to run the script.
################################################################################################################
if (__name__ == '__main__'):
    # print("This package can be run as a standalone module or imported into a larger program.")
    # print("For this homework submission, run.py only allows the selection of this homework assignment.")
    main_hw1()
