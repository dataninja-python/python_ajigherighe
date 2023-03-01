#!/usr/bin/env python3


# instructions function
def print_instructions():
    # print("This function prints the instructions each time through the loop.")
    # print("Enter a number to select one of the available options.")
    print("")
    print("Select one of the options below.")
    # for key in selections.USER_OPTIONS:
    #   a_line = key + " = " + selections.USER_OPTIONS[key]
    #   print(a_line)


# This is the core program loop. It continues until quit.
def app_loop():
    """
    This is the program's main loop that right now takes a users input.
    Then, allows you to make a selection.
    :return:
    """
    # print("This is the main loop function. It takes you into an endless while loop.")
    # pseudocode:
    # until you enter the letter 'q' to quit
    # keep asking for a user's input
    valid_options = selections.get_option_keys_in_list()
    options_strings = " ".join(str(item) for item in valid_options)
    while True:
        print_instructions()
        raw_input = input("Enter a number to review one of my homework assignments: (enter 'q' to quit) ")
        # check to see if you should quit based on whatever parameters are in quick loop function
        # if quit then break, else do the thing
        # print(f"user input: {raw_input}")
        if quit_main_loop(raw_input):
            # print("Quiting while loop...")
            break
        else:
            print("")
            print("Making a selection: ")
            if raw_input in valid_options:
                make_selection(raw_input)
            else:
                # check if the input
                if type_validators.not_valid_int(raw_input):
                    print(f"{raw_input} is not an integer.")
                    continue
                print(f"{raw_input} is not a valid option.")
                print(f"Valid options are: {options_strings}.")

                print("Please try again.")


################################################################################################################
# Press the green button in the gutter to run the script.
################################################################################################################
if (__name__ == '__main__'):
    print("Hello")
