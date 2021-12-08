list1 = list()   # list list1 = new list()
list2 = ['blue', 'yellow', 'purple', 'pink']
list3 = []  # empty list

cities = ['Plano', 'Columbus', 'Jersey City', 'Wilmington']
print(cities[0], cities[3], cities[-1], cities[len(cities)-1])

print(cities)
cities.append("Houston")
cities.append("Dallas")
print(cities)
cities.insert(0, "Kathmandu")
print(cities)
cities.insert(5, "San Francisco")
print(cities)
more_cities = ['Kolkata', 'Mumbai', 'Hyderabad']
cities.extend(more_cities)
print(cities)

#  LIST.append(obj)  LIST.insert(pos, obj)  LIST.extend(iterable)
del cities[3]   # remove 4th element
print(cities)

cities.remove("Mumbai")
print(cities)
# cities.remove('Durham')

c = cities.pop()
print(c, cities)

c = cities.pop(4)
print(c, cities)

food = ['spam', 'eggs', 'spam', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs',
        'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', ]

print(food.count('spam'))
print(food.count('eggs'))
print(food.count('ham'))

print(cities)
print(cities[1])
print(cities[-1])
print(cities[0:3], cities[:3])

#  SEQUENCE[START:STOP]    SEQUENCE[:STOP]  SEQUENCE[START:]
#  SEQUENCE[START:STOP:STEP]
print(cities[1:5])

s = "Python rocks"
print(s[:6], s[7:12], s[-5:])
print(s[3:6])

print(cities)
print()
for city in cities:
    # city = next-element-of-cities
    print(city, city.upper())
print()

s = "abc"
for char in s:
    print(char.upper())

print("city: {}\n".format(city))
print("char: {}\n".format(char))
print(cities)
print(len(cities), min(cities), max(cities))
print(sorted(cities))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
print(sum(nums))

print(cities)
r = reversed(cities)
print(r)
for city in r:
    print(city, end=" ")
print()

colors = ['red', 'blue', 'green', 'purple', 'pink', 'white', 'black']

zz = zip(cities, colors)
print(zz)
for city, color in zz:
    print(city, color)
print()

print(list(zz))
z2 = zip(cities, colors)
print(list(z2))
print(list(z2))

print(cities, '\n')

for i, city in enumerate(cities):
    print(i, city)
print('-' * 60)
print(list(enumerate(cities)))
print('-' * 60)

for i, city in enumerate(cities, 1):
    print(i, city)
print()

for i in range(3):
    print("Hip hip hooray")
print()
print(list(range(3)))
# range(stop)  range(start, stop)  range(start, stop, step)



for i in range(1, 11):
    print(i)
print()

for i in range(5, 101, 5):
    print(i, end=' ')
print('\n')

print('-' * 60)

flags = [True] * 10
print(flags)
print("Python" * 5)
print([1, 2, 3] * 4)

print([0] * 25)





