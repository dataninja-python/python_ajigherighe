#!/usr/bin/env python3

from python_ajigherighe.middleware.constants import constants


# This function allows the user to select a specific homework assignment.
def select_homework():
    # to select a specific homework:
    # 1. you should know the valid options
    # 2. you should be able to select them
    # 3. you should be able to quit
    # 4. you should get an error for invalid selections
    print(constants.VALID_HOMEWORK_OPTIONS)
    options = constants.VALID_HOMEWORK_OPTIONS.keys()
    print(f"Valid options are:{options}")
    pass


################################################################################################################
# This is the main homework function. It is the entry point for the homework.
################################################################################################################
def main_homework():
    """
    This homework module's main function. It allows the user to select what homework to review.
    :return: None
    """
    # display to user where we are in the program
    print("\n############################################################################")
    print("This function allows the selection of homework solutions ready for review.")
    print("These homework assignments are for: Akpovogho 'AJ' Igherighe")
    print("############################################################################\n")
    select_homework()


################################################################################################################
# Press the green button in the gutter to run the script.
################################################################################################################
if (__name__ == '__main__'):
    main_homework()
