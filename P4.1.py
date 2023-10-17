def range(number):
    return 0 <= number <= 100

input_num = int(input("Enter a number: "))

if range(input_num):
    print("The integer is in the range 0 to 100.")
else:
    print("The integer is not in the range 0 to 100.")