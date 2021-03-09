# Input and setup
encyptedText = input("Enter the coded text: ")
distanceValue = int(input("Enter the distance value: "))
plainText = ""

# Math
for ch in encyptedText:
    ordValue = ord(ch)
    cypherValue = ordValue - distanceValue
    if ordValue - distanceValue < 0:
        cypherValue = ordValue - distanceValue + 128
    else:
        cypherValue= ordValue - distanceValue
    plainText += chr(cypherValue)
print(plainText)    
