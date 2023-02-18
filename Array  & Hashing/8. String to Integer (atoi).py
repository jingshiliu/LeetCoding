def myAtoi(s: str) -> int:
    maxNum = 2 ** 31 - 1
    minNum = -1 * 2 ** 31
    sign = 1
    number = 0

    for i in range(len(s)):
        if s[i] == ' ':
            continue
        elif s[i] == '-':
            sign = -1
        elif s[i] == '+':
            pass
        elif not s[i].isnumeric():
            break

        i += 1 if not s[i].isnumeric() else 0
        while i < len(s) and s[i].isnumeric():
            number = number * 10 + int(s[i])
            i += 1

        break
    number *= sign
    if number < minNum:
        return minNum
    if number > maxNum:
        return maxNum
    return number
