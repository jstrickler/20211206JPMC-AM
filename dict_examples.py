d1 = dict()   # empty dict
d2 = {'NC': 'North Carolina', 'TX': 'Texas'}
d3 = {} # empty dict
d4 = dict(NC="North Carolina", TX="Texas")

states = {'NC': 'North Carolina', 'TX': 'Texas'}
states['IL'] = 'Illinois'
states['HI'] = 'Hawaii'

print(states, '\n')

for state in 'NC', 'MD', 'NJ', 'DE', 'TX':
    print(state, state in states)
print()

states['NC'] = 'Georgia'
print(states)

print(states['NC'], states['TX'], states['HI'])
print(states.get('VA'))
print(states.get('VA', "NOT FOUND"))

new_data = [('NC', 'North Carolina'), ('MI', 'Michigan'), ('CA', 'California')]
print('-' * 60)
for abbr, name in new_data:
    print(abbr, name, states.setdefault(abbr, name))
print(new_data)
print(states)
print()

for abbr, name in states.items():
    print(abbr, name)
print()
print(list(states.items()))
print(states.items())
print(states.keys())
print(states.values())








