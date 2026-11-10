square = lambda a: a * a
rectangle = lambda l, b: l * b
triangle = lambda b, h: 0.5 * b * h

a = float(input("Enter the side of square: "))
l = float(input("Enter the length of rectangle: "))
b = float(input("Enter the breadth of rectangle: "))
base = float(input("Enter the base of triangle: "))
h = float(input("Enter the height of triangle: "))

print("Area of square:", square(a))
print("Area of rectangle:", rectangle(l, b))
print("Area of triangle:", triangle(base, h))

