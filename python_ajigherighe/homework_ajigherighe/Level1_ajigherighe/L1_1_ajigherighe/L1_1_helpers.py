# This function returns the absolute file and directory path of whatever file calls it.
# The absolute file path is @ index 0. The absolute directory path is @ index 1.
def get_working_file_location():
    """
    This function returns a list containing two strings of the absolute file and directory path
    :return: a list where the [0] index contains the absolute file path and the [1] index contains
    the absolute directory path
    """
    import os
    file_path = os.path.abspath(__file__)
    dir_path = os.path.dirname(file_path)
    return [file_path, dir_path]


# This function returns the absolute file and directory path for THIS file.
# It uses calls the get_working_file_location() function within THIS file.
# Intent: return a list of the absolute file and directory path for this file
# Success:
#   - displays the file and directory absolute path on the screen and returns a list
# Failure:
#   - any other outcome
def get_this_files_location():
    """
    This returns the path to THIS file itself
    :return: the list for THIS homework helper file
    """
    this_file = get_working_file_location()
    # [print(line) for line in this_file]
    return this_file


# This function prints out useful information to the grader
def overview():
    """
    This function introduces the level 1 homework section.
    :return: None
    """
    print("###########################################################")
    print("This is an Exercise submission for: 'Level 1: Python Syntax 101'")
    print("Exercises in this section go from 1.1 to 1.6.")
    print("This is the submission for: Akpovogho 'AJ' Igherighe")
    print("Student's email: aj@redstonema.com")
    print("Student's phone: 404.247.7687")
    print("###########################################################")


# Structure: function
# Intent: tests if a supplied parameter can be cast as an integer
# Success:
#   - True if parameter can be a integer. False otherwise.
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def valid_integer(test_value="integer"):
    """
    Test if a value can be cast to an integer. Approach: use the try/except built-in error checking functionality.
    This is a useful function that likely will be reused in other homeworks and the final case. Thus, it has been
    added to this helper file.
    :return: Boolean. True = a float. False = !True.
    """
    # print(f"Testing if {test_value} can be transformed into a float")
    try:
        # recasting user input into a float
        # if this fails the input is not a valid floating point number
        # and the except clause should be triggered
        int(test_value)
        # print("Can become a float. Returning False.")
        return True
    except ValueError:
        # print("Not a valid float.")
        return False


# Structure: function
# Intent: tests if an input matches a key in a dictionary
# Success:
#   - True if parameter can be a integer. False otherwise.
# Failure:
#   - !success
#   - illogical code that takes longer than 10 seconds to understand
def is_in_options(test_value="0", the_dict={}):
    """
    Test if the test_value has an associated value in a dictionary's key-value mapping.
    :return: Boolean. True = key-value mapping found. False = no key-value mapping or !True.
    """
    # validation check #1 to see if test_value contains a non-integer
    # menu dictionary keys were intentionally made integers to make menu dictionaries different from others that
    # may be used throughout the program
    if not valid_integer(test_value):
        print("You did not enter an integer. Please try again.")
        return
    # now that we know test_value contains a string that can become an integer, we convert it to an integer
    test_value = int(test_value)
    # validation check #2 to ensure function was called with non-default parameters
    if test_value == 0 or the_dict == {}:
        print("One or more parameters were not supplied. Please try again.")
        return
    # this expression does the 'work' in this function
    # it should return true if a value is found using the value as a key
    # it should return false in any other case
    is_a_key = test_value in the_dict
    return is_a_key


# overview()
# get_this_files_location()
