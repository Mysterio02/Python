# This program uses nested loops to
# generate a multiplication table.
# Reference:
# https://www.mathsisfun.com/tables.html


def get_input(prompt):
    print(prompt)
    value = int(input())
    return value
    
    
def display_table(start, end):
    
    for i in range(start, end + 1):  
        print("\t" + str(i), end=" ") 
    print()
    
    for i in range(start, end + 1):  
        print(str(i), end="")

        for j in range(start, end + 1):  
            multiply_number = i * j
            print("\t" + str(multiply_number), end="")  
        print()
    
    
def main():
    start = get_input("Enter the starting value:")
    end = get_input("Enter the ending value:")
    display_table(start, end)
    
    
main()