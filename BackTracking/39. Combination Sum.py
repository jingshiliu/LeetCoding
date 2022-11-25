class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        combinationHolder = []

        def findCombination(curSum, index):
            if curSum == target:
                res.append(combinationHolder.copy())


            elif curSum < target:
                for i in range(index, len(candidates)):
                    combinationHolder.append(candidates[i])
                    findCombination(curSum + candidates[i], i)

            if len(combinationHolder):
                combinationHolder.pop()

        findCombination(0, 0)
        return res