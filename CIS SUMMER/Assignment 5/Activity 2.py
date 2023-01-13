def calculateDays(age):
    days = 365 * age
    
    return days

def calculateHours(days):
    hours = 24 * days
    
    return hours

def calculateMonths(age):
    months = 12 * age
    
    return months

def calculateSeconds(hours):
    seconds = 86400 * 365
    
    return seconds

def displayResult(months, days, hours, seconds):
    print("Number of months: " + str(months))
    print("Number of days: " + str(days))
    print("Number of hours: " + str(hours))
    print("Number of seconds: " + str(seconds))

def getAge():
    print("Enter your age: ")
    age = int(input())
    
    return age

# Main
# Seperate functions for output, processing, and input
age = getAge()
months = calculateMonths(age)
days = calculateDays(age)
hours = calculateHours(days)
seconds = calculateSeconds(days)
displayResult(months, days, hours, seconds)
