#Write your program below:
import turtle
import math

def drawCircle(t, startPoint, Radius):
    t.goto(startPoint)
    t.setheading(90)
    t.down()
    distance = 2.0 * math.pi * Radius / 120.0
    loopInt = range(120)
    for int in loopInt:
        t.left(3)
        t.forward(distance)
    t.up()



def main():
    t = turtle.Turtle()
    t.up()
    x = 150
    y = 75
    startPoint = (x, y)
    Radius = 100
    drawCircle(t, startPoint, Radius)


if __name__ == "__main__":
    main()
