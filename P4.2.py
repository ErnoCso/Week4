def upperLower(string):
    upper = 0
    lower = 0

    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return upper, lower

input_str = str(input("Please type something in with lower and upper case: "))
upper, lower = upperLower(input_str)

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)