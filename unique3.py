from collections import defaultdict

words = []
with open("dictionary.txt") as file:
    for line in file.readlines():
        words.append(line.strip())

def letter_count(word):
    lc = defaultdict(int)
    for letter in word:
        lc[letter] = lc[letter] + 1
    return lc

def has_repeat_letters(w):
    return max(letter_count(w).values()) > 1

words_with_unique_letters = []
for w in words:
    if not has_repeat_letters(w):
        words_with_unique_letters.append(w)

overall_letter_count = letter_count("".join(words))

def popularity(word):
    score = 0
    seen_letters = {}
    for letter in word:
        if letter not in seen_letters:
            score += overall_letter_count[letter]
        seen_letters[letter] = True
    return score

"""
weighted_popularity - if more popular letters found in the beginning, that's
good for the score. Popularity benefit decreases if popular letters found
towards end.
"""
def weighted_popularity(words, decay=0.8):
    score = 0.0
    factor = 1.0
    for word in words:
        score += factor * popularity(word)
        factor *= decay
    return score


virginias_starting_words = ["truly", "grade", "pound", "shirk"]
print(virginias_starting_words)
print(weighted_popularity(virginias_starting_words))

andrew_starting_words = ["fjord", "waltz", "quick", "nymph"]
print(andrew_starting_words)
print(weighted_popularity(andrew_starting_words))

def sort_dict_decreasing_values(input):
    return dict(sorted(input.items(), key=lambda item: -item[1]))

print(f"The overall letter frequencies are: {sort_dict_decreasing_values(overall_letter_count)}")

print(f"Finding best N=3 starting words with unique letters and max popularity")

word_set_for_best_N_test = words_with_unique_letters
threepicks = []

w1_test_indices = range(len(word_set_for_best_N_test))
n3_weighted_popularities = {}
best_n3 = []
best_n3_score = 0.0
for w1_index in w1_test_indices:
    w1 = word_set_for_best_N_test[w1_index]
    print(f"Progress: {100*w1_index/len(w1_test_indices)}")
    if has_repeat_letters(w1):
        continue
    for w2_index in range(w1_index, len(word_set_for_best_N_test)):
        w2 = word_set_for_best_N_test[w2_index]
        if has_repeat_letters(w1+w2):
            continue
        for w3_index in range(w2_index, len(word_set_for_best_N_test)):
            w3 = word_set_for_best_N_test[w3_index]
            bigword = w1+w2+w3
            n3 = [w1, w2, w3]
            score = weighted_popularity(n3)
            n3_weighted_popularities[bigword] = score
            if score > best_n3_score:
                best_n3 = n3
                best_n3_score = score
            if has_repeat_letters(bigword):
                continue
            threepicks.append(n3)

print(f"Best starting 3: {sort_dict_decreasing_values(n3_weighted_popularities)}")

print(f"Best N3: {best_n3} score: {best_n3_score}")

best_n4 = []
best_n4_score = 0.0

for w4 in word_set_for_best_N_test:
    if w4 in best_n3:
        continue
    n4 = n3 + [w4]
    score = weighted_popularity(n4)
    if score > best_n4_score:
        best_n4_score = score
        best_n4 = n4

print(f"Best N4: {best_n4} score: {best_n4_score}")

for w5 in word_set_for_best_N_test:
    if w5 in best_n4:
        continue
    n5 = n4 + [w5]
    score = weighted_popularity(n5)
    if score > best_n5_score:
        best_n5_score = score
        best_n5 = n5

print(f"Best N5: {best_n5} score: {best_n5_score}")