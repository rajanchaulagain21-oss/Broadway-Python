#hypotenus of a right triangle
import math

perpendicular = float(input("Enter the perpendicular/height of a triangle(in cm): "))
base = float(input("Enter the length/base of a triangle(in cm): "))
hypotenus = math.sqrt((pow(perpendicular, 2) + pow(base, 2)))
print(f"The hypotenus of a triangle is {hypotenus:.2f} cm")