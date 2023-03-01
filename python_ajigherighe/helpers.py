
from constants import QUIT_CODE


# This loop continues until the user enters the proper input to quit
def infinite_loop():
    """
    This function continues looping through a group of options until one is selected or quit.
    :return: None
    """
    quit_code = QUIT_CODE.lower()
    while True:
        print("instructions go here")
        raw_input = input("Enter the homework level you would like to review: (or enter the letter 'q' to quit) ")
        if raw_input == quit_code:
            print("Quiting the loop...")
            break
        else:
            print("")
            print("Making a selection: ")
            print(f"{raw_input}")
