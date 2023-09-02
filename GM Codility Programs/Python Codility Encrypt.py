# This function encrypts words (In all caps) using a Caesar Cypher with a fixed key of 4
import re


def encrypt(text):
    # Implement your solution here
    CyphText = ""
    for l in text:
        CharNum = ord(l)
        CharNum += 4
        if CharNum > 90:
            RemNum = CharNum - 90
            CharNum = 64 + RemNum
        
        FinalNum = chr(CharNum)
        CyphText = CyphText + FinalNum
    return CyphText

def main():
    PlainText1 = "PINEAPPLE"
    PlainText2 = "APPLE"
    PlainText3 = "ZENIMAX"

    ResultNum = encrypt(PlainText1)
    print("PlainText1: ", PlainText1, "CyphText: ", ResultNum)
    ResultNum = encrypt(PlainText2)
    print("PlainText2: ", PlainText2, "CyphText: ", ResultNum)
    ResultNum = encrypt(PlainText3)
    print("PlainText3: ", PlainText3, "CyphText: ", ResultNum)

if __name__ == "__main__":
    main()
