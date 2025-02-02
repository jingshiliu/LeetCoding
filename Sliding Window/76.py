def minWindow(s: str, t: str) -> str:
    if t == "":
        return ""

    validWindow = {}
    for char in t:
        validWindow[char] = validWindow.get(char, 0) + 1

    res = [0, len(s)]
    l = 0
    have, need = 0, len(validWindow)

    count = {}
    for i in t:
        count[i] = 0

    for r in range(len(s)):
        if s[r] in t:
            count[s[r]] += 1
            if count[s[r]] == validWindow[s[r]]:
                have += 1

            while have == need:
                if res[1] - res[0] + 1 > r - l + 1:
                    res[0] = l
                    res[1] = r

                if s[l] in t:
                    count[s[l]] -= 1
                    if count[s[l]] < validWindow[s[l]]:
                        have -= 1
                l += 1

    if l == 0 and have < need:
        return ""

    return s[res[0]: res[1] + 1]


# print(minWindow("abc", "b"))


def min_window2(s: str, t: str) -> str:
    count_t = [0] * 58
    count_s = [0] * 58
    need_to_match = 0
    for c in t:
        i = ord(c) - 65
        if count_t[i] == 0:
            need_to_match += 1
        count_t[i] += 1
        
    res = [-1 * len(s) - 1 , 0]
    l = 0
    for r in range(len(s)):
        i = ord(s[r]) - 65
        count_s[i] += 1

        if count_s[i] == count_t[i]:
            need_to_match -= 1
        while not need_to_match:
            l_key = ord(s[l]) - 65
            if r - l < res[1] - res[0]:
                res[0] = l
                res[1] = r + 1
            count_s[l_key] -= 1
            if count_s[l_key] < count_t[l_key]:
                need_to_match += 1
            l += 1
    if res[0] < 0:
        return ""
    return s[res[0]: res[1]]

print(min_window2("ADOBECODEBANC", "ABC"))






























