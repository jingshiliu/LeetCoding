/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(cost) {
    const minCost = Array(cost.length).fill(0)
    const findMinCost = (n)=>{
        if(n === 0 || n === 1)
            return cost[n]

        if(!minCost[n - 1]) minCost[n - 1] = findMinCost(n - 1)
        if(!minCost[n - 2]) minCost[n - 2] = findMinCost(n - 2)

        return Math.min(minCost[n-1], minCost[n-2]) + cost[n]
    }
    return Math.min(findMinCost(cost.length - 1), findMinCost(cost.length - 2))
};