# This program asks the user for the dimensions of different shapes,
# and displays the area of shapes.
#
# Reference:
# https://www.mathsisfun.com/area.html

PI = 3.14


def calculate_square():
    print("Enter the value of side of square:")
    side = int(input())
    square = side ** 2
    return square


def calculate_circle(PI):
    print("Enter the value of radius of circle:")
    radius = int(input())
    circle = radius ** 2 * PI
    return circle


def calculate_rectangle():
    print("Enter value of length of rectangle:")
    length = int(input())
    print("Enter value of width of rectangle:")
    width = int(input())
    rectangle = length * width
    return rectangle


def calculate_triangle():
    print("Enter the value of base of triangle:")
    base = int(input())
    print("Enter the value of height of triangle:")
    height = int(input())
    triangle = 0.5 * base * height
    return triangle


def calculate_trapezoid():
    print("Enter the value of base of trapezoid:")
    base = int(input())
    print("Enter the value of trapezoid base (a):")
    a = int(input())
    print("Enter the value of height of trapezoid:")
    height = int(input())
    trapezoid = 0.5 * (a + base) * height
    return trapezoid


def calculate_ellipse(PI):
    print("Enter the value of base of ellipse:")
    base = int(input())
    print("Enter the value of ellipse (a):")
    a = int(input())
    ellipse = PI * a * base
    return ellipse


def calculate_parallelogram():
    print("Enter the value of base of parallelogram:")
    base = int(input())
    print("Enter the value of height of parallelogram:")
    height = int(input())
    parallelogram = base * height
    return parallelogram


def calculate_sector(PI):
    print("Enter the radius of circle:")
    radius = float(input())
    print("Enter the measure of the sector angle:")
    angle = float(input())
    sector = 0.5 * radius ** 2 * ((angle*PI)/180)
    return sector


def display_results(square, circle, rectangle, triangle, trapezoid,
                    ellipse, parallelogram, sector):
    print(f"area of square is {square:.2f}.")
    print(f"area of circle is {circle:.2f}.")
    print(f"area of rectangle is {rectangle:.2f}.")
    print(f"area of triangle is {triangle:.2f}.")
    print(f"area of trapezoid is {trapezoid:.2f}.")
    print(f"area of ellipse is {ellipse:.2f}.")
    print(f"area of parallelogram is {parallelogram:.2f}.")
    print(f"area of sector is {sector:.2f}.")


def main():
    square = calculate_square()
    circle = calculate_circle(PI)
    rectangle = calculate_rectangle()
    triangle = calculate_triangle()
    trapezoid = calculate_trapezoid()
    ellipse = calculate_ellipse(PI)
    parallelogram = calculate_parallelogram()
    sector = calculate_sector(PI)
    display_results(square, circle, rectangle, triangle, trapezoid,
                    ellipse, parallelogram, sector)


main()





