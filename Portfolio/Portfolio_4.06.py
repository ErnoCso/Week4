#!/usr/bin/env python 3

# Task 6

# Write a program that reads 6 temperatures (in the same format as before), and
# displays the maximum, minimum, and mean of the values.
# Hint: You should know there are built-in functions for max and min. If you hunt, you
# might also find one for the mean…

from statistics import mean

if __name__ == "__main__":

    TIMES = ['8am', '10am', "12noon", "2pm", "6pm", "8pm"]

    temp = []

    for reading_time in TIMES:

        reading = int(input(f'Enter {reading_time} reading: ')[:-1])
        temp.append(reading)

        max_temp = max(temp)
        min_temp = min(temp)
        avg_temp = mean(temp)

        print(f"Maximum: {max_temp}")
        print(f"Minimum: {min_temp}")
        print(f"Average: {round(avg_temp,2)}")


# Output:

# Enter 8am reading: 21C
# Maximum: 21
# Minimum: 21
# Average: 21
# Enter 10am reading: 26C
# Maximum: 26
# Minimum: 21
# Average: 23.5
# Enter 12noon reading: 30C
# Maximum: 30
# Minimum: 21
# Average: 25.67
# Enter 2pm reading: 32C
# Maximum: 32
# Minimum: 21
# Average: 27.25
# Enter 6pm reading: 24C
# Maximum: 32
# Minimum: 21
# Average: 26.6
# Enter 8pm reading: 20C
# Maximum: 32
# Minimum: 20
# Average: 25.5