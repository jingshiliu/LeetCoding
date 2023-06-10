/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
var pacificAtlantic = function(heights) {
    // solves it backward
    // begin at the ocean, see where can it be flowed from, those with higher height
    const rowCount = heights.length
    const colCount = heights[0].length
    const pac = new Set()
    const atl = new Set()
    const res = []

    for(let i = 0; i < rowCount; i++){
        dfs(i, 0, pac, 0)
        dfs(i, colCount - 1, atl, 0)
    }

    for(let i = 0; i < colCount; i++){
        dfs(0, i, pac, 0)
        dfs(rowCount - 1, i, atl, 0)
    }


    for(let r = 0; r < rowCount; r++){
        for(let c = 0; c < colCount; c++){
            if(pac.has(`${r} ${c}`) && atl.has(`${r} ${c}`))
                res.push([r,c])
        }
    }
    return res

    function dfs(r, c, visited, prevHeight){
        if( visited.has(`${r} ${c}`)
            || r < 0
            || c < 0
            || r === rowCount
            || c === colCount
            || prevHeight > heights[r][c]
        )
            return

        visited.add(`${r} ${c}`)

        dfs(r, c + 1, visited, heights[r][c])
        dfs(r, c - 1, visited, heights[r][c])
        dfs(r + 1, c, visited, heights[r][c])
        dfs(r - 1, c, visited, heights[r][c])
    }
};

const heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
pacificAtlantic(heights)