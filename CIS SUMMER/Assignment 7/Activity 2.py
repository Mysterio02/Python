# This program asks the user how old they are
# asks the user if they would like to know their age in  months, days, hours, or seconds
# and displays the result.


def calculate_months(age):
    months = 12 * age
    return months


def calculate_days(age):
    days = 365 * age
    return days


def calculate_hours(age):
    hours = 365 * 24 * age 
    return hours


def calculate_seconds(age):
    seconds = 365 * 24 * 60 * 60 * age
    return seconds


def display_result(label, value):
    print(f"Your age in {label} is: {value}")
    return value


def get_age():
    print("Enter your age:")
    age = int(input())
    return age


def get_choice():
    print("To convert your age into months enter M. " +
          "To convert your age into days enter D. " +
          "To convert your age into hours enter H. " +
          "To convert your age into seconds enter S. ")
    choice = input()
    return choice


def main():
    age = get_age()
    choice = get_choice()
    if choice == "M" or choice == "m":
       months = calculate_months(age)
       display_result("months", months)
    elif choice == "D" or choice == "d":
        days = calculate_days(age)
        display_result("days", days)
    elif choice == "H" or choice == "h":
        hours = calculate_hours(age)
        display_result("hours", hours)
    elif choice == "S" or choice == "s":
        seconds = calculate_seconds(age)
        display_result("seconds", seconds)
    else:
        print("You must enter M, D, H, or S.")


main()