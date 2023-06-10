
const matrix = [["0","1"],["1","0"]]
console.log(maximalSquareOptimal(matrix))

/**
 * @param {string[][]} matrix
 * @return {number}
 */
function maximalSquareOptimal(matrix){
    const ROWS = matrix.length
    const COLS = matrix[0].length
    const dp = Array(COLS + 1).fill(0)
    let res = 0
    let prev = 0, temp
    for(let i = 1; i <= ROWS; i++){
        for(let j = 1; j <= COLS; j++){
            temp = dp[j]
            if(matrix[i - 1][j - 1] === "1"){
                dp[j] = Math.min(dp[j], dp[j-1], prev) + 1
                res = Math.max(res, dp[j])
            }else
                dp[j] = 0

            prev = temp
        }
    }
    return res * res
}


/**
 * @param {string[][]} matrix
 * @return {number}
 */
function maximalSquareDp2D(matrix){
    const ROWS = matrix.length
    const COLS = matrix[0].length
    const dp = Array(ROWS + 1).fill().map(()=> Array(COLS + 1).fill(0))
    let res = 0
    for(let i = 1; i <= ROWS; i++){
        for(let j = 1; j <= COLS; j++){
            if(matrix[i - 1][j - 1] === "0") continue
            dp[i][j] = Math.min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
            res = Math.max(res, dp[i][j])
        }
    }
    return res * res
}


/**
 * @param {string[][]} matrix
 * @return {number}
 */
function maximalSquareBruteForce(matrix) {
    // use dfs
    // give the size of cur rec, if its a square, update the res if it is max
    const ROWS = matrix.length
    const COLS = matrix[0].length
    let res = 0
    for(let i = 0; i < ROWS; i++){
        for(let j = 0; j < COLS; j++){
            findMaxSquare(i, j, 1)
        }
    }

    return res

    function findMaxSquare(i, j, sideLength){
        if( i === ROWS
            || j === COLS
            || matrix[i][j] === "0"
        )
            return
        let isSquare = true
        // check side
        for (let offset = 1; offset < sideLength; offset++) {
            if(matrix[i][j - offset] === "0" || matrix[i - offset][j] === "0") {
                isSquare = false
                break
            }
        }
        if(isSquare){
            res = Math.max(res, sideLength * sideLength)

            // expand square by increase side length by 1
            findMaxSquare(i + 1, j + 1, sideLength + 1)
        }
    }
}


