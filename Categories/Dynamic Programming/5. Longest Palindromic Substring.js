const s = "aacabdkacaa"
console.log(longestPalindrome(s))

/**
 * Time: O(n)
 * Space: O(1)
 * Use greedy algo, iterate string, and expand the section as much as possible at each index to get the longest palindrome substring
 * @param {string} s
 * @return {string}
 */
function longestPalindrome(s) {
    if(s.length === 1)return s

    let start = 0, end = 0
    //
    for(let i = 0; i < s.length; i++){ // O(n)
        let [s, e] = isPalindrome(i)
        if(e - s > end - start){
            end = e
            start = s
        }

        [s, e] = isPalindrome(i, i + 1)
        if(e - s > end - start){
            end = e
            start = s
        }
    }

    return s.slice(start, end + 1)

    function isPalindrome(start, end){
        if(end === undefined) end = start

        while(start >= 0 && end < s.length && s[start] === s[end]){
            start--
            end++
        }
        return [start+1, end-1]
    }
}