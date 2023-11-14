#!/usr/bin/env python 3

# Task 11

# Write a lambda expression that takes two formal parameters, hours and minutes.
# The expression should calculate and return the total number of equivalent seconds.
# Assign the expression to a variable called to_seconds, then call the function
# several times for testing.
# Given the sample input shown below, your solution should display the same results -
# >>> to_seconds(0,2)
# 120
# >>> to_seconds(2,0)
# 7200
# >>> to_seconds(1,30)
# 5400

to_sec = lambda hours, minutes: hours * 3600 + minutes * 60

result1 = to_sec(0, 2)
result2 = to_sec(2, 0)
result3 = to_sec(1, 30)


if __name__ == "__main__":
    print(result1)
    print(result2)
    print(result3)

# Output:

# 120
# 7200
# 5400