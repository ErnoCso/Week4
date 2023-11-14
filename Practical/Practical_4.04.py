#!/usr/bin/env python 3

# Task 4
#
# Re-Input the above function definition, but this time add a docstring
# that includes a description of the function’s purpose. Once that is
# done enter a command such as help(displayTwice) and see what it displays.


def displayTwice(msg):
    """
    This function displays the typed text twice.

    Args:
        text (str): The text to be displayed twice.

    """
    print("*****", msg)
    print("*****", msg)


if __name__ == "__main__":

    displayTwice("This sentence will be display twice.")
    displayTwice("And this too, if I think correctly.")
    help(displayTwice)


# ***** This sentence will be display twice.
# ***** This sentence will be display twice.
# ***** And this too, if I think correctly.
# ***** And this too, if I think correctly.
# Help on function displayTwice in module __main__:
#
# displayTwice(msg)
#     This function displays the typed text twice.
#
#     Args:
#         text (str): The text to be displayed twice.