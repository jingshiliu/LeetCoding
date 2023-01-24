
const grid = [[2,1,1],[1,1,0],[0,1,1]]
console.log(orangesRotting(grid))





/**
 * @param {number[][]} grid
 * @return {number}
 */
function orangesRotting(grid) {
    // bfs
    // use array
    // put all rotten orange address into a list and set time to 0
    // pop all the rotten orange address, and put all the fresh orange that it next to, to a new array
    // time + 1
    // repeat until no fresh orange been placed into queue
    // iterate entire grid, check if there is a fresh orange, if yes return -1 else return time
    const ROWS = grid.length, COLS = grid[0].length
    const rottenOranges = new Set()
    let curRotten = [], newRotten = [], time = 0, fresh = 0
    for(let i = 0; i < ROWS; i++)
        for(let j = 0; j < COLS; j++){

            if(grid[i][j] === 1)
                fresh++

            if(grid[i][j] === 2){
                curRotten.push([i, j])
                rottenOranges.add(`${i} ${j}`)
            }

        }
    if(fresh === 0 && curRotten.length === 0) return 0

    while (curRotten.length > 0){
        for(let rotten of curRotten){
            let i = rotten[0], j = rotten[1]
            rotNeighborOranges(i - 1, j)
            rotNeighborOranges(i + 1, j)
            rotNeighborOranges(i, j - 1)
            rotNeighborOranges(i, j + 1)
        }
        curRotten = newRotten
        newRotten = []
        time++
    }

    if(fresh === 0)
        return time - 1
    return -1

    function rotNeighborOranges(i, j){
        if( i >= 0
            && i < ROWS
            && j >= 0
            && j < COLS
            && grid[i][j] === 1
            && !rottenOranges.has(`${i} ${j}`)){
            newRotten.push([i, j])
            rottenOranges.add(`${i} ${j}`)
            fresh--
        }

    }
}