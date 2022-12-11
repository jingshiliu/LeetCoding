class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        cur = []

        def findSubset(index):

            res.append(cur.copy())

            prev = index + 1
            if prev < len(nums):
                cur.append(nums[prev])
                findSubset(prev)
                cur.pop()

            for i in range(index + 2, len(nums)):
                if nums[i] == nums[prev]:
                    continue
                cur.append(nums[i])
                findSubset(i)
                cur.pop()

                prev = i

        findSubset(-1)
        return res