
var pacificAtlantic = function (heights) {
    // 0 = notVisited, 1 = pacific, 2 = atlantic, 3 = both
    // better space complexity
    // array [], stores ocean info as above,\
    // wait, string can achieve same thing with even less space
    // if length == 1, we know it only flow to one ocean, if 2, we push to res

    const rowCount = heights.length
    const colCount = heights[0].length
    const visited = Array(rowCount).fill().map(() => Array(colCount).fill(0))
    const res = []

    for (let r = 0; r < rowCount; r++) {
        for (let c = 0; c < colCount; c++) {
            calculateOcean(r, c)
        }
    }
    return res

    function calculateOcean(r, c) {
        if (visited[r][c] !== 0)
            return visited[r][c]


        if ((r === 0 || c === 0) && (r === rowCount - 1 || c === colCount - 1)) {
            visited[r][c] = 3
            res.push([r, c])
            return visited[r][c]
        } else if (r === 0 || c === 0) {
            visited[r][c] = 1
            return visited[r][c]
        } else if (r === rowCount - 1 || c === colCount - 1) {
            visited[r][c] = 2
            return visited[r][c]
        }

        let evaluation = {
            atl: false,
            pac: false
        }
        if (heights[r][c - 1] <= heights[r][c]) {
            evaluateNeighbor(calculateOcean(r, c - 1), evaluation)
        } else if (heights[r][c + 1] <= heights[r][c]) {
            evaluateNeighbor(calculateOcean(r, c + 1), evaluation)
        } else if (heights[r - 1][c] <= heights[r][c]) {
            evaluateNeighbor(calculateOcean(r - 1, c), evaluation)
        } else if (heights[r + 1][c] <= heights[r][c]) {
            evaluateNeighbor(calculateOcean(r + 1, c), evaluation)
        }

        if (evaluation.pac && evaluation.atl) {
            res.push([r, c])
            visited[r][c] = 3
        } else if (evaluation.pac) {
            visited[r][c] = 1
        } else if (evaluation.pac) {
            visited[r][c] = 2
        }
        return visited[r][c]
    }

    function evaluateNeighbor(neighborOcean, evaluation) {
        switch (neighborOcean) {
            case 1:
                evaluation.pac = true
                break
            case 2:
                evaluation.atl = true
                break
            case 3:
                evaluation.pac = true
                evaluation.atl = true
                break
            default:
        }
    }

};

const heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
pacificAtlantic(heights)