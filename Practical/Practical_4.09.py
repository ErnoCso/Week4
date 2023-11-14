#!/usr/bin/env python 3

# Task 9

# The built-in print() function supports a keyword argument called sep.
# This is used to decide what character to display between each of the
# provided positional parameters. Write some code that makes several calls
# to the print() function while setting the sep argument to values other than
# a space (which is the default).


def calcAve(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


if __name__ == "__main__":
    result1 = calcAve(1, 2, 3, 4, 5)
    result2 = calcAve(10, 30, 50, 40, 50, 60)
    result3 = calcAve(2, 4, 6, 8)

    print(result1)
    print(result2)
    print(result3)

# Output:

# 3.0
# 35.0
# 5.0
