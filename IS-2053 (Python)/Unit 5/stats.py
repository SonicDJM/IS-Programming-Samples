# Put your code here
lyst = [3, 1, 7, 1, 4, 10]

# Median function
def median(x):
    medianNum = []
    for numbers in x:
        medianNum.append(float(numbers))
    medianNum.sort()
    midpoint = len(medianNum) // 2
    if len(medianNum) % 2 == 1:
        return medianNum[midpoint]
    else:
        return (medianNum[midpoint] + medianNum[midpoint - 1])/ 2

def mean(x):
    numInt = 0
    totalSum = 0
    for numbers in x:
       totalSum = numbers + totalSum
       numInt += 1
    meanSum = totalSum / numInt
    return meanSum

def mode(x):
    modeNum = max(x, key = x.count)
    return modeNum

def main():
    print("List: ",lyst)
    print(f'Mode: {mode(lyst)}')
    print(f'Median: {median(lyst)}')
    print(f'Mean: {mean(lyst)}')

if __name__ == "__main__":
    main()
