
animal = 'aardvark'  # global var

def spam():
    animal = 'alligator'
    print("animal: {}\n".format(animal))
    country = "Mongolia"  # local var

spam()
print("animal: {}\n".format(animal))
# print("country: {}\n".format(country))


