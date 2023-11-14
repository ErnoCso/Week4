#!/usr/bin/env python 3

# Task 12

# Improve your previous lambda expression so that if only one argument is
# passed within a call, then the number of minutes defaults to 0, as detailed below:
# >>> to_seconds(1)
# 3600
# >>> to_seconds(2)
# 7200

to_seconds = lambda hours, minutes=0: hours * 3600 + minutes * 60


result1 = to_seconds(1)
result2 = to_seconds(2)
result3 = to_seconds(3)

if __name__ == "__main__":
    print(result1)
    print(result2)
    print(result3)
# Output:

# 3600
# 7200
# 10800