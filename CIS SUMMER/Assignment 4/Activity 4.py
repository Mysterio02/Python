# This program displays the area of shapes.
PI = 3.14
side = int(input("Enter the value of sideof square: "))
square = (side * side)
    
radius = int(input("Enter the value of radius of circle: "))
circle = (2 * PI * radius)
    
length = int(input("Enter the value of length of rectangle: "))
width = int(input("Enter the value of width of rectangle: "))
rectangle = (length * width)
    
base = int(input("Enter the value of base triangle: "))
height = int(input("Enter the value of height triangle: "))
triangle = (0.5 * base * height)
    
base = int(input("Enter the value of base of trapezoid: "))
a = int(input("Enter the value of base (a): ")) 
height = int(input("Enter the value of height of trapezoid: "))
trapezoid = 0.5 * (a + base) * height
    
base = int(input("Enter the value of base of ellipse: "))
a = int(input("Enter the value of base (a): "))
ellipse = (PI * a * base)
    
base = int(input("Enter the value of base of parallelogram: "))
height = int(input("Enter the value of height of parallelogram: "))
parallelogram = (base * height)
    
radius = float(input("Enter the radius of circle: "))
angle = float(input("Enter the measure of angle: "))
sector = (PI * radius ** 2) * (angle/360)
    
print (f"area of square is {square:.2f}.")
print (f"area of circle is {circle:.2f}.")
print (f"area of rectangle is {rectangle:.2f}.")
print (f"area of triangle is {triangle:.2f}.")
print (f"area of trapezoid is {trapezoid:.2f}.")
print (f"area of ellipse is {ellipse:.2f}.")
print (f"area of parallelogram is {parallelogram:.2f}.")
print (f"area of sector is {sector:.2f}.")
