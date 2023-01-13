# This program asks the user for first and last name,
# and prints out the name in the form lastname, first initial.


def get_name():
    while True:
        print("Enter name (Firstname Lastname):")
        name = input()
        count = name.count(' ')
        index = name.find(" ")
        if index >= 0 and count != 0:  # Checks if the user is entering 2 values as first & last name.
            break
        if count == 0:
            print("Error: Incorrect input")
            return "Error"
    return name


def get_last(name):
    index = name.rfind(" ")
    if index < 0:
        last = ""
    else:
        last = name[index + 1:]  # Prints after the space after firstname.
        last = last.strip()
    return last


def get_first(name):
    index = name.find(" ")
    if index < 0:
        first = ""
    else:
        first = name[0:1]  # To display the firstname initial.
    return first


def display_name(first, last):
        print(f"{last} {first}.")


def main():
    name = get_name()
    if name != "Error":
        
        last = get_last(name)
        first = get_first(name)
        display_name(first, last)
    

main()

