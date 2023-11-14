#!/usr/bin/env python 3

# Task 10

# hypot = lambda a,b : math.sqrt(a * a + b * b)
# Since this expression was assigned to the hypot variable it can now be
# called using that identifier, in the same way as a regular function:
# >>> hypot(3,4)
# 5.0
# Enter the example lambda expression shown above, then find out
# the data type of the hypot variable using a call to the type() function.
# Notice the result.


import math

if __name__ != "__main__":
    pass
else:
    hypot = lambda a, b: math.sqrt(a * a + b * b)

    result = hypot(12, 8)
    print(round(result,2))

    type_of_hypot = type(hypot)
    print(type_of_hypot)

# Output:

# 14.42
# <class 'function'>
