# Put code here
import math
# input value
radius = float(input("Radius = "))
# the calculations
diameter = 2 * radius
circumference = diameter * math.pi
surfaceArea = 4 * math.pi * radius ** 2
volume = 4 / 3 * math.pi * radius ** 3
# the results
print("Diameter : ", diameter)
print("Circumference : ", circumference)
print("Surface area : ", surfaceArea)
print("Volume : ", volume)
