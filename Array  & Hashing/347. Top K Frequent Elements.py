class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numToCount = {}
        for i in nums:  # O(n)
            if i in numToCount:
                numToCount[i] += 1
            else:
                numToCount[i] = 1

        countToNum = [0] * (len(nums) + 1)

        for num in numToCount:  # O(unique numbers)
            count = numToCount[num]
            if countToNum[count] == 0:
                countToNum[count] = [num]
            else:
                countToNum[count].append(num)
        res = []
        for i in range(len(countToNum) - 1, 0, -1):  # O(n)
            if k == 0:
                break
            if countToNum[i] != 0:
                for num in countToNum[i]:
                    res.append(num)
                k -= len(countToNum[i])
        return res



