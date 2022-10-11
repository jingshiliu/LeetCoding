def largestRectangleArea(heights) -> int:
    stack = [[0, -1]]  # . [height, index]
    res = 0

    for i, h in enumerate(heights): # O(n)
        start = i
        while h < stack[-1][0]: # O(n)
            res = max(res, stack[-1][0] * (i - stack[-1][1]))  # Extend height *  Extend length (curIndex - beginIndex)
            start = stack[-1][1]  # If prev height is higher than current height, we can extend from prev height
            stack.pop()
        if not h == stack[-1][0]:
            stack.append([h, start])
        print(f'res: {res}       i: {i}  h: {h}          stack: {stack}')

    # O(n)
    while len(stack) > 1:  # Some may extend all the way to end
        res = max(res, stack[-1][0] * (len(heights) - stack[-1][1]))
        stack.pop()

    return res


input = [3,6,5,7,4,8,1,0]
print(largestRectangleArea(input))


