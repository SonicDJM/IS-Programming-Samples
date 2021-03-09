# Put your code here
vitalfile = input("Enter the file name: ")
f = open(vitalfile, 'r')
vitalinfo = f.readlines()
print("Name", "%18s" % "Hours", "%15s" % "Total Pay")
for line in vitalinfo:
    splitline = line.split()
    totalPay = float(splitline[1]) * float(splitline[2])
    print("%-15s" % splitline[0], "%7s" % splitline[1],"%15.2f" % totalPay)
