def asteroidCollision(asteroids):
    # Time: O(n)
    # Space: O(n)
    res = []
    for aster in asteroids:
        if not res:
            res.append(aster)
            continue

        if aster > 0 or res[-1] < 0:
            res.append(aster)
        else:
            aster_size = abs(aster)
            while aster_size >= res[-1]:
                if aster_size == res[-1]:
                    res.pop()
                    break

                res.pop()

                if not res or res[-1] < 0:
                    res.append(aster)
                    break

    return res