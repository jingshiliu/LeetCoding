def threeSumClosest(self, nums, target: int) -> int:
    nums.sort()  # nlogn
    res = 1000000
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]: continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            theSum = nums[l] + nums[r] + nums[i]
            diff = target - theSum
            if abs(diff) < abs(res - target):
                res = theSum

            if diff > 0:  # meaning theSum is smaller than target we want to be closer by l += 1
                l += 1
            elif diff < 0:
                r -= 1
            else:
                return target
    return res
