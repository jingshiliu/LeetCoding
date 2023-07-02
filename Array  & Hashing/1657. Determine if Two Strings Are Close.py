from collections import defaultdict


def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2): return False

    word1_counter = defaultdict(lambda: 0)
    word2_counter = defaultdict(lambda: 0)

    for c in word1:
        word1_counter[c] += 1
    for c in word2:
        word2_counter[c] += 1

    if word1_counter.keys() != word2_counter.keys():
        return False

    num_chars1 = defaultdict(lambda: [])
    num_chars2 = defaultdict(lambda: [])
    for c in word1_counter.keys():
        char_count = word1_counter[c]
        num_chars1[char_count].append(c)

    for c in word2_counter.keys():
        char_count = word2_counter[c]
        num_chars2[char_count].append(c)

    print(num_chars1, '\n', num_chars2)
    for num in num_chars1.keys():
        if len(num_chars1[num]) != len(num_chars2[num]):
            return False

    return True