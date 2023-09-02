import collections
# This function takes three diffrent arreys and sorts them in desending order (Bigger to Smaller) and lists the stacks the values come from in a single variable that is returned
def solution(stack1, stack2, stack3):
    # Implement your solution here
    StackOrder = ""
    dict = {}
    for i in stack1:
        dict[i] = "stack1"
    for i in stack2:
        dict[i] = "stack2"
    for i in stack3:
        dict[i] = "stack3"
    SortDict = collections.OrderedDict(sorted(dict.items(), reverse = True))
    for i in SortDict.values():
        if i == "stack1":
            StackOrder = StackOrder + "1"
        elif i == "stack2":
            StackOrder = StackOrder + "2"
        elif i == "stack3":
            StackOrder = StackOrder + "3"
    return StackOrder

def main():
    Array1 = [4,5,3]
    Array2 = [2,6,1]
    Array3 = [8,7]

    ResultArray = solution(Array1, Array2, Array3)
    print(ResultArray)

if __name__ == "__main__":
    main()
