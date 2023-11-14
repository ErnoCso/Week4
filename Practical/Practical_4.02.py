#!/usr/bin/env python 3

# Task 2

# Write some code that imports only the log2() function from the math module,
# then call this function to calculate the log base 2 value of 1024.
# Print the result to the screen.

from math import log2

if __name__ == "__main__":
    x = 1024
    print(f"The base 2 logarithm of {x} is {log2(x)}")


# Output:

# The base 2 logarithm of 1024 is 10.0