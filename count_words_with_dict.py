letter_counts = {}

with open('DATA/words.txt') as words_in:
    for word in words_in:
        letter = word[0]
        if letter not in letter_counts:
            letter_counts[letter] = 0

        letter_counts[letter] += 1

print(letter_counts)
