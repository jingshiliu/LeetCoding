def threeSum(nums):
    nums.sort()  # O(nlogn)
    answer = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            ans = nums[i] + nums[l] + nums[r]
            if ans == 0:
                answer.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l + 1] == nums[l]:
                    l += 1
                l += 1
            elif ans > 0:
                r -= 1
            else:
                l += 1

    return answer
