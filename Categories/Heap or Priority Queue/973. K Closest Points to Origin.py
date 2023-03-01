import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Overall Time: max(O(n), O(klogn)) = O(nlogn)
        # put distance in heap  O(n)
        # and then pop while res.length < k O(klogn)
        # however, sorting a list of lists will make them sort base on the first element, therefore, we can [dist, point]
        distToPoints = {}
        heap = []
        for point in points:
            # actual distance need to apply a sqrt to it
            distance = point[0] ** 2 + point[1] ** 2
            heap.append([distance, point])

        heapq.heapify(heap)

        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])

        return res

    def kClosest1(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Overall Time: max(O(n), O(klogn))
        # put distance in heap  O(n)
        # and then pop while res.length < k O(klogn)
        # hashtable: key is distance, val is a list of points
        distToPoints = {}
        heap = []
        for point in points:
            # actual distance need to apply a sqrt to it
            distance = point[0] ** 2 + point[1] ** 2
            heap.append(distance)
            if distance in distToPoints:
                distToPoints[distance].append(point)
            else:
                distToPoints[distance] = [point]
        heapq.heapify(heap)

        res = []
        while len(res) < k:
            distance = heapq.heappop(heap)
            for i in distToPoints[distance]:
                res.append(i)

        return res

