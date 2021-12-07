person = "Fred Flintstone"
city = "Bedrock"
value = 47.3292930930932

print(person)  # str(person) + '\n'

print(person, city, value)
# str(person) + ' ' + str(city) + ' ' + str(value) + '\n'

print(person, end=' ')
print(city, end=' => ')
print(value)
print(person, city, value, sep='/')
print(person, city, value, sep=', ')
print(person, city, value, sep='')
print()
print(person, "lives in", city)

print("{} lives in {}".format(person, city))
print(f"{person} lives in {city} ({person})")
print("{0} lives in {1} ({0})".format(person, city))

print("Value:", value)
print("Value: {}".format(value))
print("Value: {:.2f}".format(value))
print(f"Value: {value:.2f}")
