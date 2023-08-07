def frequency_sort(s):
    s_list = [c for c in s]
    s_list.sort()

    char_list = []
    l = 0
    for r in range(len(s)):
        if s_list[r] != s_list[l]:
            char_list.append(''.join([s_list[i] for i in range(l, r)]))
            l = r
    char_list.append(''.join([s_list[i] for i in range(l, len(s))]))
    char_list.sort(key=lambda x: -1 * len(x))
    return ''.join(char_list)