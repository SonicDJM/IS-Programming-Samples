"""
File: sepia.py
Project 7.8

Defines and tests a function for converting images to sepia.
"""

from images import Image

def sepia(image):
    image2 = grayscale(image)
    # image2.draw() #DEBUG
    for y in range(image2.getHeight()):
        for x in range(image2.getWidth()):
            (red, green, blue) = image2.getPixel(x, y)
            if red < 63:
                red = int(red * 1.1)
                blue = int(blue * 0.9)
                image2.setPixel(x, y, (red, green, blue))
            elif red < 192:
                red = int(red * 1.15)
                blue = int(blue * 0.85)
                image2.setPixel(x, y, (red, green, blue))
            else:
                red = min(int(red * 1.08), 255)
                blue = int(blue * 0.93)
                image2.setPixel(x, y, (red, green, blue))
    return image2

def grayscale(image):
    """Converts an image to grayscale."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))
    return image

def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    image = sepia(image)
    image.draw()

if __name__ == "__main__":
   main()


