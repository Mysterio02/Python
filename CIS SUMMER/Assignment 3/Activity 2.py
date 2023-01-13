# This program displays age in months, days, hours, and seconds.
print("Enter your age:")
age = int(input())
months = 12 * age
days = 365 * age
hours = 24 * days
seconds = 86400 * 365
print("Number of months: " + str(months))
print("Number of days: " + str(days))
print("Number of hours: " + str(hours))
print("Number of seconds: " + str(seconds))
