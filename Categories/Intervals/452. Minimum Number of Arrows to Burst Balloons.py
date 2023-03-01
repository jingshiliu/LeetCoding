class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # aim is to find number of non overlapping intervals
        # if 2 intervals overlap, it's possible to shot once and both explode
        # therefore, any set of overlapping intervals that overlap in a common interval can be shot by one arrow
        # we just find max number intervals non overlapping

        res = 1
        points.sort()
        start = points[-1][0]
        for i in range(len(points) - 2, -1, -1):
            if points[i][1] < start:
                res += 1
                start = points[i][0]

        return res