# This program uses for loop to generate a list of multiplication
# expressions for a given value.


def get_number():
    print("Enter a number to generate multiplication expressions for:")
    number = int(input())
    return number


def get_value():
    print("Enter the number of value to be displayed:")
    value = int(input())
    return value


def for_loop(number, value):  # No need to pass i as it is being declared inside the function.
    i = 1
    print("For Loop multiplying " + str(number) + " times by " + str(value) + ":")
    for i in range(1, value + 1, 1):
        print(str(number) + " * " + str(i) + " = " + str(number * i))
        
        
def main():
    number = get_number()
    value = get_value()
    for_loop(number, value)
    
    
main()
