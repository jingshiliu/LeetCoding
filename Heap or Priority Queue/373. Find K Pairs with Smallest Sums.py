from heapq import heappop, heappush


def k_smallest_pairs(nums1, nums2, k):
    # Time: O(klogk) or O(m*n logm*n) the min of them
    # Space: O(min(k, m*n)
    # 100 200 300 400
    # 500 600 601 602
    # 00, next will either be 10 or 01
    # in other word, if cur min pair is [i, j], the next min pair is either the leftover from previous pairs
    # or [i+1, j] or [i, j+1]

    res, heap = [], [[nums1[0] + nums2[0], 0, 0]]
    N1, N2 = len(nums1), len(nums2)
    visited = set()

    while len(res) < k and heap:
        # logk
        val, index1, index2 = heappop(heap)
        if (index1, index2) in visited:
            continue
        visited.add((index1, index2))
        res.append([nums1[index1], nums2[index2]])

        # will put 2k pairs into the heap at most
        # logk
        if index2 + 1 < N2:
            heappush(heap, [nums1[index1] + nums2[index2 + 1], index1, index2 + 1])
        # logk
        if index1 + 1 < N1:
            heappush(heap, [nums1[index1 + 1] + nums2[index2], index1 + 1, index2])

    return res