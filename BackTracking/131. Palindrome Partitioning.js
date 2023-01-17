/**
 * @param {string} s
 * @return {string[][]}
 */
function partition(s) {
    const res = []
    const cur = []

    dfs(0, [])
    return res

    // for each char, we either push into current string, or start a new string
    function dfs(index, curStr){
        if(index === s.length){
            res.push(cur.map(x => x.join('')))
            return
        }

        curStr.push(s[index])
        dfs(index + 1, curStr)
        curStr.pop()

        if(curStr.length && isPalindrome(curStr)){
            cur.push(curStr)
            curStr = [s[index]]
            dfs(index + 1, curStr)
        }
    }

    function isPalindrome(str){
        let l = 0
        let r = str.length
        while ( l < r){
            if (str[l] !== str[r])
                return false
            l += 1
            r -= 1
        }
        return true
    }

}
let s = 'partition'
console.log(partition(s))