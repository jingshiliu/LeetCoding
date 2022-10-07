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


print(minWindow("abc", "b"))