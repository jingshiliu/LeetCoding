def spiralOrder(matrix):
    # when see WALL (index bound), or see a visited index, turn right
    # 0 0 -> 0 1 -> 0 2 -> 1 2 -> 2 2 -> 2 1 -> 2 0 -> 1 0 -> 1 1
    # x, y
    # x     y+1
    # x+1,  y
    # x,    y-1
    # x-1,  y

    # update direction: curDirection = (curDirection + 1)%4
    # get direction: directions[curDirection]
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    curDirection = 0
    isRow = True
    cellsTotal = len(matrix[0]) * len(matrix)
    visitedRows = set()
    visitedCols = set()
    res = []
    curIndex = [0, 0]
    while True:
        if len(res) == cellsTotal: return res
        num = matrix[curIndex[0]][curIndex[1]]
        res.append(num)

        direction = directions[curDirection]
        nextIndex = [curIndex[0] + direction[0], curIndex[1] + direction[1]]
        # move index
        if (isRow and (nextIndex[1] == len(matrix[0])
                       or nextIndex[1] < 0
                       or nextIndex[1] in visitedCols)
                or
                not isRow and (
                        nextIndex[0] == len(matrix)
                        or nextIndex[0] < 0
                        or nextIndex[0] in visitedRows)):
            if isRow:
                visitedRows.add(curIndex[0])
            else:
                visitedCols.add(curIndex[1])
            isRow = not isRow

            curDirection = (curDirection + 1) % 4
            direction = directions[curDirection]
            curIndex[0] += direction[0]
            curIndex[1] += direction[1]

        else:
            curIndex = nextIndex


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print(spiralOrder(matrix))
