#!/usr/bin/env python 3

# Task 6
#
# Define a function that takes two numeric values, multiplies them together
# then returns the result. If the function is called with only a single argument
# however, then the value should be multiplied by itself. Once the function is defined,
# call it several times and display the returned values for testing purposes.

def main():
    ans = ["Y", "y", "yes", "Yes", "YES", "Yeah" "YEAH", "yeah"]
    x_value = input("Please enter x value: ")
    y_value = input("Please enter y value: ")

    if x_value == "" or y_value == "":
        if x_value == "":
            x = int(y_value)
            y = int(y_value)
        else:
            x = int(x_value)
            y = int(x_value)
    else:
        x = int(x_value)
        y = int(y_value)

    def displayFunction(x, y):
        """Prints the product of x and y."""

        print(x * y)

    if __name__ == "__main__":

        displayFunction(x, y)

        answer = input("Would you like to run again? Y/N ")
        if answer in ans:
            main()

        else:
            exit()


main()


# Please enter x value: 4
# Please enter y value:
# 16
# Would you like to run again? Y/N y
# Please enter x value: 6
# Please enter y value: 5
# 30
# Would you like to run again? Y/N y
# Please enter x value:
# Please enter y value: 8
# 64
# Would you like to run again? Y/N n
#
# Process finished with exit code 0
