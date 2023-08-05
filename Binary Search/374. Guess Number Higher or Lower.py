def guess_number(n):
    l, r = 0, 2 ** 32
    while l < r:
        cur = (l + r) // 2
        guess_result = guess(cur)
        if guess_result < 0:
            r = cur
        elif guess_result > 0:
            l = cur
        else:
            return cur