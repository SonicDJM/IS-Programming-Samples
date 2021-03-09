"""
File: octaltodecimal.py
Converts octal numbers to a decimal integer.
"""

ostring = input("Enter a string of octal digits: ")
decimal = 0
totalDec = 0
exponent = len(ostring) - 1
for digit in ostring:
    decimal = (8 ** exponent) * int(digit)
    totalDec += decimal
    exponent = exponent - 1
print("The integer value is", totalDec)
