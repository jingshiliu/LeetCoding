def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    res = []
    q = deque()

    l = -1
    r = 0

    while r < k:  # O(k)
        while q and nums[r] > q[-1][0]:
            q.pop()
        q.append((nums[r], r))  # (num, index)
        r += 1
    res.append(q[0][0])

    # Our queue can have max of k items and only store the nums in curWindow
    # If curVal larger than the one before, pop the before
    # because curVal is larger, they wont be max since they are less than curVal
    # The first item in queue is always the max since we apply the above algo
    # If first item is out the left window bound, we pop it, and the one small than first item will be max
    while r < len(nums):  # O(n - k)
        while q and nums[r] > q[-1][0]:  # O(k)
            q.pop()
        q.append((nums[r], r))

        l += 1
        if l == q[0][1]:
            q.popleft()
        res.append(q[0][0])
        r += 1

    return res  # O(n)