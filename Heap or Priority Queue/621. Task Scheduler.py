from collections import deque
import heapq


def leastInterval(tasks, n: int) -> int:
    # Time: O(n)
    # Space: O(1) bc countTask at most have length of 26 which is the number of capital letters
    countTask = {}
    for i in tasks:  # O(n)
        countTask[i] = countTask.get(i, 0) + 1

    # slot size * slots that can be filled full + last slot (not full, only maxFreq can be put in this one)
    # (n + 1) * (maxFreq - 1) + countFreq
    maxFreq = 0

    for task in countTask.keys():  # O(1), since len(countTask) will never exceed 26 which is the number of capital letters
        maxFreq = max(countTask[task], maxFreq)

    countMaxFreq = 0
    for task in countTask.keys():  # O(1)
        if countTask[task] == maxFreq:
            countMaxFreq += 1

    # You may wonder, what if we have something like {A:8, B:7, C:7, D:7, E:7, F:7} n = 2
    # which will exceed the capacity of 'slot'
    # However, do we really 'slot' in this case? We used 'slot' because there are some need to be filled 'idle'
    # In this case, there will be no idle, and there will have some permutation such that it will work
    return max(len(tasks), (n + 1) * (maxFreq - 1) + countMaxFreq)


def leastInterval2(tasks, n: int) -> int:
    if n == 0:
        return len(tasks)
    # strategy: use the one that has highest frequency
    # higher freq, higher priority
    queue = deque([[0]] * n)  # stores the Letter used that can be used again

    # count freq
    letterToFreq = {}
    for i in tasks:
        letterToFreq[i] = letterToFreq.get(i, 0) + 1

    # create a list of [freq, letter] and heapify
    heap = [[-1 * letterToFreq[key], key] for key in letterToFreq]
    heapq.heapify(heap)
    res = 0
    isUnfinished = len(tasks)
    # then while heap, push the head of queue, and pop the heap, and append to queue,
    while isUnfinished:
        res += 1
        cur = heapq.heappop(heap)
        heapq.heappush(heap, queue.popleft())
        if cur[0]:
            cur[0] += 1
            isUnfinished -= 1
        queue.append(cur)
    return res


tasks = ["A","A","A","B","B","B"]
n = 0
print(leastInterval(tasks, n))


