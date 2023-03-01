def nextPermutation(nums) -> None:
    def reverseList(l, r=len(nums) - 1):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

    findNext = False
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            for j in range(len(nums) - 1, i, -1):
                if nums[j] > nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]

                    reverseList(i + 1)
                    findNext = True
                    break
            break

    if not findNext:
        reverseList(0)