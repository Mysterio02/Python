# This program displays each address as a single line of comma-separated values.


import os


def read_file(filename):
    address = []
    file = open(filename, "r")
    for line in file:
        line = line.strip()
    #   print(line)
        address.append(line)
    #   print(address)
    for index in range(0, len(address), 4):
        if (address[index] != '' and address[index+1] != ''
        and address[index+2] != ''):
            print(f"{address[index]}, {address[index+1]}, {address[index+2]}\n")
        else:
            print("")
    file.close()


def main():
    filename = "directory.txt"

    if os.path.isfile(filename):
        #   print("File exists.")
        read_file(filename)
    else:
        print("File does not exist")


main()