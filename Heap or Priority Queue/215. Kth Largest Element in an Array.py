def findKthLargest(nums: list[int], k: int) -> int:
    k = len(nums) - k
    l, r = 0, len(nums) - 1
    while True:
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1

        nums[p], nums[r] = nums[r], nums[p]
        if p < k:
            l = p + 1
        elif p > k:
            r = p - 1
        else:
            return nums[p]


nums = [2, 1]
k = 1
print(findKthLargest(nums, k))