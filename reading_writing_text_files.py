file_path = 'DATA/mary.txt'

mary_in = open(file_path, 'r')
# ...
mary_in.close()

with open(file_path) as mary_in:
    pass

# with open('DATA/new/fun.txt')

with open(file_path) as mary_in:
    for raw_line in mary_in:   # raw line has \n
        line = raw_line.rstrip()  # line does not have \n
        print(line)
print('-' * 60)

with open(file_path) as mary_in:
    contents = mary_in.read()
    print("raw:")
    print(repr(contents))
    print("normal:")
    print(contents)
print('-' * 60)

with open(file_path) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

with open(file_path) as mary_in:
    all_lines_without_nl = mary_in.read().splitlines()
    print(all_lines_without_nl)

start_letter = 'k'
word_count = 0
with open('DATA/words.txt') as words_in:
    for line in words_in:
        if line.startswith(start_letter):
            word_count += 1
print(f"{word_count} words start with {start_letter}")
print()

cat_count = 0
with open('DATA/words.txt') as words_in:
    for raw_line in words_in:
        if 'cat' in raw_line:
            cat_count += 1
            line = raw_line.rstrip()
            print(line)
print(f"{cat_count} words contain 'cat'")
print('-' * 60)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit.upper() + '\n')

with open('DATA/words.txt') as words_in:
    with open('cats.txt', 'w') as cats_out:
        for line in words_in:
            if 'cat' in line:
                cats_out.write(line)