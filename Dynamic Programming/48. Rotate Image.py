def rotate(matrix) -> None:
    ROWS, COLS = len(matrix), len(matrix[0])

    def getRotateIndexes(r, c):
        return [
            [c, COLS - r - 1],
            [ROWS - r - 1, COLS - c - 1],
            [ROWS - c - 1, r],
            [r, c]
        ]

    # get 1/4 of top left section, start rotate from there
    one4thRows = ROWS // 2
    one4thCols = COLS // 2 if COLS % 2 == 0 else COLS // 2 + 1
    cur = None
    for i in range(one4thRows):
        for j in range(one4thCols):
            cur = matrix[i][j]
            for r, c in getRotateIndexes(i, j):
                matrix[r][c], cur = cur, matrix[r][c]