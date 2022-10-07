def findMin(nums: list[int]) -> int:
    l, r = 0, len(nums) - 1

    while l < r:
        if nums[l] < nums[r]:
            return nums[l]
        if r - l == 1:
            return min(nums[l], nums[r])

        mid = l + (r - l) // 2
        if nums[mid] > nums[l]:
            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
        else:
            r = mid

    print(f'{l} {r}')

inputs = [
[3,4,5,1,2],
[4,5,6,7,0,1,2],
[11,13,15,17],
]


for nums in inputs:
    print(f'{findMin(nums)}        {nums}')