#!/usr/bin/env python 3

# Task 7

# Modify the previous program so that it can process any number of values. The input
# terminates when the user just pressed "Enter" at the prompt rather than entering a
# value.


from statistics import mean

if __name__ == "__main__":

    TIMES = ['8am', '10am', "12noon", "2pm", "6pm", "8pm"]
    temp = []

    while True:
        reading_input = input(f"Please enter temperature reading with Celsius"
                              f" (or press Enter to finish): ")

        if not reading_input:
            break
        try:
            reading = int(reading_input[:-1])
            temp.append(reading)
        except ValueError:
            print("Invalid data, please enter valid temperature.")
    if temp:
        max_temp = max(temp)
        min_temp = min(temp)
        avg_temp = mean(temp)

        print(f"Maximum: {max_temp}")
        print(f"Minimum: {min_temp}")
        print(f"Average: {round(avg_temp,2)}")
    else:
        print("No temperature readings entered.")


# Output:

# Please enter temperature reading with Celsius
# (or press Enter to finish): 23C
# Please enter temperature reading with Celsius
# (or press Enter to finish): 32C
# Please enter temperature reading with Celsius
# (or press Enter to finish): 42C
# Please enter temperature reading with Celsius
# (or press Enter to finish): 44C
# Please enter temperature reading with Celsius
# (or press Enter to finish):
# Maximum: 44
# Minimum: 23
# Average: 35.25