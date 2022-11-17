class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        i = 1
        while i < len(intervals):
            prev = res[-1]
            cur = intervals[i]

            if cur[0] <= prev[1]:
                prev[1] = max(prev[1], cur[1])
            else:
                res.append(cur)

            i += 1

        return res