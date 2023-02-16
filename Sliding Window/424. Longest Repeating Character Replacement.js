const s = "AABABBA"
const k = 1
console.log(characterReplacement(s, k))

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
function characterReplacement(s, k) {
    // keep track of all {char: times } in the window
    // if max(charTime) + k < windowSize, shrink window

    let res = 0, l = 0, curMax // [char, times]
    const charToTimes = new Map()
    for(let r = 0; r < s.length; r++){
        if(!charToTimes.has(s[r]))
            charToTimes.set(s[r], 1)
        else
            charToTimes.set(s[r], charToTimes.get(s[r]) + 1)

        curMax = 0
        for(let val of charToTimes.values()){ // O(1)
            curMax = Math.max(val, curMax)
        }

        while (curMax + k <= r - l){
            charToTimes.set(s[l], charToTimes.get(s[l]) - 1)
            l++
        }

        res = Math.max(res, r - l + 1)
    }
    return res
}