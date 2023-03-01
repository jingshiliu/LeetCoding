from collections import Counter


def permuteUnique(nums):
    res, cur = [], []
    length = len(nums)
    counter = Counter(nums)

    def findPermutations():
        if len(cur) == length:
            res.append(cur.copy())
            return

        for num in counter:
            if counter[num] == 0: continue

            counter[num] -= 1

            cur.append(num)
            findPermutations()
            cur.pop()

            counter[num] += 1

    findPermutations()
    return res


# Time: O(n! n)
# Space: O(n! n)

nums = [1, 1, 2]
print(permuteUnique(nums))
