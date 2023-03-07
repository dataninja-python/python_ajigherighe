#!/usr/bin/env python3

################################################################################################################
# This contains items used in the homework for level 1
################################################################################################################

# import all files in this homework section

from python_ajigherighe.homework_ajigherighe.Level1_ajigherighe.L1_1_ajigherighe.hw1_1 import hw1_1 as runhw1_1
from python_ajigherighe.homework_ajigherighe.Level1_ajigherighe.L1_2_ajigherighe.hw1_2 import hw1_2 as runhw1_2
from python_ajigherighe.homework_ajigherighe.Level1_ajigherighe.L1_3_ajigherighe.hw1_3 import hw1_3 as runhw1_3
from python_ajigherighe.homework_ajigherighe.Level1_ajigherighe.L1_4_ajigherighe.hw1_4 import hw1_4 as runhw1_4
from python_ajigherighe.homework_ajigherighe.Level1_ajigherighe.L1_5_ajigherighe.hw1_5 import hw1_5 as runhw1_5
from python_ajigherighe.homework_ajigherighe.Level1_ajigherighe.L1_6_ajigherighe.hw1_6 import hw1_6 as runhw1_6


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
    print("Reviewing Homework 1.1")
    runhw1_1()


# Structure: function
# Intent: invokes the main function from the corresponding homework exercise
# Success:
#   - Lets the user run the imported homework's main function
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def one_two():
    """
    Runs the main function for 1.2
    :return: None.
    """
    print("Reviewing Homework 1.2")
    runhw1_2()


# Structure: function
# Intent: invokes the main function from the corresponding homework exercise
# Success:
#   - Lets the user run the imported homework's main function
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def one_three():
    """
    Runs the main function for 1.3
    :return: None.
    """
    print("Reviewing Homework 1.3")
    runhw1_3()


# Structure: function
# Intent: invokes the main function from the corresponding homework exercise
# Success:
#   - Lets the user run the imported homework's main function
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def one_four():
    """
    Runs the main function for 1.4
    :return: None.
    """
    print("Reviewing Homework 1.4")
    runhw1_4()


# Structure: function
# Intent: invokes the main function from the corresponding homework exercise
# Success:
#   - Lets the user run the imported homework's main function
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def one_five():
    """
    Runs the main function for 1.5
    :return: None.
    """
    print("Reviewing Homework 1.5")
    runhw1_5()


# Structure: function
# Intent: invokes the main function from the corresponding homework exercise
# Success:
#   - Lets the user run the imported homework's main function
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def one_six():
    """
    Runs the main function for 1.6
    :return: None.
    """
    print("Reviewing Homework 1.6")
    runhw1_6()


# dictionary that contains the homework functions to select from
# NOTE: it took quite a bit of debugging to discover that I needed to not only list this after the functions
# but also convert valid inputs to integers before providing it to the dictionary
SELECTOR_DICT = {
    1: one_one,
    2: one_two,
    3: one_three,
    4: one_four,
    5: one_five,
    6: one_six
}


# Structure: function
# Intent: prints an overview for the grader
# Success:
#   - provides grader useful information about the student
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
# Intent: allows grader to select the desired homework to review
# Success:
#   - executes the selected function
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def selector():
    """
    This function allows the user to select a homework's main function to run.
    The default is to run the first homework assignment.
    :return: None
    """
    # need to determine how to call a function from a dictionary or other location
    SELECTOR_DICT[3]()


# Structure: function
# Intent: displays the homework assignments
# Success:
#   - displays the homework assignments
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def display_menu():
    """
    This function allows the user to select a homework's main function to run.
    The default is to run the first homework assignment.
    :return: None
    """
    # need to determine how to call a function from a dictionary or other location
    SELECTOR_DICT[3]()


# Structure: function
# Intent: allows grader to continue looking at different available assignments in this homework until ready to quit
# Success:
#   - executes the selected function
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def review_loop():
    """
    This function allows the user to select a homework's main function to run.
    The default is to run the first homework assignment.
    :return: None
    """
    while True:
        user_input = input("")
        # see if user wants to quit, if so, quit
        # validate input can be cast as an integer
        # transform into an integer if possible
        # call desired function


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
    selector()


################################################################################################################
# Press the green button in the gutter to run the script.
################################################################################################################
if (__name__ == '__main__'):
    # print("This package can be run as a standalone module or imported into a larger program.")
    # print("For this homework submission, run.py only allows the selection of this homework assignment.")
    main_hw1()
