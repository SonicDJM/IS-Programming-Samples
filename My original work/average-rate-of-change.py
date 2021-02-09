# Input
newYvalue = int(input("Type in Fb: "))
oldYvalue = int(input("Type in Fa: "))
newXvalue = int(input("Type in b: "))
oldXvalue = int(input("Type in a: "))

# Math
totalY = newYvalue - oldYvalue
totalX = newXvalue - oldXvalue
value = float(totalY) / float(totalX)
value = round(value, 3)
value = value * 1000000

# Result
print("The answer for this question is", value)