inputValue = str(input("Enter a string of bits: "))

shiftValue = inputValue[-1] + inputValue[:len(inputValue) - 1:]

print(shiftValue)
