
const rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
wallsAndGates(rooms)
console.log(rooms)

/**
 * @param {number[][]} rooms
 * @return {void} Do not return anything, modify rooms in-place instead.
 */
function wallsAndGates(rooms) {
    // all gates start bfs, and write the step to the empty room, if larger the empty room step, stop dfs
    const ROWS = rooms.length, COLS = rooms[0].length, GATE = 0
    let step = 0
    let cur = [], next = [], visited = new Set()
    for (let i = 0; i < ROWS; i++) {
        for (let j = 0; j < COLS; j++) {
            if(rooms[i][j] === GATE){
                cur.push([i, j])
                visited.add(`${i} ${j}`)
            }

        }
    }

    while(cur.length > 0){
        for(let index of cur){
            let i = index[0], j = index[1]
            rooms[i][j] = step
            addToQueue(i + 1, j)
            addToQueue(i - 1, j)
            addToQueue(i, j + 1)
            addToQueue(i, j - 1)
        }
        step++
        cur = next
        next = []
    }

    function addToQueue(i, j){
        if( i < 0
            || i === ROWS
            || j < 0
            || j === COLS
            || rooms[i][j] === -1
            || visited.has(`${i} ${j}`)
        )
            return

        next.push([i, j])
        visited.add(`${i} ${j}`)
    }
}
