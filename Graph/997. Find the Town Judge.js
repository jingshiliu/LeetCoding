/**
 * @param {number} n
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function(n, trust) {
    // if A trust B, A's score--, and B's score++
    // at last, the one who has score of N - 1 is trusted by N-1 and trust nobody
    const trustScore = Array(n + 1).fill(0)
    for(let [t1, t2] of trust){
        trustScore[t2]++
        trustScore[t1]--
    }

    for(let i = 1; i < trustScore.length; i++){
        if(trustScore[i] === n - 1)
            return i
    }
    return -1

};