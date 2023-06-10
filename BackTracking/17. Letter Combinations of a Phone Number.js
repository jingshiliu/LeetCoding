/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if(!digits.length)
        return []
    const phoneDigitsCharacters = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }

    const res = []
    const curCombin = []
    bt(0)
    return res

    function bt(index){
        if(index === digits.length){
            res.push(curCombin.join(''))
            return
        }
        const characters = phoneDigitsCharacters[digits[index]]
        for(let i = 0; i < characters.length; i++){
            curCombin.push(characters[i])
            bt(index + 1)
            curCombin.pop()
        }
    }
};