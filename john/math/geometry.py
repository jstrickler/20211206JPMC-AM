import math

ANIMAL = 'wombat'

def circle_area(diameter):
    radius = diameter / 2
    return math.pi * radius ** 2

def rectangle_area(length, width):
    return length * width
# 'private' function
def _helper():
    pass

# if running as script NOT imported as module
if __name__ == '__main__':
    print("RUNNING MODULE")
    print(circle_area(25))
    print(rectangle_area(5, 10))
