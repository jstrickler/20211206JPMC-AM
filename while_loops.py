i = 0
while i < 3:
    print(i)
    i += 1
print()


while True:
    name = input("What is your name? (or q to quit) ")
    if name == 'q':
        break  # exit loop
    if name == '':
        print("please enter a name...")
        continue
    print("Hi,", name)

