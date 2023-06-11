from collections import defaultdict

def max_operations_two_pointers(nums, k: int) -> int:
    # Time: O(nlogn)
    # Space: O(1)
    nums.sort()
    l, r = 0, len(nums) - 1

    res = 0
    while l < r:
        _sum = nums[l] + nums[r]
        if _sum > k:
            r -= 1
        elif _sum < k:
            l += 1
        else:
            res += 1
            r -= 1
            l += 1
    return res

def max_operations_hashmap(nums) -> int:
    """
    Time: O(n + |unique num|)
    Space: O(|unique num|)
    """
    nums_dict = defaultdict(lambda: 0)
    for n in nums:
        nums_dict[n] += 1

    res = 0
    for num in list(nums_dict.keys()):
        diff = k - num
        if nums_dict[diff] != 0:
            ops = 0
            if diff == num:
                ops = nums_dict[num] // 2
            else:
                ops = min(nums_dict[diff], nums_dict[num])
            res += ops
            nums_dict[diff] -= ops
            nums_dict[num] -= ops
    return res