


def solveNQueens(n: int):
    backTrack = [-1] * n
    chess = [['.'] * n for i in range(n)]
    col = 0

    def getSolution():
        nonlocal chess
        res = []
        for i in chess:
            res.append(''.join(i))
        return res

    def diagonalTest(row, col):
        nonlocal chess
        i = 1
        while col - i >= 0 and row - i >= 0:
            if chess[row - i][col - i] == 'Q':
                return False
            i += 1

        i = 0
        while row + i < n and col - i >= 0:
            if chess[row + i][col - i] == 'Q':
                return False
            i += 1
        return True

    def rowTest(row, col):
        nonlocal chess
        for i in range(col - 1, -1, -1):
            if chess[row][i] == 'Q':
                return False
        return True

    res = []
    while True:
        row = backTrack[col]
        chess[row][col] = '.'
        row += 1

        while True:
            if row == n:
                backTrack[col] = -1
                col -= 1
                break
            if diagonalTest(row, col) and rowTest(row, col):
                chess[row][col] = 'Q'
                if col == n - 1:
                    res.append(getSolution())
                    backTrack[col] = -1
                    chess[row][col] = '.'
                    col -= 1
                    break
                backTrack[col] = row
                col += 1
                break

            row += 1

        if col == -1:
            break
    return res


def solveNQueens2(n: int):
    chess = [['.'] * n for i in range(n)]

    def isOk(row, col):
        nonlocal n
        for i in range(n):
            if chess[row][i] == 'Q':
                return False
            if row + i < n and col - i >= 0 and chess[row + i][col - i] == 'Q':
                return False
            if col - i >= 0 and row - i >= 0 and chess[row - i][col - i] == 'Q':
                return False
        return True

    backTrack = [-1] * n
    col = 0
    res = []
    while True:
        row = backTrack[col]
        chess[row][col] = '.'
        row += 1

        while True:
            if row == n:
                backTrack[col] = -1
                col -= 1
                break
            if isOk(row, col):
                chess[row][col] = 'Q'
                if col == n - 1:
                    res.append([''.join(i) for i in chess])
                    backTrack[col] = -1
                    chess[row][col] = '.'
                    col -= 1
                    break
                backTrack[col] = row
                col += 1
                break

            row += 1

        if col == -1:
            break
    return res