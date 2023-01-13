# This program asks the user to enter grade scores
# Calculate and display the average for the entered scores.
#
# Reference:
# https://www.mathsisfun.com/definitions/average.html


def get_number():
    print("How many scores would you like to enter?")
    number = int(input())
    return number
    

def calculate_total(number):
    i = 1    # Score count
    scores = 0
    while i <= number:
        print("Enter your score " + str(i) + ":")
        a = int(input())   # To store the value of scores.
        scores = a + scores
        i = i + 1

    scores = scores / number
    return scores


def display_results(scores):
    print("Average of your scores is:" + str(scores))


def main():
    number = get_number()
    scores = calculate_total(number)
    display_results(scores)
    
    
main()