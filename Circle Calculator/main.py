import math
radius = input("Enter the radius of the circle: ")

while radius.isdigit() != True:
    print("Please enter a valid number")
    radius = input("Enter the radius of the circle: ")

area = math.pi * (float(radius) ** 2)
circumference = 2 * math.pi * float(radius)
print(f"Area: {area}")
print(f"Circumference: {circumference}")


