def maxArea(height) -> int:
    """
    want container be as wide as possible
    therefore we use left, and right pointers that point to 0, and len(height)-1

    then we calculate the volume of container

    then we want to find if there is a new container that can hold more water
    we want to keep the side that is higher
    also, when we find new side, the width of container is shrinking, meaning it is impossible for new container
    to holder more water if the new side is not higher than the new side
    """

    l, r = 0, len(height) - 1
    res = 0
    while l < r:
        res = max(res, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            cur = height[l]
            while l < r and height[l] <= cur:
                l += 1
        else:
            cur = height[r]
            while l < r and height[r] <= cur:
                r -= 1
    return res