

def printInstruction():
    print("This program calculates the serfacearea of the rectangle")
    print("Please enter the data of the rectangle")


def the_area_of_the_rectangle(length, width):
    area = length * width
    return area


def the_surface_area_of_the_rectangle(length, width, height):
    front = length * height
    side = width * height
    top = length * width


def getLength():
    length = input("Enter Length:")
    return length


def getWidth():
    width = input("Enter Width:")
    return width


def getHeight():
    height = input("Enter Height:")
    return height


def main():
    printInstruction()
    length = getLength()
    width = getWidth()
    height = getHeight()
    the_surface_area_of_the_rectangle()
    printresult()

main()
