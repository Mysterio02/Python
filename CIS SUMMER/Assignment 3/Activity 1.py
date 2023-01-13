# This program displays weekly, monthly, and annual gross pay.
print("Enter number of hours worked:")
hours = int(input())
print("Enter rate per hour:")
rate = int(input())
weekly = hours * rate
monthly = 4 * weekly
annually = 52 * weekly
print("weekly: " + str(weekly))
print("monthly: " + str(monthly))
print("Annual gross pay: " + str(annually))
