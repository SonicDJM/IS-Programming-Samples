# Put your code here
def printAll(seq):
    print(seq)
    if seq:
        print(seq[0])
        printAll(seq[1:])

mylist = ['Cat','Dog','Mouse']
mystring = 'CatDogMouse'
mytuple = (1,2,3,4,5)

printAll(mylist)
printAll(mystring)
printAll(mytuple)