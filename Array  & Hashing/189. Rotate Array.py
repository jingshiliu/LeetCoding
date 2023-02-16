def rotate(nums, k: int) -> None:
    k = k % len(nums)

    def reverseList(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverseList(0, len(nums) - 1)
    reverseList(0, k - 1)
    reverseList(k, len(nums) - 1)


