#!/usr/bin/env python3

from python_ajigherighe.middleware.constants.constants import QUIT_CODE
from python_ajigherighe.middleware.validation import valid_funcs


# This is an infinite loop that does not end until the user enters the correct command.
# Throughout this course, unless otherwise specified, the letter 'Q' will be the command
# to quit such loops. It is a constant called the QUIT_CODE.
def menu_loop():
    while True:
        user_input_str = input("Make a selection or enter the letter 'q' to quit. Enter here -> ")
        # for usability the function lets the user know nothing was entered
        if not user_input_str:
            print("You did not make a selection. Please try again.\n")
            continue
        # next we must check if the user wants to quit before proceeding
        # this is because, unless otherwise specified, menu selections will be made via
        # the user entering an integer to coincide a desired choice
        if valid_funcs.quit_loop(user_input_str):
            break
        # except for the letter q - upper or lowercase - only integers are valid going forward
        if not valid_funcs.not_valid_int(user_input_str):
            print("You did not enter a valid option. Please try again.\n")
            continue


# This function gives the instructions to the user the first time
def print_instructions():
    """
    This function instructs the user on how to use the program the first time.
    :return: None
    """
    # it simply prints a set of statements
    # future improvements could be to abstract away the need to manually type these lines
    # then create a function that takes any lines from a list or dict and prints them
    # this would allow the reuse of this functionality.
    print("")
    print("####################################################################################")
    print("This function allows you to select from a predefined set of options.")
    print("To make a selection, enter the designated number at the prompt.")
    print("To quit, enter the letter 'q' or 'Q'. If anything else is entered,")
    print("this process will restart and continue until you make a valid entry or quit.")
    print("####################################################################################")
    print("")


################################################################################################################
# This function continues asking the user for input until the proper selection is made
################################################################################################################
def main_selection(user_input="Q"):
    """
    This program's main function. It allows the user to select from a menu of options.
    :return: None
    """
    print_instructions()
    menu_loop()


################################################################################################################
# Press the green button in the gutter to run the script.
################################################################################################################
if (__name__ == '__main__'):
    main_selection()
