def singleNonDuplicate(nums) -> int:
    # bin search
    # check if mid is the single
    # otherwise,
    # mid is even
    # if mid - 1 = mid, means in left half
    # otherwise in right half
    # mid is odd
    # if mid - 1 = mid, means in right half
    left, right = 0, len(nums) - 1

    while left < right:

        mid = (right + left) // 2
        cur = nums[mid]
        left_cur = nums[mid - 1]

        if cur != left_cur and cur != nums[mid + 1]:

            return cur
        elif mid % 2 == 0:
            if left_cur == cur:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if left_cur == cur:
                left = mid + 1
            else:
                right = mid - 1

    return nums[left]


nums = [3,3,7,7,10,11,11]
print(singleNonDuplicate(nums))