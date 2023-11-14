#!/usr/bin/env python 3

# Task 3
#
# Write some Python code that defines a function called print_header(msg).
# This should output the value provided by the ‘msg’ parameter to the
# screen (prefixed by five asterisks ‘*****’) characters.

def print_header(text):
    print("*****", text)
    print("*****", text)


if __name__ == "__main__":
    print_header("This sentence will be display twice.")
    print_header("And this too, if I think correctly.")

# Output:

# ***** This sentence will be display twice.
# ***** This sentence will be display twice.
# ***** And this too, if I think correctly.
# ***** And this too, if I think correctly.
