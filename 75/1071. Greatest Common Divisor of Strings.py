def gcdOfStrings(str1: str, str2: str) -> str:
    # O(m + n)
    if str1 + str2 != str2 + str1:
        return ""

    max_length = gcd(len(str1), len(str2))
    return str1[:max_length]


def gcdOfStrings2( str1: str, str2: str) -> str:
    # O(|CD| * (M + N)
    # iterate 2 str at the same time
    # if find a char that is not in other str, then there is no solution

    # find common divisor of the length
    # 6, 4.  common divisor: 1, 2
    # str1 = "ABABAB", str2 = "ABAB"
    # then find the common divisor candidates of string
    # A, AB

    n1, n2 = len(str1), len(str2)
    candidates = []
    for i in range(min(n1, n2), 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            candidates.append(str1[:i])

    for candidate in candidates:
        i = 0
        len_candidate = len(candidate)
        is_invalid = False
        while i < max(n1, n2):
            for j in range(len_candidate):
                if i < n1 and str1[i] != candidate[j] or i < n2 and str2[i] != candidate[j]:
                    is_invalid = True
                    break
                i += 1
            if is_invalid: break

        if is_invalid:
            break
        return candidate
    return ""