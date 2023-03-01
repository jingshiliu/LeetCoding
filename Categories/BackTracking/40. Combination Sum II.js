/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {
    candidates.sort()
    const combinationHolder = []
    const res = []

    function getCombinations(index, curSum){
        if (curSum >= target){
            if(curSum === target)
                res.push(combinationHolder.map(x => x)) // copy combination holder
            return
        }

        for(let i = index; i < candidates.length; i++){
            if(i !== index && candidates[i] === candidates[i - 1])
                continue

            combinationHolder.push(candidates[i])
            getCombinations(i + 1, curSum + candidates[i])
            combinationHolder.pop()
        }
    }

    getCombinations(0, 0)
    return res
};

const candidates = [10,1,2,7,6,1,5]
const target = 8
console.log(combinationSum2(candidates, target))