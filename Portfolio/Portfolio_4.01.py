#!/usr/bin/env python 3

# Task 1

# Functions are often used to validate input. Write a function that accepts a single
# integer as a parameter and returns True if the integer is in the range 0 to 100
# (inclusive), or False otherwise. Write a short program to test the function.

if __name__ == "__main__":
    def scale(number):
        return 0 <= number <= 100


    input_num = int(input("Enter a number: "))

    if scale(input_num):
        print("The integer is in the range 0 to 100.")
    else:
        print("The integer is not in the range 0 to 100.")

# Output:
#
# Enter a number: 112
# The integer is not in the range 0 to 100.
#
# Enter a number: 14
# The integer is in the range 0 to 100.
