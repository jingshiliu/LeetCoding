def find_kth_largest(nums:list[int], k: int) -> int:
    # pivot
    # performing quick select
    # then swap pivot and left
    # if pivot index is k, then return
    # else do quick select again for either left or right side of pivot

    # Time: O(n) average case N + N/2 + N/4 ... = 2N = O(n)
    #       O(n2) worst case where pivot is always the smallest, we have to do quick select n times with each cost N
    # Space: O(1) as we do in place swap

    K_INDEX = len(nums) - k
    L, R = 0, len(nums) - 1
    while True:
        pivot, l, r = L, L, R

        while l < r:
            while l < r and nums[r] >= nums[pivot]:
                r -= 1
            while l < r and nums[l] <= nums[pivot]:
                l += 1

            nums[l], nums[r] = nums[r], nums[l]

        nums[l], nums[pivot] = nums[pivot], nums[l]
        if l < K_INDEX:
            L = l + 1
        elif l > K_INDEX:
            R = l - 1
        else:
            return nums[l]


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