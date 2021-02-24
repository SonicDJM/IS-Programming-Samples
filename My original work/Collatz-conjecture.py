# Program for IS Assignment 2

# Input
inputInt = int(input("Please type in a positive integer: "))
steps = 0
ruleOne = 1
ruleTwo = 2
oneCount = 0
twoCount = 0

# Math
while inputInt > 1:
    steps += 1
    if (inputInt % 2) == 0:
        inputInt = inputInt / 2
        twoCount += 1
        print("Step", steps, "(rule", ruleTwo, ") gives", int(inputInt))
    else:
        inputInt = (inputInt * 3) + 1
        oneCount += 1
        print("Step", steps, "(rule", ruleOne, ") gives", int(inputInt))
    

# Results
print("It took", steps, "steps (", oneCount, "for rule 1, and", twoCount, "for rule 2)")