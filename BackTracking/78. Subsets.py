def subsets(nums):
    # Time: O(|res|)
    # Space: O(|nums|)
    res = [[]]
    subset = []

    def findSubset(index):

        if index == len(nums):
            return

        subset.append(nums[index])
        res.append(subset.copy())
        for i in range(index + 1, len(nums)):
            findSubset(i)

        subset.pop()

    for i in range(len(nums)):
        findSubset(i)
    return res

