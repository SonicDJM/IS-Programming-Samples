# Put your code here
mydict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

def repToDecimal(mystring,mybase):
    numbase10 = 0
    digitcount = 0
    for digit in mystring[::-1]:
        numbase10 += mydict[digit] * mybase ** digitcount #digitcount represents our position and exponent
        digitcount += 1
    return numbase10

# A main for testing your program
def main():
    """Tests the function."""
    print(repToDecimal('10', 10))
    print(repToDecimal('10', 8))
    print(repToDecimal('10', 2))
    print(repToDecimal('10', 16))

# The entry point for program execution
if __name__ == "__main__":
    main()
