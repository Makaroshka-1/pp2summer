import math

def to_radian(degree):
    print(math.radians(degree))

def trapezoid_area():
    print("Height: ")
    height = int(input())
    print("Base, first value: ")
    first_base  = int(input())
    print("Base, second value: ")
    second_base = int(input())
    print("Expected Output: ")
    print((first_base+second_base/2)*height)

def polygon_area():
    sides  = int(input())
    length = int(input())
    angle = 180/sides
    height = math.cos(math.radians(angle))/math.sin(math.radians(angle))*length/2
    return sides * height * length/2  


def parallelogram_area():
    height = int(input())
    base = int(input())
    return height * base 

    
