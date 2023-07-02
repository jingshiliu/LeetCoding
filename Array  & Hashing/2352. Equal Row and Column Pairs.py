def equal_pairs(grid):
    COLS, ROWS = len(grid[0]), len(grid)
    row_nums = {}
    col_nums = {}

    cur = []
    for r in range(ROWS):
        cur = []
        for c in range(COLS):
            cur.append(str(grid[r][c]))
        row_nums[''.join(cur)] = r

    print(row_nums)

