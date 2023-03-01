def permute(nums):
    res = []

    nonVisited = set(nums.copy())
    cur = []

    def findPermutation():  # O(n!)
        if len(cur) == len(nums):  # O(1)
            res.append(cur.copy())
        for num in tuple(nonVisited):  # n
            cur.append(num)
            nonVisited.remove(num)

            findPermutation()  # n - 1     *     n - 2      *  n - 3 ... * 1

            cur.pop()
            nonVisited.add(num)

    findPermutation()
    return res