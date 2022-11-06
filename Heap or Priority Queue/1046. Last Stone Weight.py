class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Overall: O(nlogn)
        heap = [-1 * i for i in stones]
        heapq.heapify(heap)
        while len(heap) > 1:  # O(n)
            # O(logn) * 3
            s1, s2 = heapq.heappop(heap), heapq.heappop(heap)
            if s1 < s2:
                heapq.heappush(heap, s1 - s2)
        return -1 * heap[0] if heap else 0
