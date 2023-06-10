def compress(chars) -> int:
    if len(chars) == 1:
        return 1
    cur_count = 1
    cur_index = 0

    def add_to_chars():
        nonlocal cur_index
        for c in str(cur_count):
            chars[cur_index] = c
            cur_index += 1

    for i in range(1, len(chars)):
        if chars[i] == chars[cur_index]:
            cur_count += 1
        else:
            cur_index += 1
            if cur_count > 1:
                add_to_chars()
            chars[cur_index] = chars[i]
            cur_count = 1

    cur_index += 1
    if cur_count > 1:
        add_to_chars()
    return cur_index