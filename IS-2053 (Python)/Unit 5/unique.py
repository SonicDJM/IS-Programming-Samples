# Put your code here
fileName = str(input("Enter the input file name: "))
print("\n")
f = open(fileName, 'r')
wordList = f.read()
wordList = wordList.split()
wordList.sort()
for word in wordList:
    print(word)
f.close()
