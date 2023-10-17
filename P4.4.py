def removeLastChar(stringParam):
    if len(stringParam) <= 1:
        return stringParam
    else:
        return stringParam[:-1]

stringParam = input("Enter a string: ")
result = removeLastChar(stringParam)
print("Modified string:", result)