# This program reads the data from a file, build arrays and
# displays the menu items for breakfast along with the total number
# of items on the menu, the average number of calories per item,
# and the average price per item.
# References:
# https://www.youtube.com/watch?v=r6dyk68gymk
# https://stackoverflow.com/questions/17747330/correct-way-to-check-for-empty-or-missing-file-in-python


import xml.etree.ElementTree as ET
import os


def parse_file(mytree, tag):
    myroot = mytree.getroot()
    text = []
    for x in myroot.findall('food'):
        try:
            if (x.find(tag).text) == None:
                text.append("Missing data here")
            elif tag == "calories":
                item = int(x.find(tag).text)
                text.append(item)
            elif tag == "price":
                item = x.find(tag).text
                index = item.find("")
                if index < 0:
                    item = 0
                else:
                    item = float(item[1:index+5])
                text.append(item)
            else:
                item = x.find(tag).text
                text.append(item)
        except:
          #  print("Bad data")
            text.append("Bad data")

    return text


def error_handling(tag):
    for index in range(0, len(tag)):
        if tag[index] == "Bad data":
          #  print("Bad data")
            tag[index]=0
        elif tag[index] == "Missing data here":
            tag[index] = 0

    return tag


def average_calories(calories):
    total_cal = sum(calories)
    average_cal = total_cal / len(calories)

    return average_cal


def average_price(price):
    total_pr = sum(price)
    average_price = total_pr / len(price)

    return average_price


def display_result(name, description, calories, price):
    #   print("name - description - calories - price")

    for i in range(0, len(name)):
        print(name[i]+" - " + description[i]+" - " +
              str(calories[i])+" - $" + str(price[i]))


def display_results(name, average_cal, average_pr):
    print("\n" + str(len(name))+" items - " +
          f"{average_cal:.0f} average calories ${average_pr:.2f} average price")


def main():
    filename = "breakfast.xml"

    try:
        if os.stat(filename).st_size > 0:
            mytree = ET.parse(filename)
            tag = "name"
            name = parse_file(mytree, tag)
            tag = "description"
            description = parse_file(mytree, tag)
            tag = "calories"
            calories = parse_file(mytree, tag)
            calories = error_handling(calories)
            tag = "price"
            price = parse_file(mytree, tag)
            price = error_handling(price)
            display_result(name, description, calories, price)
            average_cal = average_calories(calories)
            average_pr = average_price(price)
            display_results(name, average_cal, average_pr)

        else:
            print ("Empty file")
    except OSError:
        print ("File does not exist")

main()