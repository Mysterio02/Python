# Separate functions for input, each type of processing, and output.

def get_hours():
    print("Enter the numbers of hours worked this week:")
    hours = float(input())
    return hours


def get_rate():
    print("Enter rate per hour in dollars:")
    rate = float(input())    
    return rate


def calculate_pay(hours, rate):
    if hours > 40:
        pay = 40 * rate + (hours - 40) * rate * 1.5
    else:
        pay = hours * rate
    return pay


def display_results(hours, rate, pay):
    print(str(hours) + " hours worked at $" + str(rate) + 
        " per hour with overtime is $" + str(pay))


def main():
    hours = get_hours()
    rate = get_rate()
    pay = calculate_pay(hours, rate)
    display_results(hours, rate, pay)


main()