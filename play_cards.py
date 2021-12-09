from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Nellie")
d2 = CardDeck("Andy")
print(d1)

# very evil:
# print(d1._dealer)

print(d1.dealer)
d1.dealer = 'Fred'
print(d1.dealer)
try:
    d1.dealer = 123.4
except Exception as err:
    print(err)
else:
    print(d1.dealer.upper())

d1.shuffle()
print(d1.cards)
for _ in range(5):
    print(d1.draw())
print(d1)

print(len(d1))
print(len(d2))
print(d2)
print(repr(d2))
print('-' * 60)

j1 = JokerDeck("Jill")
j1.shuffle()
print(j1.cards)
print(j1)
print(len(j1))

