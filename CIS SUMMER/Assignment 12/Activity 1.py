# This program asks the user to enter grade scores,
# calculates and displays the high, low, and average
# for the entered scores until the user enters a
# negtive value for the score.
# Value is assigned -1 to fulfill the requirement of question.


def get_scores():
    score = []
    count = 0
    while True:
        value = int(input('Enter score: '))
        if (value > 0):
            score.append(value)  # To include entered scores in array.
            count = count + 1
        if not(value > 0):
            break
    display_results(score, count)


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


def avg(score, number):
    average = score[0]
    for i in range(1, number):
        average = average + score[i]
    average = average / number
    return average


def display_results(score, number):
    print("Highest score:" + str(high(score, number)))
    print("Lowest score:" + str(low(score, number)))
    print("Average of your scores is:" + str(avg(score, number)))


def main():
    get_scores()


main()