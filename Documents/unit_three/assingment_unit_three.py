# Frank Zhang
# 10/1/18
# this program helps me a lot to understand what computer science is. Before this I did not figure out what it is.
# Unless I know what I should do.


def printInstruction():
    print("This program calculates the serfacearea of the rectangle")
    print("Please enter the data of the rectangle")


def getLength():
    length = input("Enter Length:")
    return float(length)


def getWidth():
    width = input("Enter Width:")
    return float(width)


def getHeight():
    height = input("Enter Height:")
    return float(height)


def the_area_of_the_rectangle(length, width):
    area = length * width
    return area


def the_surface_area_of_the_rectangle(length, width, height):
    front = length * height
    side = width * height
    top = length * width
    return 2 * (front + side + top)


def main():
    printInstruction()
    length = getLength()
    width = getWidth()
    height = getHeight()
    surfacearea = the_surface_area_of_the_rectangle(length, width, height)
    print("the surface area is", surfacearea)


main()
