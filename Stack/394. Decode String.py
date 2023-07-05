def decodeString(s: str) -> str:
    # num [string]
    # after num, must be string

    # initialize stack like this to generalize all the steps
    # once detect a number, meaning a [encoded_string] follows
    # so append [k, encoded_string] on stack
    # bc this is when the recursion happens

    # when detect a ']', meaning the encoded_string has been read, and we can pop the stack
    stack = [[['0'], []]]

    k, encoded_string = stack[-1]
    is_reading_num = False

    for c in s:
        if c == ']':
            repeat_times = int(''.join(k))
            encoded_str = ''.join(encoded_string)
            decoded_string = encoded_str * repeat_times
            stack.pop()

            k, encoded_string = stack[-1]
            encoded_string.append(decoded_string)
            continue
        if c == '[':
            is_reading_num = False
            continue

        if is_reading_num:
            k.append(c)
        elif c.isnumeric():
            is_reading_num = True
            stack.append([[c], []])
            k, encoded_string = stack[-1]
        else:
            encoded_string.append(c)

    return ''.join(stack[0][1])

print(decodeString('3[a]2[bc]'))
