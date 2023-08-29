# Program purpose to find the largest value not in the array.

def solution(A):
# Implement your solution here
    array = A
    array.sort()
    MaxNum = max(array)
    NoInt = 1
    FinalNum = 0
    LoopStat = True

    while LoopStat == True:
        
        if NoInt == len(array):
            FinalNum = max(array) + 1
            LoopStat = False
        
        elif MaxNum > 0:
            MaxNum -= 1
            if MaxNum not in array:
                FinalNum = MaxNum
                LoopStat = False
            elif MaxNum in array:
                NoInt += 1

        else:
            FinalNum = 1
            LoopStat = False
  
    return FinalNum

def main():
    Loopstat = True
    PosArray = [1,4,6,2,3]
    NegArray = [-5,-3,-2]
    FullArray = [1,2,3]
    
    while Loopstat == True:
        switcher = int(input("Please select array to use on solution (Positive = 1, Negative = 2, or Full = 3):"))

        if switcher == 1:
            temp = str(solution(PosArray))
            Loopstat = False
            print("The output is " + temp + ". The answer is 5")
        

        elif switcher == 2:
            temp = str(solution(NegArray))
            Loopstat = False
            print("The output is " + temp + ". The answer is 1")

        elif switcher == 3:
            temp = str(solution(FullArray))
            Loopstat = False
            print("The output is " + temp + ". The answer is 4")

        else:
            print("Invalid input, please try again.")


if __name__ == "__main__":
        main()
