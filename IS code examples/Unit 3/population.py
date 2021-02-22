# Put your code here
initalNum = int(input("Enter the inital number of organisms: "))
rateOFgrowth = float(input("Enter the rate of growth  [a real number > 1]: "))
numHours = int(input("Enter the number of hours to achieve the rate of growth: "))
totalHours = int(input("Enter the total hours of growth: "))

# math
while totalHours > 0:
    totalHours -= numHours
    initalNum = initalNum * rateOFgrowth
#   print(initalNum, "\n") # DEBUG
    
if totalHours < 0: # improvments could be made
    initalNum = initalNum / rateOFgrowth
# result
print("The total population is", int(initalNum))
