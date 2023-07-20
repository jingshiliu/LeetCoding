def orange_rotting(grid):
    # doing bfs for each of the NEWLY rotten tomatoes, bc old one had rotten all the adjacent tomamtoes
    # record the amount of rotten tomamtoes in each round
    # if the amount is same as the last round's
    # meaning no tomamto is been rotten this round and no more tomamtoes can be rotten

    fresh_orange, HEIGHT, WIDTH = 0, len(grid), len(grid[0])
    ADJ_INDEXES = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    queue, next_queue = [], []
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if grid[i][j] == 1:
                fresh_orange += 1
            elif grid[i][j] == 2:
                for x, y in ADJ_INDEXES:
                    queue.append((i + x, j + y))

    last_round_count, rounds_count = 0, -1
    while not last_round_count == fresh_orange:
        rounds_count += 1
        last_round_count = fresh_orange
        for i, j in queue:
            if i < 0 or i == HEIGHT or j < 0 or j == WIDTH or not grid[i][j] == 1:
                continue
            fresh_orange -= 1
            grid[i][j] = 2
            for x, y in ADJ_INDEXES:
                next_queue.append((i + x, j + y))
        queue, next_queue = next_queue, []

    if rounds_count == -1:
        return 0
    return rounds_count if fresh_orange == 0 else -1