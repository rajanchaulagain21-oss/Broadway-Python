#area of circle
import math

radius = float(input("Enter radius of a circle (in cm): "))
area =  math.pi * pow(radius, 2)
print(f"The area of your circle is {area:.2f} cm²")