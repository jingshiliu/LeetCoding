def searchMatrix(matrix, target: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])

    r, c = ROWS - 1, 0

    while r >= 0 and c < COLS:
        if matrix[r][c] < target:
            c += 1
        elif matrix[r][c] > target:
            r -= 1
        else:
            return True

    return False
