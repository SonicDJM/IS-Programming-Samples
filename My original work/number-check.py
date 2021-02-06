value = int(input("Type in the goal number: "))
x = 1
doubleValue = 0
singleValue = 0


while x < value:
    x = x * 2
    doubleValue += 1


if x == value:
    print("Done, you just have to double", doubleValue, "times")
elif x > value:
    x = x / 2
    doubleValue -= 1

    while x < value:
     x = x + 1
     singleValue += 1
     print("Done, you have to double", doubleValue, "and add one", singleValue, "times")
