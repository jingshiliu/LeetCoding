import heapq
from heapq import heappop, heappush, heapify


def total_costs_2(costs, k, candidates):
    # Time: O(m + k * logm)
    # Space: O(m)
    # 2 heaps, better implementation
    # first candidates workers and last candidates workers
    # if they overlap, combine into one heap

    # O(candidates)
    head_workers = costs[:candidates]
    tail_workers = costs[max(candidates, len(costs) - candidates):]
    heapify(head_workers)
    heapify(tail_workers)

    next_head, next_tail = candidates, len(costs) - candidates
    total_cost = 0
    # O(k * 4 logm) = O(k * logm)
    # O(k)
    for _ in range(k):
        if not tail_workers or head_workers and head_workers[0] <= tail_workers[0]:
            # O(logm)
            total_cost += heappop(head_workers)

            if next_head < next_tail:
                # O(logm)
                heappush(head_workers, costs[next_head])
                next_head += 1
        else:
            # O(logm)
            total_cost += heappop(tail_workers)

            if next_head < next_tail:
                next_tail -= 1
                # O(logm)
                heappush(tail_workers, costs[next_tail])

    return total_cost

def total_costs_1(costs, k, candidates):
    # 2 heaps
    # first candidates workers and last candidates workers
    # if they overlap, combine into one heap
    first_c_workers = [(costs[i], i) for i in range(candidates)]
    last_c_workers = [(costs[i], i) for i in range(len(costs) - candidates, len(costs))]
    heapq.heapify(first_c_workers)
    heapq.heapify(last_c_workers)

    l, r = candidates, len(costs) - candidates
    total_cost = 0
    had_combined_heaps = False
    for hiring_session in range(k):

        if not had_combined_heaps and not l < r:
            for cost, index in last_c_workers:
                if index < l:
                    continue
                heapq.heappush(first_c_workers, (cost, index))
            had_combined_heaps = True

        if had_combined_heaps:
            total_cost += heapq.heappop(first_c_workers)[0]
        else:
            first_cost, first_index = first_c_workers[0]
            last_cost, last_index = last_c_workers[0]
            if first_cost <= last_cost:
                total_cost += first_cost
                heapq.heapreplace(first_c_workers, (costs[l], l))
                l += 1
            else:
                total_cost += last_cost
                r -= 1
                heapq.heapreplace(last_c_workers, (costs[r], r))

    return total_cost