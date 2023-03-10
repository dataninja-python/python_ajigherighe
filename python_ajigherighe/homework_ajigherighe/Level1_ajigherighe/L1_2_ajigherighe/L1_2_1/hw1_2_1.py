#!/usr/bin/env python3

# Section:          Level 1
# Exercise:         1.2.2
# Testing:          Python Syntax
# Creation Date:    3/10/2023
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

from python_ajigherighe.helpers import InvalidImportException

from python_ajigherighe.homework_ajigherighe.Level1_ajigherighe.L1_1_ajigherighe.L1_1_1 import hw1_1_1


# Structure: function
# Intent: display an overview for this homework
# Success:
#   - user understands what this homework accomplishes
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def display_overview():
    """
    Tells user what this homework does
    :return: None
    """
    print("The goal of this homework is to create a list and perform a series of operations on it.")
    print("For simplicity, each action will be made a function and each function will explain what it does.")


# Structure: function
# Intent: converts input to float if possible
# Success:
#   - converts only inputs that can become floating point numbers into floating point numbers
#   - display an error message otherwise
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def generate_a_list(list_size=1, random=True, min_number=0, max_number=10):
    """
    This function should create a list with a specific number of random numbers within a specified range that can
     be either all integers or floating points
    :return: None
    """
    return [number for number in range(min_number, max_number)]


# Structure: function
# Intent: manually calculate an average using a loop
# Success:
#   - adds each number from list together using a loop
#   - counts the number of items by the number of times you go through the loop
#   - calculates the average = total / # of numbers at the end
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def calculate_average_with_loop(a_list_of_floats=[]):
    """
    Use a for loop to calculate the average of a set of numbers contained in a list
    :return: None
    """
    # check list is not empty
    if not a_list_of_floats:
        print("No numbers provided. Can not calculate the average.")
        return
    # NOTE: I assumed you did not want me to use the built-in count function
    count_of_numbers = 0
    total_of_numbers = 0
    for number in a_list_of_floats:
        # print out the initial values
        print(f"Current sum: {total_of_numbers:,.2f}")
        print(f"Current count: {count_of_numbers:,.2f}")
        # add a number from the list to the total
        total_of_numbers += number
        # increment the count
        count_of_numbers += 1
        # display where we are
    print("\n----------------------------------------------------")
    print(f"Final sum: {total_of_numbers:,.2f}")
    print(f"Final count: {count_of_numbers:,.2f}")
    print(f"The average: {total_of_numbers / count_of_numbers:,.2f}")
    print("----------------------------------------------------\n")


# Structure: function
# Intent: loops through and gathers user's inputs until 's' is entered
# Success:
#   - store only valid floats in a list until 's' is entered
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def run_loop():
    """
    Asks users for numbers until the letter 's' is entered
    :return: None
    """
    # list object that will contain the numbers to average
    values_to_average_list = []
    while True:
        # get input from user
        user_input = input("Enter a number to include in the average (enter 's' to stop): ")
        # checks user provided an input
        if user_input == "":
            print("No input detected. Please try again.")
            continue
        # checks for quit condition
        if user_input == 's':
            print("Numbers collected.")
            # calculate the average using a loop
            print("The numbers to average are:")
            [print(f"{number:,.2f}") for number in values_to_average_list]
            calculate_average_with_loop(values_to_average_list)
            # exit the function
            return
        # checks if input can be converted to a floating point number
        if is_float(user_input):
            # converts input
            user_input = float(user_input)
            # adds input to a list
            values_to_average_list.append(user_input)


# This is the main function that runs each Level 1 homework section
def hw1_2_2():
    """
    If required files are imported, the overview() and display_hello_world() functions are run.
    :return: None
    """
    if hw1_1_1.were_files_imported():
        display_overview()
        print(generate_a_list())
    else:
        print("Unexpected error! Please examine code.")


################################################################################################################
# Putting parentheses around the '__name__ ... ' section allows us to test this as a standalone script
# and to import it as a module alone or as part of the larger package and program
################################################################################################################
if (__name__ == '__main__'):
    # print("This package can be run as a standalone module or imported into a larger program.")
    # print("For this homework submission, run.py only allows the selection of this homework assignment.")
    hw1_2_2()
