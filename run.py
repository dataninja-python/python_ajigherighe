#!/usr/bin/env python3
from Middlewares import helpers

INTRO_LINES_LIST = [
    "",
    "",
    "###########",
    "",
    "Welcome to AJ Igherighe's python home work assignment grading program.",
    "This app was designed to make (a) grading homework easier to review and",
    "(b) allow me to practice building a more complete financial model.",
    "When this script is run, it launches the main function and enters the",
    "main program.",
    "",
    "###########",
    "",
    ""
]

INSTRUCTIONS_LINES_LIST = [
    "",
    "",
    "###########",
    "",
    "To select a homework exercise to review:",
    "1) enter one of the valid options printed after this message",
    "2) enter the letter 'Q' or 'q' to quit.",
    "Taking any action other than the two above will bring you back here.",
    "",
    "###########",
    "",
    ""
]


################################################################################################################
# Press the green button in the gutter to run the script.
################################################################################################################
def print_list_as_lines(ALIST):
    """
    This functions prints a list of strings as lines on the console.
    :param ALIST: a list of lines to be printed separately
    :return: None
    """
    [print(line) for line in ALIST]


################################################################################################################
# Press the green button in the gutter to run the script.
################################################################################################################
def main():
    """
    This program's main function. It gives an intro, instructions, and allows the user to select a homework
    assignment to review for grading.
    :return: None
    """
    print_list_as_lines(INTRO_LINES_LIST)
    helpers.sleep(2)
    helpers.clear_screen()
    print_list_as_lines(INSTRUCTIONS_LINES_LIST)


################################################################################################################
# Press the green button in the gutter to run the script.
################################################################################################################
if __name__ == '__main__':
    main()
