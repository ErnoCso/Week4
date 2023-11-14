#!/usr/bin/env python 3

# Task 4
#
# In the answer box below give an example of what the docstring may look like for the
# print_header(msg) function.

if __name__ == "__main__":
    def print_header(msg):
        """
        This function displays the typed text twice.

        Args:
            text (str): The text to be displayed twice.

        """
        print("*****", msg)
        print("*****", msg)


    print_header("This sentence will be display twice.")
    print_header("And this too, if I think correctly.")
    help(print_header)


# ***** This sentence will be display twice.
# ***** This sentence will be display twice.
# ***** And this too, if I think correctly.
# ***** And this too, if I think correctly.
# Help on function print_header in module __main__:
#
# print_header(msg)
#     This function displays the typed text twice.
#
#     Args:
#         text (str): The text to be displayed twice.


