def countAndSay(n: int) -> str:
    def generateSequence(prevSeq):
        cur, curCount = prevSeq[0], 0
        res = []
        for c in prevSeq:
            if c == cur:
                curCount += 1
            else:
                res.append(str(curCount))
                res.append(cur)
                cur, curCount = c, 1
        res.append(str(curCount))
        res.append(cur)
        return ''.join(res)

    curSeq = "1"
    for i in range(1, n):
        curSeq = generateSequence(curSeq)
    return curSeq

n = 4
print(countAndSay(n))
