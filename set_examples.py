bob_countries = ['Spain', 'India', 'Nepal', 'Burkina Faso', 'New Zealand', 'Canada',
                 'Mongolia', 'Ireland']

mary_countries = ['India', 'Nepal', 'India', 'India', 'New Zealand', 'Portugal',
                  'France', 'Estonia', 'France', 'Canada']

bob = set(bob_countries)
mary = set(mary_countries)
bob.add('Denmark')
mary.add('Japan')
mary.add('Denmark')

print("Common:", bob & mary) # intersection
print("Not common:", bob ^ mary)  # xOR
print("Both:", bob | mary)   # union
print("Bob only:", bob - mary)
print("Mary only:", mary - bob)

food = ['spam', 'eggs', 'spam', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs',
        'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', ]

unique_food = set(food)
print("unique_food: {}\n".format(unique_food))


