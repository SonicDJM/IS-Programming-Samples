import turtle

def drawFractalLine(width, height, size, level):
    if level > 0:
        for d in [60, -120, 60, 0]:
            drawFractalLine(width, height, size / 3, level-1)
            # t.forward(size / 3)
            turtle.left(d)
            # t.setheading(d)
            
        
    else:
        turtle.forward(size)


def main():
    width = 200
    height = 200
    size = 150
    level = 4
    for i  in range(3):
        drawFractalLine(width, height, size, level)
        turtle.right(120)



if __name__ == "__main__":
    main()

