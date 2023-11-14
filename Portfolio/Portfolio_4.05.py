# # !/usr/bin/env python 3

# Task 5

# Write and test a function that converts a temperature measured in degrees
# centigrade into the equivalent in Fahrenheit, and another that does the
# conversion. Test both functions. (Google will find you the formulae).

if __name__ == "__main__":
    def converter():
        list_y = ["yes", "YES", "Yes", "Y", "y", "Yeah", "YEAH", "yeah", "yep", "Yep", "YEP"]
        list_n = ["no", "NO", "No", "N", "n", "Nope", "NOPE", "nope"]

        try:
            choice = int(input("\nPlease choose 1 or 2:\n1. Centigrade to Fahrenheit or \n2. Fahrenheit to Centigrade! "))
        except ValueError:
            print("Only numbers 1 or 2 are acceptable, please try again!")
            converter()

        def yesno():
            question = input("\nDo you want to run the converter again? Y/N")
            if question in list_y:
                converter()
            if question in list_n:
                exit()
            else:
                print("Invalid data, try again!")
                yesno()

        if choice == 1:
            def value1():
                try:
                    value = float(input("Please enter the Centigrade you want to convert:  "))

                    fahrenheit = (value * 1.8) + 32
                    print(f"{value} C is equivalent to {fahrenheit} F.")

                except:
                    print('That is not a number!')
                    value1()

            value1()
            yesno()

        if choice == 2:

            def value2():
                try:
                    value = float(input("\nPlease enter the Fahrenheit you want to convert: "))
                    if choice == 1:
                        def val1():
                            try:
                                val = float(input("Please enter the centigrade you want to convert:  "))
                                fahrenheit = (val * 1.8) + 32
                                print(f"{val} C is equivalent to {fahrenheit} F.")

                            except:
                                print('That is not a number!')
                                val1()

                        val1()
                        yesno()
                    celsius = (value - 32) / 1.8000
                    print(f"{value} F is equivalent to {round(celsius,2)} C.")

                except:
                    print('That is not a number!')
                    value2()

            value2()
            yesno()

        else:
            print("Invalid data, please enter 1 or 2.")
            converter()


    converter()

# Output:

# Please choose 1 or 2:
# 1. Centigrade to Fahrenheit or
# 2. Fahrenheit to Centigrade! 4
# Invalid data, please enter 1 or 2.
#
# Please choose 1 or 2:
# 1. Centigrade to Fahrenheit or
# 2. Fahrenheit to Centigrade! 1
# Please enter the centigrade you want to convert:  37.1
# 37.1 C is equivalent to 98.78 F.
#
# Do you want to run the converter again? Y/Ny
#
# Please choose 1 or 2:
# 1. Centigrade to Fahrenheit or
# 2. Fahrenheit to Centigrade! 2
#
# Please enter the Fahrenheit you want to convert: 100
# 100.0 F is equivalent to 37.78 C.
#
# Do you want to run the converter again? Y/Nn