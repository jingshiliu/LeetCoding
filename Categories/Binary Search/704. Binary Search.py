def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)

    # When picking r
    # make sure if r is included in the bound or not included
    # have to be consistent
    while l < r:
        cur = floor((l + r) / 2)
        if nums[cur] == target:
            return cur

        if nums[cur] > target:
            r = cur
        else:
            l = cur + 1

    return -1