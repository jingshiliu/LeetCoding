def nearest_exit_distance(maze: list[list[str]], entrance: list[int]) -> int:
    # BFS
    # Time: O(n) n is the total length of path
    # Space: O(n) queue and visited set()
    HEIGHT, WIDTH, RIGHT_BOUNDARY, BOTTOM_BOUNDARY = len(maze), len(maze[0]), len(maze[0]) - 1, len(maze) - 1
    entrance_index = tuple(entrance)
    queue, next_queue = [entrance_index], []
    steps = -1
    visited = set()
    while queue:
        steps += 1
        for index in queue:
            x, y = index
            if index in visited or x < 0 or x == HEIGHT or y < 0 or y == WIDTH or maze[x][y] == '+':
                continue
            visited.add(index)
            if index != entrance_index and (x == 0 or y == 0 or x == BOTTOM_BOUNDARY or y == RIGHT_BOUNDARY):
                return steps

            next_queue.append((x - 1, y))
            next_queue.append((x + 1, y))
            next_queue.append((x, y - 1))
            next_queue.append((x, y + 1))

        queue, next_queue = next_queue, []

    return -1