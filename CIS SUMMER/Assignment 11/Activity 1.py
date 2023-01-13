# This program asks the user for a year,
# calculates and displays whether or not the given year is a leap year.
# Reference:
# https://www.mathsisfun.com/leap-years.html


def get_year():
    print("Enter year:")
    year = int(input())
    return year


def get_month(checkLeap):
    while True:
        print("Enter the month number:")
        month = int(input())
        if (month > 0 and month <= 12):
            display_month(month, checkLeap)
        if not(month > 0 and month <= 12):
            break
    return month


def check_leap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def display_month(month, checkLeap):
    month = month - 1
    months = ["January", "February", "March", "April", "May",
              "June", "July", "August", "September", "October",
              "November", "December"]
    number = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
    if (checkLeap == "Leap" and months[month] == "February"):
        print(months[month]+" = " + str(number[month]+1))  # If leap year February is calculated as 28 + 1
    else:
        print(months[month]+" = " + str(number[month]))


def display_results(year):
    if(check_leap(year)):
        print("Leap Year")
        return "Leap"  # Stores in checkLeap.
    else:
        print("Not a Leap Year")
        return "Noleap"


def main():
    year = get_year()
    checkLeap = display_results(year)
    get_month(checkLeap)


main()