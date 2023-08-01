from heapq import heapify, heappop, heappush


def kth_smallest(matrix, k):
    # Time: O(n + klogn), let x = min(k, n)
    # Space: O(n)
    # store the first number in each row in a heap
    # the first time popping it, is the smallest, and we add the next number on that row to the heap
    # then the second smallest is among one of them
    # we do this k times, and get answer
    N = len(matrix)
    heap = [[matrix[i][0], i, 0] for i in range(N)]
    heapify(heap)

    while True:
        number, row, col = heappop(heap)
        k -= 1
        if k == 0:
            return number
        if col + 1 < N:
            heappush(heap, [matrix[row][col + 1], row, col + 1])