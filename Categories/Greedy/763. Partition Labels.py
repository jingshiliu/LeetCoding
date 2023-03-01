# def partitionLabels(s: str):
#     leftMost = {}
#     rightMost = {}
#     for i, c in enumerate(s):
#         if c not in leftMost:
#             leftMost[c] = i
#             rightMost[c] = i
#         else:
#             rightMost[c] = i
#
#     l = 0
#     res = []
#     while l < len(s):
#         c = s[l]
#         r = rightMost[s[l]] + 1
#
#         i = l
#         while i < r:
#             char = s[i]
#             if rightMost[s[i]] + 1 > r:
#                 r = rightMost[s[i]] + 1
#             i += 1
#         res.append(r - l)
#         l = r
#
#     return res

# same idea but a better implementation using greedy method

def partitionLabels( s: str) :
    rightMost = {s[i]: i for i in range(len(s))}

    i, r = 0, 0
    curLen = 0
    res = []
    while i < len(s):
        r = max(rightMost[s[i]], r)
        curLen += 1

        if i == r:
            res.append(curLen)
            curLen = 0
        i += 1

    return res






input = "qiejxqfnqceocmy"
print(partitionLabels(input))
