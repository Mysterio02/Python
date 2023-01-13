# This program displays the array contents and then calculate
# and display the high, low, and average score
# Reference:
# https://stackoverflow.com/questions/9578580/skip-first-couple-of-lines-while-reading-lines-in-python-file


import os


def read_file(filename):
    score = []
    count = 0
    file = open(filename, "r")
    for _ in range(1):
        next(file)
    for line in file:
        line = line.strip()
    #   print(line)
        index = line.find(",")
        if index < 0:
            number = 0
        else:
            number = int(line[index + 1:])
            score.append(number)  # To include entered scores in array.
            count = count + 1
    print(score)
    display_results(score, count)
    file.close()
    print("")


def high(score, number):
    score.sort(reverse=True)
    maximum = score[0]
    return maximum


def low(score, number):
    score.sort()
    minimum = score[0]
    return minimum


def average(score, number):
    total = sum(score)
    average = total / number
    return average


def display_results(score, number):
    print("Highest score:" + str(high(score, number)))
    print("Lowest score:" + str(low(score, number)))
    avg = average(score, number)
    print(f"Average of your scores is {avg:.2f}")


def main():
    filename = "scores.txt"

    if os.path.isfile(filename):
        #  print("File exists.")
        read_file(filename)
    else:
        print("File does not exist")


main()