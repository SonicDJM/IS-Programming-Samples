"""
File: enlarge.py
Project 7.11

Defines and tests a function to enlarge an image.
"""

from images import Image

def enlarge(image, factor):
    width = image.getWidth()
    height = image.getHeight()
    newX = width * factor
    newY = height * factor
    new = Image(newX, newY)
    for y in range(height):
        for x in range(width):
            oldP = image.getPixel(x, y)
            new.setPixel(x*factor, y*factor, oldP)
            new.setPixel((x*factor)+1, y*factor, oldP)
            new.setPixel(x*factor, (y*factor)+1, oldP)
            new.setPixel((x*factor)+1, (y*factor)+1, oldP)
    return new

def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    #image.draw() #DEBUG
    newimage = enlarge(image, 2)
    newimage.draw()

if __name__ == "__main__":
   main()


