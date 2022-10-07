import math


def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = int((l + r) / 2)
        if nums[mid] == target:
            return mid
        if nums[r] > nums[l]:
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        elif nums[mid] > nums[l] and nums[l] <= target and nums[mid] > target:
            r = mid - 1
        elif nums[mid] < nums[l] and (target >= nums[l] or target < nums[mid]):
            r = mid - 1
        else:
            l = mid + 1

    return -1

nums = [4,5,6,7,8,1,2,3]
target = 8

print(search(nums, target))