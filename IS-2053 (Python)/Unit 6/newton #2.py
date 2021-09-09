# Modify the code below
"""
Program: newton.py
Author: Ken
Compute the square root of a number.
1. The input is a number.
2. The outputs are the program's estimate of the square root
   using Newton's method of successive approximations, and
   Python's own estimate using math.sqrt.
"""

import math

# Receive the input number from the user
x = 0

# Initialize the tolerance and estimate
tolerance = 0.000001
estimate = 1.0
totalSum = 0

# Perform the successive approximations
def newton(x):
    global estimate
    global totalSum
    estimate = (estimate + x / estimate) / 2
    while True:
        difference = abs(x - estimate ** 2)
        result = limitReached(difference, tolerance)
        if result == True:
            break
        elif result == False:
            estimate = improveEstimate(x, estimate)
    totalSum = estimate
    return totalSum

def limitReached(difference, tolerance):
    if difference <= tolerance:
        result = True
    else:
        result = False
    return result

def improveEstimate(x, estimate):
    estimate = (estimate + x / estimate) / 2
    return estimate

def main():
    while True:
        x = (input("Enter a positive number or enter/return to quit: "))
        if x == "":
            break
        x = float(x)
        # Output the result
        print("The program's estimate is", newton(x))
        print("Python's estimate is     ", math.sqrt(x))

if __name__ == "__main__":
    main()
