def encode(strs) -> str:
    """Encodes a list of strings to a single string.
    """
    encode = []
    for s in strs:  # O(n)
        length = str(len(s))
        while len(length) < 3:  # Overall O(1)
            length = '0' + length
        encode.append(length + s)  # O(1)

        # It can also be solved this way, but everytime we do 'encode += length + s'
    # A new string is created with Time Complexity O(n), and the overall will be O(n2)
    # In contrast, ''.join() only have O(n)
    '''
    encode = ''
    for s in strs:
        length = str(len(s))
        while len(length) < 3:
            length = '0' + length
        encode += length + s
    '''
    return ''.join(encode)   # O(n)


def decode(s: str) -> list[str]:
    """Decodes a single string to a list of strings.
    """
    decode = []
    i = 0
    while i < len(s):  # O(n)
        length = int(s[i:i + 3])  # O(k)
        i += 3
        decode.append(s[i: i + length])     # O(k)
        i += length
    return decode
