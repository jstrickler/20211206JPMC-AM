from john.math import geometry
import sys

a = geometry.circle_area(55)
b = geometry.rectangle_area(10, 8)
print(a, b)
print(geometry.ANIMAL)

# module search
#  1. current folder
#  2. folders in PYTHONPATH
#  3. under Python installation folder
print('-' * 60)
for path in sys.path:
    print(path)




