#!/usr/bin/env python 3

# Task 3

# Modify your "greetings" program so that the first letter of the name entered is
# always in uppercase with the rest in lowercase. This should happen even if the user
# entered their name differently. So if the user entered arthur, ARTHUR, or even
# arTHur the name should be displayed as Arthur.

def greetings():
    name = input("Please enter your name: ")
    corrected_name = name.capitalize()
    print(f"Hello, {corrected_name}!")


if __name__ == "__main__":
    greetings()

# Output:

# Please enter your name: MAUricE
# Hello, Maurice!

