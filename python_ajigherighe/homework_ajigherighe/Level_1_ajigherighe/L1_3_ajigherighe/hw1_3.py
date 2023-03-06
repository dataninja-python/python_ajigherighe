#!/usr/bin/env python3

# Section:          Level 1
# Exercise:         1.2
# Testing:          Python Syntax
# Creation Date:    3/6/2023
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
#       - NOTE: non-tested but shared functionality is stored in the 'hw1_helpers.py' file
#   - PyCharm
#   - Terminal/Shell (optional if using PyCharm)


from python_ajigherighe.homework_ajigherighe.Level_1_ajigherighe.L1_1_ajigherighe import hw1_1
from python_ajigherighe.homework_ajigherighe.Level_1_ajigherighe.L1_2_ajigherighe import hw1_2


# This is the main function that runs each Level 1 homework section
# Structure: function
# Intent: print each item in a list as a line on the console
# Success:
#   - loop through list printing each line
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def hw1_3():
    """
    If required files are imported, the overview() and display_hello_world() functions are run.
    :return: None
    """
    hello = 'Hello World!'
    separator = '\t'
    spacer = ' '
    if hw1_1.were_files_imported():
        hw1_1.hw1_helpers.overview()
        hw1_2.display_string(hello, spacer, separator)
    else:
        print("Unexpected error! Please examine code.")


################################################################################################################
# Putting parentheses around the '__name__ ... ' section allows us to test this as a standalone script
# and to import it as a module alone or as part of the larger package
################################################################################################################
if (__name__ == '__main__'):
    # print("This package can be run as a standalone module or imported into a larger program.")
    # print("For this homework submission, run.py only allows the selection of this homework assignment.")
    hw1_3()
