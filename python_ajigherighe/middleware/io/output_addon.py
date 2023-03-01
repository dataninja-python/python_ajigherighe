#!/usr/bin/env python3


# This function gives the instructions to the user the first time
def print_lines_from_list(a_list=[]):
    """
    This function prints each item in a list on a new line.
    This is an abstracted form of the instructions function used
    in the selection_menu python file in the menu module.
    :param a_list: a passed list of items. default: empty list
    :return: None
    """
    # first we check if the list is empty
    # if the list is empty by default or an empty list is sent,
    # the user is informed and the function exits
    # Note: revision was made to make code cleaner. instead of checking
    # code against an empty list (list1 == []), we use 'truthiness' default
    # built into python that an empty list = False and non-empty = True
    if not a_list:
        print("Nothing given to print. Try again.\n")
        return
    # for non-empty lists, list comprehension is used to print
    # each item (called a line here) on a separate line since
    # this is the default behavior of the print function
    [print(line) for line in a_list]


################################################################################################################
# This function continues asking the user for input until the proper selection is made
################################################################################################################
def main_print(user_input="Q"):
    """
    This program's main function. It allows the use of this files print helper functions as a complete script.
    :return: None
    """
    random_stuff_in_list = [
        "Hello World!",
        "I like beef!",
        "Haskell is great"
    ]
    print_lines_from_list()
    print_lines_from_list(random_stuff_in_list)


################################################################################################################
# Press the green button in the gutter to run the script.
################################################################################################################
if (__name__ == '__main__'):
    main_print()
