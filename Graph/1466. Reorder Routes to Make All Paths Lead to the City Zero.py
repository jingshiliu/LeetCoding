from collections import defaultdict


def min_reorder(n: int, connections: list[list[int]]) -> int:
    # impossible to have a circle since it requires N roads
    # do bfs, centered from 0
    # if the road not directed to 0, change it
    # problem: need to create a hashmap (city: [roads])
    # Space: O(N)
    # Time: O(N) since doing bfs and visit each node exact once

    city_roads = defaultdict(lambda: [])
    for road in connections:
        city_roads[road[0]].append(road)
        city_roads[road[1]].append(road)

    cur_direction, next_direction = {0}, set()
    visited = [False] * n
    res = 0
    while cur_direction:
        for cur in cur_direction:

            roads = city_roads[cur]
            for road in roads:
                a, b = road
                if visited[a] or visited[b]:
                    continue

                if b not in cur_direction:
                    res += 1
                    next_direction.add(b)
                else:
                    next_direction.add(a)

            visited[cur] = True

        cur_direction, next_direction = next_direction, set()

    return res