# This program asks the user for a distance in miles,
# converts the given miles into yards, feet, inches,
# and displays the results.
#
# Reference:
# https://www.mathsisfun.com/measure/us-standard-length.html

def get_miles():
    print("Enter distance in miles:")
    miles = int(input())
    return miles


def calculate_yards(miles):
    yards = miles * 1760
    return yards


def calculate_feet(miles):
    feet = miles * 5280
    return feet


def calculate_inches(miles):
    inches = miles * 63360
    return inches


def display_result(yards, feet, inches):
    print("Distance in yards is: " + str(yards))
    print("Distance in feet is: " + str(feet))
    print("Distance in inches is: " + str(inches))
    
    
def main():
    miles = get_miles()
    yards = calculate_yards (miles)
    feet = calculate_feet (miles)
    inches = calculate_inches (miles)
    display_result (yards, feet, inches)
    
    
main()