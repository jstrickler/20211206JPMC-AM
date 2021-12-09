import math
import os

def get_message():
    return "Hello, JPMC world"

message = get_message()
print("message:", message)

def show_message():
    msg = get_message()
    print(msg)

show_message()

def circle_area(diameter):
    radius = diameter / 2
    return math.pi * radius ** 2

def rectangle_area(length, width):
    return length * width

print(circle_area(10))
print(rectangle_area(14, 9.6))

def search(search_string, *paths, ignore_case=False):
    for path in paths:
        file_name = os.path.basename(path)
        with open(path) as file_in:
            for line in file_in:
                if search_string in line:
                    print(f"{file_name}: {line.rstrip()}")

search('bird', 'DATA/parrot.txt', 'DATA/alice.txt')
print('-' * 60)
search('sasquatch')
print('-' * 60)
search('sasquatch', 'DATA/words.txt', ignore_case=True)

def get_value(*, city, state):
    pass

get_value(city='Houston', state='TX')
get_value(state='NY', city='Corning')

def hello(whom="world"):
    print("Hello,", whom)

hello("Mom")
hello()

def config(**values):
    print("Config values:",  values)

config(file_name="wombats.txt", country="Burkina Faso")

#  et.Element('person', id="123abc", zip="12345")
#   <person id="123abc zip="12345"></person>









