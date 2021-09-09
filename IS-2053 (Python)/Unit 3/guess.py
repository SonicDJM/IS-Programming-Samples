# Modify the code below:
import random


lower_bound = int(input("Enter the smaller number: "))
upper_bound = int(input("Enter the larger number: "))
round = 0
while True:
    round += 1
    print('\n', str(lower_bound), str(upper_bound))
    myguess = int((lower_bound + upper_bound) / 2)
    print(f'Your number is {myguess}')
    response = input("Enter =, <, or >: ")
    if (myguess == lower_bound + 1 and response == '<') or (myguess == upper_bound -1 and response == '>'):
        if response == '=':
            print(f"Hooray, I've got it in {round} tries!")
            break
        else:
            print("I'm out of guesses, and you cheated")
            break
    else:
        if response == '<':
            upper_bound = myguess
        elif response == '>':
            lower_bound = myguess
        elif response == '=':
            print(f"Hooray, I've got it in {round} tries!")
            break
        else:
            print("Invalid Input")
