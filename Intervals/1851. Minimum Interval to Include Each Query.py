class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # use a priority queue which stores all the intervals that current query is in

        heap = []
        res = {}
        intervals.sort()

        i = 0
        for query in sorted(queries):
            while i < len(intervals) and query >= intervals[i][0]:
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1

            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            res[query] = heap[0][0] if heap else -1

        return [res[q] for q in queries]
