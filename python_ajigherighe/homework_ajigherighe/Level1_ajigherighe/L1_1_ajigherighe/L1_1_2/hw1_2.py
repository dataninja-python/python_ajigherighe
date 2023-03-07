#!/usr/bin/env python3

# Section:          Level 1
# Exercise:         1.2
# Testing:          Python Syntax
# Creation Date:    3/2/2023
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


from python_ajigherighe.homework_ajigherighe.Level1_ajigherighe.L1_1_ajigherighe import hw1_1


# This function checks if the string is empty ( x == "" ).
# Structure: function
# Intent: check if the supplied string is empty, which is the default in the parent function
# Success:
#   - return True or False
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def is_empty_string(string_to_check):
    """
    Checks if the supplied list is empty
    :return: Boolean. False = empty list. True = !False.
    """
    if not string_to_check:
        return True
    return False


# This function replaces the space between words with a supplied separator.
# Structure: function
# Intent: replace a desired character with a separator
# Success:
#   - return copy of the supplied string with replacements made
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def replace_space(input_string, replace_this, replace_with):
    """
    Replaces the 'replace_this' with the 'replace_with' ascii code in a new string
    :return: Copy of the string after replacement.
    """
    output_string = input_string.replace(replace_this, replace_with)
    return output_string


# This function takes the provided string and, if not empty, displays it as desired
# Structure: function
# Intent: print the provided string with a new line or tab where spaces were in the original word
# Success:
#   - displaying the string as desired
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def display_string(a_string="", to_replace=" ", separator=" "):
    """
    Replace desired element in the supplied string with the provided string
    :return: None
    """
    if not is_empty_string(a_string):
        print("\nWe are able to proceed so the string is not empty.")
        to_screen = f"We seek to replace {to_replace} in {a_string} with {separator}."
        print(repr(to_screen))
        new_string = replace_space(a_string, to_replace, separator)
        print(new_string)
    else:
        print("\nThe supplied string is empty. To proceed, provide a string.")


# This is the main function that runs each Level 1 homework section
# Structure: function
# Intent: print each item in a list as a line on the console
# Success:
#   - loop through list printing each line
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def hw1_2():
    """
    If required files are imported, the overview() and display_hello_world() functions are run.
    :return: None
    """
    print("The goal of this homework is to display each word in 'Hello World!' on the screen as desired.")
    print("My definition of this problem (after looking at the next exercise as well) is to create this function that")
    print("for homework 1.2 it replaces the 'Hello World!' space with a new line.")
    print("for homework 1.3 it replaces the 'Hello World!' space with a tab.")
    print("Right now, the ascii codes used are hardcoded but this can be rewritten to allow inputing any valid code.\n")
    hello = 'Hello World!'
    separator = '\n'
    spacer = ' '
    if hw1_1.were_files_imported():
        # hw1_1.hw1_helpers.overview()
        display_string(hello, spacer, separator)
    else:
        print("Unexpected error! Please examine code.")


################################################################################################################
# Putting parentheses around the '__name__ ... ' section allows us to test this as a standalone script
# and to import it as a module alone or as part of the larger package
################################################################################################################
if (__name__ == '__main__'):
    # print("This package can be run as a standalone module or imported into a larger program.")
    # print("For this homework submission, run.py only allows the selection of this homework assignment.")
    hw1_2()
