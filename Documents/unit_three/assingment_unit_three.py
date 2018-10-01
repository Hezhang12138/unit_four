

def printInstruction():
    print("This program calculates the serfacearea of the rectangle")
    print("Please enter the data of the rectangle")


def the_area_of_the_rectangle(length, width):
    area = length * width
    return area


def getLength():
    length = input("Enter Length:")
    return length


def getWidth():
    width = input("Enter With:")
    return width


def getHeight():
    height = input("Enter Height:")
    return height


def sidearea1():
    sidearea1 = length * getWidth()


def sidearea2():
    sidearea2 = getWidth() * getHeight()


def sidearea3():
    sidearea3 = getLength() * getHeight()


def surfacearea():
    surfacearea = sidearea1() + sidearea2() + sidearea3()



def main():
    printInstruction()
    length = getLength()
    width = getWidth()
    height = getHeight()
    sidearea1()
    sidearea2()
    sidearea3()
    surfacearea()
    printresult()

main()
