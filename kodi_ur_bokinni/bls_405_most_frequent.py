import sys
freq = {}
for piece in open(sys.path[0] + "/freq_data.txt").read().lower().split():
    # only consider alphabetic characters in this piece
    word = "".join(c for c in piece if c.isalpha())
    if word:    # require at least one alphabetic character
        freq[word] = 1 + freq.get(word, 0)

max_word = ""
max_count = 0
for (w,c) in freq.items():  # (key, value) tuple represents (word, count)
    if c > max_count:
        max_word = w
        max_count = c
print("The most frequent word is", max_word)
print("It's number of occurrences is", max_count)