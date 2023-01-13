# This program uses do while loop to ask the user for grade scores and displays the average.
# Value is assigned -1 to fulfill the requirement of question.


def get_scores():
    print("Enter your grade scores: ")
    scores = int(input())
    return scores


def calculate_average(): # No need to pass i, a, or total as parameters as they are being declared inside the function.
    i = -1
    a = 0
    total = 0
    while True:    #This simulates a Do Loop
        total = total + a
        i = i + 1
        a = get_scores()
        if not(a > 0): break   #Exit loop
    average(total, i)
    
    
def average(total, i):
    total = float(total) / i
    display_result(total)


def display_result(average):
    print("Average of your scores is:" + str(average))
    
    
def main():
    calculate_average()
    
    
main()
    


