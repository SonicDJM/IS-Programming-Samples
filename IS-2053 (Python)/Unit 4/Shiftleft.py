inputValue = str(input("Enter a string of bits: "))

shiftValue = inputValue[1::] + inputValue[0]

print(shiftValue)
