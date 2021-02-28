# Setup and input
import math
perimInital = float(input("Please type in the perimeter: "))
placeHold = 0

# To prevent negative integers from being used
if perimInital < 0:
    print("Sorry, you can only use positive numbers in this program")
    quit()

# This math is used for finding area of a square
placeHold = perimInital / 4
areaSquare = placeHold ** 2
areaSquare = round(areaSquare, 2)
print("A square with that perimeter would have an area of", areaSquare)

# This math is for finding the area of a cricle
placeHold = perimInital / (2 * math.pi)  # finding radius
areaCircle = math.pi * placeHold ** 2
areaCircle = round(areaCircle, 2)
print("A circle with that perimeter would have an area of", areaCircle)

# This math finds the area of Equalateral Triangle
placeHold = perimInital / 3
areaTriangle = (math.sqrt(3) / 4) * (placeHold ** 2)
areaTriangle = round(areaTriangle, 2)
print("A triangle with that perimeter would have an area of", areaTriangle)