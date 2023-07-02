from collections import defaultdict


def equalPairs( grid) -> int:
    # Time: O(n2)
    # Space: O(n2)
    N = len(grid)
    row_pairs = defaultdict(lambda: 0)
    res = 0

    for r in range(N):
        row_pairs[tuple(grid[r])] += 1

    for c in range(N):
        col_pair = tuple([grid[r][c] for r in range(N)])
        res += row_pairs[col_pair]

    return res


def equal_pairs2(grid):
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

