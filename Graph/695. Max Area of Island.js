/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function(grid) {
    const ROWS = grid.length
    const COLS = grid[0].length

    const visited = new Set()
    let res = 0
    let cur = 0

    for(let i = 0; i < ROWS; i++){
        for(let j = 0; j < COLS; j++){
            if(visited.has(`${i} ${j}`))
                continue

            cur = 0
            findIslandArea(i, j)
            res = Math.max(cur, res)
        }
    }

    return res

    function findIslandArea(i, j){
        if( i < 0
            || j < 0
            || i === ROWS
            || j === COLS
            || grid[i][j] === 0
            || visited.has(`${i} ${j}`)
        )
            return

        cur++
        visited.add(`${i} ${j}`)
        findIslandArea(i + 1, j)
        findIslandArea(i - 1, j)
        findIslandArea(i, j + 1)
        findIslandArea(i, j - 1)
    }
};