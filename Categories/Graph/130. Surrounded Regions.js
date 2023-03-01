const board = [
    ["O", "X", "O", "O", "O", "X"],
    ["O", "O", "X", "X", "X", "O"],
    ["X", "X", "X", "X", "X", "O"],
    ["O", "O", "O", "O", "X", "X"],
    ["X", "X", "O", "O", "X", "O"],
    ["O", "O", "X", "X", "X", "X"]
]
solve(board)
console.log(board)


/**
 * @param {string[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
function solve(board) {
    // dfs from all borders, if you see a O then mark it with an E
    // bc they are the Os that we want to keep, we need to distinguish it from captured Os
    // then we change all Es to O, and all Os that border cannot reach since they are not E, to X
    const ROWS = board.length, COLS = board[0].length

    for (let i = 0; i < ROWS; i++){
        dfs(i, 0)
        dfs(i, COLS - 1)
    }

    for (let i = 0; i < COLS; i++) {
        dfs(0, i)
        dfs(ROWS - 1, i)
    }

    for (let i = 0; i < ROWS; i++) {
        for (let j = 0; j < COLS; j++) {
            if(board[i][j] === 'E')
                board[i][j] = 'O'
            else if(board[i][j] === 'O')
                board[i][j] = 'X'
        }
    }


    function dfs(i, j) {
        if (
            i < 0
            || i === ROWS
            || j < 0
            || j === COLS
            || board[i][j] === "X"
            || board[i][j] === "E"
        )
            return false

        board[i][j] = 'E'
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    }
}

