#!/usr/bin/env python 3

# Task 7
#
# someFunc(y=2, z=3, x=1)
#
# x is 1
# y is 2
# z is 3
# Enter the example function shown above, then try calling it using
# the keyword arguments in several different orders.

def someFunc(x, y, z):
    print("x is", x, "\ny is", y, "\nz is", z)

    
if __name__ == "__main__":
    print()
    someFunc(y=2, z=3, x=1)
    print()
    someFunc(z=3, x=1, y=2)
    print()
    someFunc(y=2, x=1, z=3)


# Output:
#
# x is 1
# y is 2
# z is 3
#
# x is 1
# y is 2
# z is 3
#
# x is 1
# y is 2
# z is 3
#
# Process finished with exit code 0