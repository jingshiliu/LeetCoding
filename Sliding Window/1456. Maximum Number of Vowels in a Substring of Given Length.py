def max_vowels(s: str, k: int) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}

    res = 0
    for i in range(k):
        if s[i] in vowels:
            res += 1
    cur = res
    l = 0
    for i in range(k, len(s)):
        if s[l] in vowels:
            cur -= 1
        if s[i] in vowels:
            cur += 1
        res = max(res, cur)
        l += 1
    return res