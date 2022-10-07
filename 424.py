def characterReplacement(s: str, k: int) -> int:
    if not len(s) or s == len(s):
        return len(s)

    count = [0] * 26

    def getMostFrequentCharInWindow():
        res = 0
        for index in range(26):
            if count[res] < count[index]:
                res = index
        return count[res]

    res = 0
    l, r = 0, 0

    for character in s:
        count[ord(character) - ord('A')] += 1
        r += 1
        if getMostFrequentCharInWindow() + k >= r - l:
            res = max(r - l, res)
        else:
            count[ord(s[l]) - ord('A')] -= 1
            l += 1


    return res


print(characterReplacement("ABAA", 0))