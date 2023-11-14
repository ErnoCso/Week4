# !/usr/bin/env python 3

# Task 4

# When processing data it is o en useful to remove the last character from some
# input (it is oft en a newline). Write and test a function that takes a string parameter
# and returns it with the last character removed. (If the string contains one or fewer
# characters, return it unchanged.)

def rem_last_char(entered_data):
    if len(entered_data) <= 1:
        return entered_data
    else:
        return entered_data[:-1]


if __name__ == "__main__":

    entered_data = input("Enter a string: ")
    result = rem_last_char(entered_data)
    print("Modified string:", result)


# Output:

# Enter a string: Eagle
# Modified string: Eagl
#
# Enter a string: a
# Modified string: a
