import heapq


class MedianFinder:

    def __init__(self):
        # Space: o(n)
        # Time: O(logn) for addNum, O(1) for findMedian
        # idea
        # use two heaps where the top of two heaps are median
        self.small = []  # maxHeap
        self.large = []  # minHeap

    def addNum(self, num: int) -> None:
        # k, k -> k + 1, k -> k, k + 1
        # k, k + 1 -> k, k + 2 -> k + 1, k + 1
        # the goal is to make them have same length
        # but if we add 1 to large heap when median is 5, large heap is not valid
        # that's why we need to pop the smallest from Large, and push it to Small
        # so that the heap of two heaps will always be median
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self) -> float:
        # same length means even length
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        return self.large[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()