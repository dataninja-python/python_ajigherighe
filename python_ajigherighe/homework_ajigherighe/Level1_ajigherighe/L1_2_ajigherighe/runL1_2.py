#!/usr/bin/env python3

################################################################################################################
# This contains items used in the homework for level 1
################################################################################################################

# import all files in this homework section

from python_ajigherighe.homework_ajigherighe.Level1_ajigherighe.L1_1_ajigherighe.L1_1_1.hw1_1_1 import hw1_1 as runhw1_1
from python_ajigherighe.homework_ajigherighe.Level1_ajigherighe.L1_1_ajigherighe.L1_1_2.hw1_1_2 import hw1_2 as runhw1_2
from python_ajigherighe.homework_ajigherighe.Level1_ajigherighe.L1_1_ajigherighe.L1_1_3.hw1_1_3 import hw1_3 as runhw1_3
from python_ajigherighe.homework_ajigherighe.Level1_ajigherighe.L1_1_ajigherighe.L1_1_4.hw1_1_4 import hw1_4 as runhw1_4
from python_ajigherighe.homework_ajigherighe.Level1_ajigherighe.L1_1_ajigherighe.L1_1_5.hw1_1_5 import hw1_5 as runhw1_5
from python_ajigherighe.homework_ajigherighe.Level1_ajigherighe.L1_1_ajigherighe.L1_1_6.hw1_1_6 import hw1_6 as runhw1_6

# created middleware imports
from python_ajigherighe.homework_ajigherighe.Level1_ajigherighe.L1_1_ajigherighe import L1_1_helpers
from python_ajigherighe.homework_ajigherighe.Level1_ajigherighe.L1_1_ajigherighe import L1_1_constants

# specific imports
from python_ajigherighe.homework_ajigherighe.Level1_ajigherighe.L1_1_ajigherighe.L1_1_4.hw1_1_4 import get_user_input
from python_ajigherighe.homework_ajigherighe.Level1_ajigherighe.L1_1_ajigherighe.L1_1_1.hw1_1_1 import \
    were_files_imported
from python_ajigherighe import constants


# Structure: function
# Intent: invokes the main function from the corresponding homework exercise
# Success:
#   - Lets the user run the imported homework's main function
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def one_one():
    """
    Runs the main function for 1.1.1
    :return: None.
    """
    print("Reviewing Homework 1.1.1")
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
    Runs the main function for 1.1.2
    :return: None.
    """
    print("Reviewing Homework 1.1.2")
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
    Runs the main function for 1.1.3
    :return: None.
    """
    print("Reviewing Homework 1.1.3")
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
    Runs the main function for 1.1.4
    :return: None.
    """
    print("Reviewing Homework 1.1.4")
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
    Runs the main function for 1.1.5
    :return: None.
    """
    print("Reviewing Homework 1.1.5")
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
    Runs the main function for 1.1.6
    :return: None.
    """
    print("Reviewing Homework 1.1.6")
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

# list with instructions for using this part of the program
# the idea is this constant is used by a function that prints each line as requested by the user or programmer
INSTRUCTIONS_LIST = [
    "---------------------------------------------------------------------------------------------",
    "This file allows you to review homework exercises in this section by selecting from a menu.",
    "After these instructions, a selection for this section menu will be displayed.",
    "To review a specific exercise in this section, enter the number that corresponds to it.",
    "NOTE: the supplied 'number' must be a positive integer (a whole number greater than 0) and",
    "the number correspond to one of the available options.",
    "At any time, you can enter 'Q' or 'q' to quit or 'i' or 'I' to see these instructions again.",
    "---------------------------------------------------------------------------------------------\n",
]


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
    print("It contains submissions for: Exercises 1.1.1 - 1.1.6")
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
def selector(selection=1):
    """
    This function allows the user to select a homework's main function to run.
    The default is to run the first homework assignment.
    :return: None
    """
    # need to determine how to call a function from a dictionary or other location
    SELECTOR_DICT[selection]()


# Structure: function
# Intent: displays the available options
# Success:
#   - shows what the user can select
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def display_menu_options(a_dict_of_options):
    """
    This function displays the options available for the user to select
    :return: None
    """
    # need to determine how to call a function from a dictionary or other location
    print("\n-------------------------------------------------------")
    print("--------------- EXERCISE SELECTION MENU ---------------")
    print("-- Enter a number to choose the corresponding option --")
    [print(f"{key}: {a_dict_of_options[key]}") for key in a_dict_of_options]
    print("-------------------------------------------------------")
    print("")


# Structure: function
# Intent: explains how to use this script, module, package, or program
# Success:
#   - user understands how to achieve the desired outcome
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def display_instructions(a_list_of_instructions):
    """
    This function displays each item in a list as a line on the screen.
    :return: None
    """
    [print(line) for line in a_list_of_instructions]


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
    # display instructions the first time
    display_instructions(INSTRUCTIONS_LIST)
    while True:
        # display menu options
        display_menu_options(L1_1_constants.L1_1_EXERCISES_DICT)
        # get user input
        user_input = get_user_input("Enter a number from the above menu (or enter 'q' to quit): ")
        # see if user wants to quit, if so, quit
        if user_input.lower() == constants.QUIT_CODE.lower():
            print("You are choosing to stop reviewing this unit. Thank you for your time. Goodbye")
            return
        # see if user wants to see the instructions again, if so display them
        if user_input.lower() == constants.INSTRUCTIONS_CODE.lower():
            display_instructions(INSTRUCTIONS_LIST)
            continue

        # see if user has entered a valid option
        # this uses a helper function that both checks if the input is an integer and if it has a matching value in the
        # options dictionary
        if L1_1_helpers.is_in_options(user_input, L1_1_constants.L1_1_EXERCISES_DICT):
            # convert user input to an integer
            user_input = int(user_input)
            # run the desired exercise
            selector(user_input)
        else:
            # we should only reach here if an invalid entry was made
            print("Invalid entry. Enter 'i' to see the instructions again.\n")
            continue


# Structure: function
# Intent: Homework #1 main function that allows a grader to review each exercise's results
# Success:
#   - Reviewer is able to quickly and easily complete his/her/their job of judging my ability to solve problems
# using Python
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def main_hw1_1():
    if were_files_imported():
        overview()
        review_loop()
    else:
        print("Unexpected error")


################################################################################################################
# Press the green button in the gutter to run the script.
################################################################################################################
if (__name__ == '__main__'):
    # print("This package can be run as a standalone module or imported into a larger program.")
    # print("For this homework submission, run.py only allows the selection of this homework assignment.")
    main_hw1_1()
