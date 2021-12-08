person = "Bill", "Gates", "Microsoft", "1955-10-28"

print(person[0], person[1])

first_name, last_name, product, dob = person

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

print(type(people), type(people[0]), type(people[0][0]))

for person in people:
    print(person)
print('-' * 60)

for person in people:
    first_name, last_name, product, dob = person
    print(first_name, last_name)
print('-' * 60)

#   people[0]    people[1] people[2] ...
for first_name, last_name, product, dob in people:
    print(first_name, last_name)
print('-' * 60)

data = [('Bob', 5), ('Mary', 7), ('Nellie', 2)]
for name, number in data:
    print(name, number)
print()



