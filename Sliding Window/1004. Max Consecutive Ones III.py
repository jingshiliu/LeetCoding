def longestOnes(nums, k: int) -> int:
    """
    Time O(n)
    Space O(1)
    """
    res = 0
    cur_zero = 0
    l = 0

    for r in range(len(nums)):
        if nums[r] == 0:
            cur_zero += 1

        while cur_zero > k:
            if nums[l] == 0:
                cur_zero -= 1
            l += 1

        res = max(res, r - l + 1)
    return res