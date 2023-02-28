def uniquePaths(m: int, n: int) -> int:
    ans = [[0] * (n + 1)] * (m + 1)
    ans[1][1] = 1

    for r in range(1, m + 1):
        for c in range(1, n + 1):
            if r == 1 and c == 1: continue
            ans[r][c] = ans[r - 1][c] + ans[r][c - 1]

    return ans[m][n]
