class SmallestInfiniteSet:

    def __init__(self):
        #
        self.add_back_set = set()  # constant lookup for the heap
        self.add_back_heap = []  # keep track the num added back that is smaller than cur_int
        # and it is guaranteed number greater than cur_int must in the set

        self.cur_int = 1  # min int that is not in heap

    def popSmallest(self) -> int:
        # worst time: O(logn for remove from heap)
        # if add_back_heap is empty: return cur_int
        # else: return heap[0]
        smallest = 0
        if not self.add_back_heap:
            smallest = self.cur_int
            self.cur_int += 1
        else:
            smallest = heapq.heappop(self.add_back_heap)
            self.add_back_set.remove(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        # O(logn) for add to heap
        # if num greater than cur_int or in add_back_set: do nothing
        # else, add to add_back_set and heap
        if num >= self.cur_int or num in self.add_back_set:
            return

        self.add_back_set.add(num)
        heapq.heappush(self.add_back_heap, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)