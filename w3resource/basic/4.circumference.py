"""
task: compute the area of a circle after the user inputs the radius
"""
from math import pi

radius = float(input("Enter Radius: "))

print("Area: {}".format(round(pi*radius**2, 2)))
