def uniquePathsWithObstacles(obstacleGrid) -> int:
    if obstacleGrid[0][0] == 1: return 0
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * n for i in range(m)]
    dp[0][0] = 1

    for r in range(m):
        for c in range(n):
            if obstacleGrid[r][c] or dp[r][c]: continue
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

    return dp[-1][-1]