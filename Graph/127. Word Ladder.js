const beginWord = 'hit'
const endWord = 'cog'
const wordList = ["hot","dot","dog","lot","log","cog"]
console.log(ladderLength(beginWord, endWord, wordList))


/**
 * Time O(n2 * m)
 * Space: O(n2)
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
function ladderLength(beginWord, endWord, wordList) {
    // first put into map keys: h_t, ho_  value: [words that satisfies this pattern]
    // then do a bfs
    const patternToWords = new Map()
    wordList.push(beginWord)
    // O(n * m)
    for(let word of wordList){
        // getPattern: O(word.length = m)
        for(let pattern of getPatterns(word)){
            if(patternToWords.has(pattern)){
                patternToWords.get(pattern).push(word)
            }else{
                patternToWords.set(pattern, [word])
            }
        }
    }

    const visited = new Set()
    let cur = [beginWord], next = [], depth = 1
    // O(n2)
    while(cur.length > 0){
        for(let word of cur){
            visited.add(word)

            if(word === endWord)
                return depth
            // O(m)
            for(let pattern of getPatterns(word)){
                for(let wrd of patternToWords.get(pattern)){
                    if(visited.has(wrd))
                        continue
                    next.push(wrd)
                }
            }
        }

        cur = next
        next = []
        depth++
    }

    return 0

    function getPatterns(word){
        return Array(word.length).fill().map((_, i) => `${word.slice(0, i)}_${word.slice(i + 1)}` )
    }

}