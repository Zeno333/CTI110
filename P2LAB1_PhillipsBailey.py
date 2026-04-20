# Bailey Phillips
# 03/05/2026
# P2LAB1
# This program asks the user for the radius of a circle and calculates
# the diameter, circumference, and area using circle formulas.

import math

radius = float(input("What is the radius of the circle? "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print()
print(f"The diameter of the circle is {diameter:.1f}")
print()
print(f"The circumference of the circle is {circumference:.2f}")
print()
print(f"The area of the circle is {area:.3f}")