from collections import defaultdict

words = []
with open("dictionary.txt") as file:
    for line in file.readlines():
        words.append(line.strip())
for w in words:
    print(w)

threepicks = []

def has_repeat_letters(w):
    lettercount = defaultdict(int)
    for letter in w:
        lettercount[letter] = lettercount[letter] + 1
    return max(lettercount.values()) > 1

words_with_unique_letters = []
for w in words:
    if not has_repeat_letters(w):
        words_with_unique_letters.append(w)

def get_index(word, wordlist):
    for index,test in enumerate(wordlist):
        if word.upper() == test.upper():
            return index
    return -1

w1_test_indices = range(len(words))
w1_test_indices = [get_index("beach", words)]

for w1_index in w1_test_indices:
    print(f"Progress: {w1_index} / {len(words)}")
    w1 = words[w1_index].strip()
    if has_repeat_letters(w1):
        continue
    for w2_index in range(w1_index, len(words)):
        w2 = words[w2_index].strip()
        if has_repeat_letters(w1+w2):
            continue
        for w3_index in range(w2_index, len(words)):
            w3 = words[w3_index].strip()
            bigword = w1+w2+w3
            if has_repeat_letters(bigword):
                continue
            #print(f"❤️ Found: {w1} {w2} {w3}")
            threepicks.append([w1, w2, w3])

for w in threepicks:
    print(f"❤️ Found: {w}")

