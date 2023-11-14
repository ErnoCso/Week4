# !/usr/bin/env python 3
#
# Task 2

# Write a function that has a single string as its parameter, and returns the number of
# uppercase letters, and the number of lowercase letters in the string. Test the
# function with a short program.

if __name__ == "__main__":
    def upper_lower(string):

        uppercase = 0
        lowercase = 0

        for char in string:
            if char.isupper():
                uppercase += 1
            elif char.islower():
                lowercase += 1
        return uppercase, lowercase

    input_str = str(input("Please type something in with lower and upper case: "))
    upper, lower = upper_lower(input_str)

    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

    # Output:

    # Please type something in with lower and upper case: Leeds Beckett University
    # Uppercase letters: 3
    # Lowercase letters: 19