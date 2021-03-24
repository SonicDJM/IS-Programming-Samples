'''
Example alternative to range() function in python
'''
def myRange(start, stop=None, step=None):
    mylist = []
    i=0
    if (stop == None and step == None):
        stop = start
        while i < stop:
            mylist.append(i)
            i += 1
    elif (step == None):
        i = start
        while i < stop:
            mylist.append(i)
            i += 1
    else:
        i = start
        if step > 0:
            while i < stop:
                mylist.append(i)
                i += step
        else:
            while i > stop:
                mylist.append(i)
                i += step
        
    
    return mylist

print(myRange(10))
print(myRange(10,1,-1))

        
    