import math


def minEatingSpeed(piles: list[int], h: int) -> int:
    # l is 1 bc speed min is 1
    # r is max(piles) bc Koko can eat n piles in n time(which is the min time possible) with this speed
    l, r = 1, max(piles)  # O(n)

    # Approach, bin search
    # from l to r, there are some speed that it is guaranteed Koko can finish on time and some cannot
    # if Koko can finish in N time, it is guaranteed to finish in N + 1
    # if Koko cannot finish in N time, it cannot finish in N - 1
    # The goal is to find the RES that separates time that can do and cannot do

    while l < r:    # O(log r)
        cur = (l + r) // 2
        # we take the middle and check if Koko can finish the pile with this speed
        timeTake = 0
        for i in piles:  # O(n)
            timeTake += math.ceil(i / cur)

        # if takes longer than h, means cannot finish on time
        if timeTake > h:
            l = cur + 1
        else:
            r = cur

    return r    # O(n log r)


piles = [30,11,23,4,20]
h = 5
print(minEatingSpeed(piles, h))