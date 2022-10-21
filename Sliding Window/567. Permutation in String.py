from collections import defaultdict


def checkInclusion(s1, s2):  # O(len(s2))
    if len(s1) > len(s2):
        return False

    count = defaultdict(int)
    for c in s1:  # O(len(s1))
        count[c] += 1

    need = len(count)
    had = defaultdict(int)
    l = 0
    for r in range(len(s1)):  # O(len(s1))
        if s2[r] in count:
            had[s2[r]] += 1
            if had[s2[r]] == count[s2[r]]:
                need -= 1

    for r in range(len(s1), len(s2)):   # O(len(s2))
        if need == 0:
            return True

        if s2[r] in count:
            had[s2[r]] += 1
            if had[s2[r]] == count[s2[r]]:
                need -= 1
        if s2[l] in count:
            if had[s2[l]] == count[s2[l]]:
                need += 1
            had[s2[l]] -= 1

        l += 1

    return need == 0


s1 = "abc"
s2 = "ccccbbbbaaaa"

s1 = "trinitrophenylmethylnitramine"
s2 = "dinitrophenylhydrazinetrinitrophenylmethylnitramine"
print(checkInclusion(s1, s2))
