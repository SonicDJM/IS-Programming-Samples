"""
File: decimaltoOctal.py
Converts a decimal integer to octal numbers.
"""

decimal = int(input("Enter a decimal integer: "))
print("Quotient Remainder Octal")
ostring = ""

powerofEight = [1, 8, 64, 512, 4096]
for power in powerofEight:
    if decimal > power:
        usedpowermax = int(power)

while decimal > 0:
    remainder = decimal % usedpowermax # 11
    decimal = decimal // usedpowermax  # 2
    ostring = ostring + str(decimal)
    print("%5d%8d%12s" % (remainder, decimal, ostring))
    decimal = remainder
    usedpowermax = usedpowermax // 8
print("The binary representation is", ostring)
