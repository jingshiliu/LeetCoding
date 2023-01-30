const n = 45
console.log(climbStairs(n))


/**
 * @param {number} n
 * @return {number}
 */
function climbStairs(n) {
    const memory = Array(45).fill(0)
    function calcWays(n){
        if(n === 1)
            return 1
        if(n === 2)
            return 2

        if(!memory[n - 1])
            memory[n - 1] = calcWays(n - 1)
        if(!memory[n - 2])
            memory[n - 2] = calcWays(n - 2)

        return memory[n - 1] + memory[n - 2]
    }
    return calcWays(n)
}