# Put your code here
inputfile = input("Please type in the input file: ")
outputfile = input("Please type in the output file: ")
n = 1

f = open(inputfile, 'r')

lines = f.readlines()
f.close()

f = open(outputfile, 'w')
for line in lines:
    f.write(str("%4s" % n) + '> ' + line)
    n += 1
f.close()
