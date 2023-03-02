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


# overview()
# get_this_files_location()

