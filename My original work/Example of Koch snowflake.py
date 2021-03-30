import turtle


def kochFractal(width, height, size, level):
    t = turtle.Turtle()
    t.up()
    t.hideturtle()
    t.goto(-width // 3, height // 4)
    t.down()
    for d in [0, -120, 120]:
        drawFractalLine(t, size, d, level)


def drawFractalLine(t, distance, direction, level):
    if (level == 0):
        polarLine(t, distance, direction)
    else:
        drawFractalLine(t, distance // 3, direction, level - 1)
        drawFractalLine(t, distance // 3, direction + 60, level - 1)
        drawFractalLine(t, distance // 3, direction - 60, level - 1)
        drawFractalLine(t, distance // 3, direction, level - 1)


def polarLine(t, distance, direction):
    t.setheading(direction)
    t.forward(distance)


def main():
    width = 200
    height = 200
    size = 150
    level = 4
    kochFractal(width, height, size, level)


if __name__ == '__main__':
    main()