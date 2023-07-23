import heapq


def max_score(nums1, nums2, k):
    pairs = [(nums1[i], nums2[i]) for i in range(len(nums1))]
    pairs.sort(key=lambda x: -x[1])  # sort from large to small based on the second value of the tuple(nums2)

    topk = [pairs[i][0] for i in range(k)]
    heapq.heapify(topk)
    topk_sum = sum(topk)

    res = topk_sum * pairs[k - 1][1]
    for i in range(k, len(pairs)):
        n1, n2 = pairs[i]
        topk_sum = topk_sum - topk[0] + n1
        heapq.heappop(topk)
        heapq.heappush(topk, n1)

        res = max(res, topk_sum * n2)
    return res