# Put your code here
fileName = str(input("Enter the input file name: "))
print('\n')
mydict = {}
myfile = open(fileName,'r')
for line in myfile:
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word in mydict:
            mydict[word] = mydict[word] + 1
        else:
            mydict[word] = 1
mylist = list(mydict.keys())
mylist.sort()
for item in mylist:
    print(item, mydict[item])
myfile.close()
