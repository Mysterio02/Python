def get_name():
    while True:
        print("Enter name (last, first):")
        name = input()
        index = name.find(",")
        if index >= 0:
            break
    return name

def get_last(name):
    index = name.find(",")
    if index < 0:
        last = ""
    else:
        last = name[0:index]
    return last

def get_first(name):
    index = name.find(",")
    if index < 0:
        first = ""
    else:
        first = name[index + 1:]
        first = first.strip()
    return first

def display_name(first, last):
    print(f"Hello {first} {last}!")

def main():
    name = get_name()
    last = get_last(name)
    first = get_first(name)
    display_name(first, last)
    
main()