# Input
smallNum = int(input("Enter the smaller number: "))
largeNum = int(input("Enter the larger number "))

# Math
while smallNum > 0:
    remainderNum = float(largeNum) % float(smallNum)
    largeNum = smallNum
    smallNum = remainderNum

# Result
print("The greatest common divisor is:", int(largeNum))
