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
    # Input height value
    tpHight = float(input("Please input the height of the Triangular Pyramid: "))
    # Performs calculations
    finalVal = (value * tpHight) * (1/3)
    return finalVal



def main():
    # Input function
    while True:
        InputNum = float(input("Please input a positive number: "))

        if InputNum < 0:
            print("Invalid Number, try again please")

        else:
            shapeType = str(input("Select Sphere, Cube, or Triangular Pyramid: "))

            if shapeType == "Sphere":
                valueSphere = sphereVol(InputNum)
                print("The volume of a sphere with the given area is: ", valueSphere)
                break

            elif shapeType == "Cube":
                valueCube = cubeVol(InputNum)
                print("The volume of a cube with the given area is: ", valueCube)
                break

            elif shapeType == "Triangular Pyramid":
                valueTP = tpVol(InputNum)
                print("The volume of a Triangular Pyramid with the given area is: ", valueTP)
                break

            else:
                print("Invalid Shape")



if __name__ == "__main__":
    main()
