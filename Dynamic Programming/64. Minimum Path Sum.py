def minPathSum(grid) -> int:
    m, n = len(grid), len(grid[0])
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for r in range(1, m + 1):
        for c in range(1, n + 1):

            if r - 1 == 0 or c - 1 == 0:
                min_path_cost = max(dp[r - 1][c], dp[r][c - 1])
            else:
                min_path_cost = min(dp[r - 1][c], dp[r][c - 1])
            dp[r][c] = min_path_cost + grid[r - 1][c - 1]

    return dp[-1][-1]
