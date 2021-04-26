import math

def sphereVol(value):
    # Deconstruct for radius
    tempHol = value / 4
    tempHol = tempHol / math.pi
    radiusHol = math.sqrt(tempHol)
    # Use radius for Volume
    tempHol = radiusHol ** 3
    tempHol = tempHol * math.pi
    finalVal = tempHol * (4/3)
    return finalVal

def cubeVol(value):
    # Decounstruct to find a side length
    tempHol = value / 6
    cubeSide = math.sqrt(tempHol)
    # Calculate Volume
    finalVal = cubeSide ** 3
    return finalVal

def tpVol(value):
    # Unable to do the math relating to such a shape, Sorry about that
    return



def main():
    # Input function
    while True:
        InputNum = float(input("Please input a positive number: "))
        if InputNum < 0:
            print("Invalid Number, try again please")
        else:
            shapeType = str(input("Select Sphere, Cube, or Triangualar Pyramid: "))
            if shapeType == "Sphere":
                valueSphere = sphereVol(InputNum)
                print("The volume of a sphere with the given area is: ", valueSphere)
            elif shapeType == "Cube":
                valueCube = cubeVol(InputNum)
                print("The volume of a cube with the given area is: ", valueCube)
            elif shapeType == "Triangular Pyramid":
                #valueTP = tpVol(InputNum)
                #print("The volume of a Triangular Pyramid with the given area is: ", valueTP)
                print("Unable to do this")
            else:
                print("Invalid Shape")



if __name__ == "__main__":
    main()
