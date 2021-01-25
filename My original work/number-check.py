value = int(input("Type in a number: "))
x = value - 1


while value < 400:
    value = value * 2
    print(value)
    x += 1

print("Done, stopped at", value)
print(x, "Rounds needed to get there")
