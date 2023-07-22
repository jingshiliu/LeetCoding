import heapq


class SmallestInfiniteSet:

    def __init__(self):
        # Assume M is calls to popSmallest, n is calls to addBack
        # each take O(logn) because addBack which is n calls determines the size of heap
        # Time: O((m + n)logn)
        # Space: O(n) for the space taken by set and heap, each determined by number of addBack calls
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


class SmallestInfiniteSetBruteForce:

    def __init__(self):
        # M calls for popSmallest, N calls for addBack
        # Time: O(m2 + n) for M calls to O(m) popSmallest and N calls to O(1) addBack
        # Space: worst O(m) we might add m numbers to set
        self.removed_set = set()
        self.removed_heap = []
        self.cur_min = 1

    def popSmallest(self) -> int:
        # Time: O(m) for find new cur_min takes up to m ops
        # Space for removed_set is O(m)
        # removed_set
        # if removed_set is empty, we return the cur_min and add cur_min to removed
        # find new cur_min: while cur_min in removed_set: cur_min++
        # why cur_min + 1 might not be the smallest
        # bc we can removed num from 1 - 10 and add 1 back
        smallest = self.cur_min
        self.removed_set.add(smallest)
        while self.cur_min in self.removed_set:
            self.cur_min += 1
        return smallest

    def addBack(self, num: int) -> None:
        # O(1)
        # check if num in removed_set
        # yes, add back, and cur_min = min(num, cur_min)
        # no, do nothing
        if num < 1 or num not in self.removed_set:
            return

        self.cur_min = min(num, self.cur_min)
        self.removed_set.remove(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)