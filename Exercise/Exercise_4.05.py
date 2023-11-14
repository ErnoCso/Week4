#!/usr/bin/env python 3

# Task 5
#
# Write some Python code that defines a function called find_min(a,b) that returns
# the smallest of the two given parameter values.

a = int(input("Please enter a value: "))
b = int(input("Please enter b value: "))

def findmin(x, y):
    """Finds the minimum of two values."""

    if x < y:
        minimum = x
    else:
        minimum = y
    return minimum


if __name__ == "__main__":
    print("'a' value is:", a, "\n'b' value is:", b, "\nThe minimum value is:", findmin(a, b))

# Output:

# Please enter a value: 34
# Please enter b value: 12
# 'a' value is: 34
# 'b' value is: 12
# The maximum value is: 12