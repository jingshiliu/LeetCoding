def trap(height) -> int:
    res, l, r = 0, 0, len(height) - 1
    maxL, maxR = 0, 0
    while l <= r:
        if maxL <= maxR:
            maxL = max(maxL, height[l])
            res += maxL - height[l]
            l += 1
        else:
            maxR = max(maxR, height[r])
            res += maxR - height[r]
            r -= 1

    return res


height = [4,2,0,3,2,5]
print(trap(height))