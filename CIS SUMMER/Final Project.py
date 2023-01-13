# This program reads the data from a file, build arrays and
# displays the menu items for breakfast.


import os


def read_file(filename):
    menu = []
    name = []
    description = []
    calories = []
    price = []
    file = open(filename, "r")
    for line in file:
        line = line.strip()
   #     print(line)
        menu.append(line)
    print(menu)
    for index in range(0, len(menu)):
        if (menu[index] == '<food>'):
            name = menu[index+1]
        else:
            name = 'a'
    print(name)
    #    start = menu.find("<name>")
     #   end = menu.find("</name>")
      #  if start < 0:
       #     name = ""
        #else:
         #   name = line[start:end]
        #    return name
   # print(name)
    file.close()


def main():
    filename = "breakfast.xml"

    if os.path.isfile(filename):
        #   print("File exists.")
        read_file(filename)
    else:
        print("File does not exist")


main()