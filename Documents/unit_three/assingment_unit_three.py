

def area_of_base(length, width):
    width = 4
    length = 3
    area_of_base = length * width
    return area_of_base

def area_of_side(width, height):
    width = 4
    height = 9
    area_of_side = width * height
    return area_of_side

def area_of_front(length, height):
    length = 3
    height = 9
    area_of_front = length * height

def main(surface):
    surface = area_of_base + area_of_side + area_of_front
    print(surface)

main(surface)