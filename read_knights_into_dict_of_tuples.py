from pprint import pprint

knight_info = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_info[name] = title, color, quest, comment

pprint(knight_info)

for name, data in knight_info.items():
    print(name, data)
print('-' * 60)

for name, data in knight_info.items():
    print(data[0], name)
print('-' * 60)

print(knight_info['Lancelot'][2])
print(knight_info['Bedevere'][1])

