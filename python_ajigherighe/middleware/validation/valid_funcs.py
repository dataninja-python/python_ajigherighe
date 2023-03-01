#!/usr/bin/env python3

from homework_ajigherighe.middleware import constants


# test to see value sent can be recast into a float
def not_valid_float(test_value):
    """
    Tests if an input is a float
    :param test_value: a string to be tested to see if it can be a floating point number
    :return: boolean. True = can not be a floating point number; False = can be a floating point number.
    """
    # print("Entering not_valid_float function...")
    try:
        float(test_value)
        print(f"{test_value} can become a floating point (decimal) number.")
        # print("...Exiting not_valid_int function")
        return False
    except ValueError:
        # int(test_value)
        # print(ValueError)
        print(f"{test_value} can not become a floating point (decimal) number.")
        # print("...Exiting not_valid_float function")
        return True


# test to see value sent can be recast into an integer
def not_valid_int(test_value):
    """
    Tests if an input is an int
    :param test_value: a string to test if it can be an integer.
    :return: boolean. True = can not be an integer; False = can be an integer.
    """
    print("Entering not_valid_int function...")
    try:
        int(test_value)
        print(f"{test_value} can become an integer.")
        # print("...Exiting not_valid_int function")
        return False
    except ValueError:
        # int(test_value)
        # print(ValueError)
        print(f"{test_value} can not become an integer.")
        # print("...Exiting not_valid_int function")
        return True


# test if value says you should exit the loop
def quit_main_loop(test_value):
    """
    Tests if you should quit the loop
    :param test_value: the input value
    :return: True if test_value equals 'q', False for any other value
    """
    print("\nThis is the quit loop test function. It checks if the user entered 'q' or 'Q' to quit.")
    user_input = test_value.lower()
    # since 'Q' or 'q' will be used throughout my code going forward I added it as a high level
    # constant that can be reached and imported from outside a specific script
    tester = constants.QUIT_CODE.lower()
    if user_input == tester:
        print(f"User entered: {user_input}.")
        print("")
        # print("Thanks for using A.J. Igherighe's homework program.")
        # print("Again, if there are suggestions, please email them to: akpoigherighe@gmail.com.")
        print("Quiting this loop!")
        return True
    # print("User wishes to continue.")
    return False


def main_valid():
    pass


###############################################################
# Press the green button in the gutter to run the script.
if (__name__ == '__main__'):
    test_values = ['Q', 1, 'w', 'q', 's', 45, '!']
    [quit_main_loop(str(item)) for item in test_values]
