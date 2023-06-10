class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        nonOverlapping = 1

        # count from end to begin
        start = intervals[-1][0]

        for i in range(len(intervals) - 2, -1, -1):
            if intervals[i][1] <= start:
                nonOverlapping += 1
                start = intervals[i][0]

        return len(intervals) - nonOverlapping
