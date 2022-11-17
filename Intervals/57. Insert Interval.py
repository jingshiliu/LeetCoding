def insert(intervals, newInterval):
    if not intervals:
        return [newInterval]
    if newInterval[0] > intervals[-1][1]:
        intervals.append(newInterval)
        return intervals
    res = [[-1, -1]]
    if newInterval[1] <= intervals[0][0] or newInterval[0] < intervals[0][0]:
        res.append(newInterval)

    newAppended = False
    for i in range(len(intervals)):
        curInterval = intervals[i]
        if not newAppended and newInterval[1] < curInterval[0] and newInterval[0] > res[-1][1]:
            newAppended = True
            res.append(newInterval)
        if curInterval[0] <= res[-1][1]:
            res[-1][1] = max(curInterval[1], res[-1][1])
            continue

        if newInterval[0] <= curInterval[1]:
            curInterval[1] = max(curInterval[1], newInterval[1])
            if newInterval[0] < curInterval[0] < newInterval[1]:
                curInterval[0] = min(curInterval[0], newInterval[0])
        res.append(curInterval)

    return res[1:]


# Solution 2

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        res = [[-1, -1]]
        i = 0
        newIsInserted = False
        while i < len(intervals):
            cur = intervals[i]

            if not newIsInserted and newInterval[0] <= cur[0]:
                cur = newInterval
                newIsInserted = True
            else:
                i += 1

            prev = res[-1]

            if prev[1] >= cur[0]:
                prev[1] = max(prev[1], cur[1])
            else:
                res.append(cur)

        if len(res) == len(intervals) + 1:
            prev = res[-1]
            if prev[1] >= newInterval[0]:
                prev[1] = max(prev[1], newInterval[1])
            else:
                res.append(newInterval)

        return res[1:]


intervals = [[1,5]]

newInterval = [0,0]

print(insert(intervals, newInterval))
