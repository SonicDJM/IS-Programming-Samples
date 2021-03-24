import random

 

def recursiveExample(num,count=0):

    count+=1

    while num<100:

        num += random.randrange(1,9)

        num, count = recursiveExample(num,count)

    return(num,count)

 

num,count = recursiveExample(random.randrange(1,9))

print("We ended at",num,"and it took",count,"recursive steps!")