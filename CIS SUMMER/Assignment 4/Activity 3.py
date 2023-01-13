# This program displays distance in yards, feet, and inches.
miles = int(input("Input distance in miles: "))

yards = miles * 1760
feet = miles * 5280
inches = miles * 63360

print(f"The distance in yards is {yards:.2f}.")
print(f"The distance in feet is {feet:.2f}.")
print(f"The distance in inches is {inches:.2f}.")