#!/usr/bin/env python 3

# Task 8

# The built-in print() function supports a keyword argument called sep.
# This is used to decide what character to display between each of the
# provided positional parameters. Write some code that makes several calls
# to the print() function while setting the sep argument to values other than
# a space (which is the default).


if __name__ == "__main__":
    print("Okey", "Dokey", sep="-")

    # Example 2
    print("Chair", "Table", "Sofa", sep=", ")

    # Example 3
    print("Python", "Java", "C++", sep=" | ")

    # Example 4
    print("Strawberry", "Raspberry", "Blueberry", sep=" | ")

    # Example 5
    print("Red", "Blue", "Yellow", sep=" / ")

# Output:
#
# Okey-Dokey
# Chair, Table, Sofa
# Python | Java | C++
# Strawberry | Raspberry | Blueberry
# Red / Blue / Yellow
#
# Process finished with exit code 0