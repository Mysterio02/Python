# This program asks the user to enter grade scores,
# calculates and displays the high, low, and average
# for the entered scores.
# Reference:
# https://www.mathsisfun.com/definitions/average.html


def get_number():
    print("How many scores would you like to enter?")
    number = int(input())
    return number


def get_scores(number):
    score = [None] * number
    for i in range(number):
        value = int(input('Enter score: '))
        score[i] = value  # To include entered scores in array.
    return score


def high(score, number):
    maximum = score[0]
    for i in range(1, number):
        if maximum < score[i]:
           maximum = score[i]
    return maximum


def low(score, number):
    minimum = score[0]
    for i in range(1, number):
        if minimum > score[i]:
           minimum = score[i]
    return minimum


def average(score, number):
    total = sum(score) 
    average = total / number
    return average


def display_results(score, number):
    print("Highest score:" + str(high(score, number)))
    print("Lowest score:" + str(low(score, number)))
    print("Average of your scores is:" + str(average(score, number)))


def main():
    number = get_number()
    score = get_scores(number)
    display_results(score, number)


main()