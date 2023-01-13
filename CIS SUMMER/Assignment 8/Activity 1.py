def getNumber():
    print("Enter a number to generate multiplication expressions for:")
    number = int(input())
    
    return number

def getValue():
    print("Enter the number of value to be displayed:")
    value = int(input())
    
    return value

# Main
# This program generates a list of multiplication expressions for a given value.
# 
number = getNumber()
value = getValue()
i = 1
while i <= value:
    print(str(number) + " * " + str(i) + " = " + str(number * i))
    i = i + 1
