/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
    if(s.length === 1)return 1
    let res = 0
    for(let i = 0; i < s.length; i++){
        findPalindrome(i)
        findPalindrome(i, i + 1)
    }
    return res

    function findPalindrome(start, end){
        if(end === undefined) end = start
        while (start >= 0 && end < s.length && s[start] === s[end]){
            res++
            start--
            end++
        }
    }
};