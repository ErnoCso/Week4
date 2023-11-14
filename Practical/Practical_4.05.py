#!/usr/bin/env python 3

# Task 5
#
# def findMax(a,b):
# """Finds the maximum of two values."""
# if ( a > b ):
# 	max = a
# else:
# 	max = b
# return max
# Input the above function definition. Once that is done
# make several calls to the function passing different argument
# values and displaying the returned value.

a = input("Please enter a number: ")
b = input("Please enter another number: ")


def findMax(a, b):
    """Finds the maximum of two values."""
    if (a > b):
        max = a
    else:
        max = b
    return max


if __name__ == "__main__":
    print(f"\n'a' value is: {a}\n'b' value is: {b} \nThe maximum value is: {findMax(a, b)}")

# Please enter a number: 34
# Please enter another number: 13
#
# 'a' value is: 34
# 'b' value is: 13
# The maximum value is: 34
