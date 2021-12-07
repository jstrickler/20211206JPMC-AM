actor = "Chris Hemsworth"

print(actor)
print(len(actor), type(actor))
print(actor.upper())
a1 = actor.upper()

# print(dir(a1))
print(actor.capitalize())
s = "abc def ghi"
print("123".capitalize(), s.upper(), s.capitalize(),
      s.title())

print(actor.count('Chris'))
print(actor.count('Liam'))
print(actor.count('h'))
print(actor.count('H'))
print(actor.lower().count('h'))  # method chaining
print(actor.startswith('Chris'))
print(actor.startswith('Liam'))
print("worth" in actor)  # substr
print("value" in actor)

print(actor.replace("Chris", "Liam"))
print(actor.replace("worth", ""))

print(actor.find("worth"))
print(actor.find("value"))

s = "every    good boy   does    fine      "
words = s.split()
print(words)

s = "fee:fi:fo:fum"
words = s.split(':')
print(words)  # words is a list

s = "       All my exes live in Texas       "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

m = "The end....."
print(m.rstrip('.'))

n = "abc1309308408240248"
print(n.rstrip('0123456789'))

line = "spam ham toast\n"
x = line.rstrip()
print("x is", x)
print("Done")











