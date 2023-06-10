def searchRange(nums, target: int):
    """
    Find a target first use binSearch
    Then do binSearch on left of targetIndex, check if nums[index  -1] != target
    Vice versa on right side
    """
    if not nums: return [-1, -1]

    def binSearch(l=0, r=len(nums)-1, tgt=target):
        while l <= r:
            mid = (l + r) // 2
            cur = nums[mid]
            if cur == tgt:
                return mid
            elif cur < tgt:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    targetIndex = binSearch()
    if targetIndex == -1: return [-1, -1]

    first, last = targetIndex, targetIndex
    while first != 0 and nums[first - 1] == target:
        first = binSearch(r=first-1)

    while last != len(nums) - 1 and nums[last + 1] == target:
        last = binSearch(l=last+1)
    return [first, last]


nums = [2, 2]
target = 2
print(searchRange(nums, target))
