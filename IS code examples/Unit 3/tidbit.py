# Input
puchasePrice = float(input("Enter the puchase price: "))
downPay = (puchasePrice * 0.1)
month = 0
# Math
startBalance = puchasePrice - downPay
monthPay = (startBalance * 0.05)
endBalance = startBalance
print( "%-6s" % "Month", "%8s" % "Starting Balance", "%18s" % "Interest to Pay", "%22s" % "Principal to Pay" "%10s" % "Payment", "%15s" % "Ending Balance")

while endBalance > 0:
    # Annual Intrest
    interestPay = (startBalance * 0.12) / 12

    # Principal
    if monthPay < startBalance:
        principalPay = monthPay - interestPay
    else:
        principalPay = startBalance
    # Payment
    if monthPay < startBalance:
        totalPay = monthPay
    elif monthPay > startBalance:
        interestPay = 0
        totalPay = startBalance
    else:
        print("ERROR")
    # End Balence
    endBalance = startBalance - principalPay
    month += 1
    print( "%-6.0f" % month,  "%10.2f" % startBalance,  "%16.2f" % interestPay,  "%17.2f" % principalPay,  "%17.2f" % totalPay,  "%16.2f" % endBalance)
    startBalance = endBalance
