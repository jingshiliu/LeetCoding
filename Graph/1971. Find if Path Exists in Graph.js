/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} source
 * @param {number} destination
 * @return {boolean}
 */
var validPath = function(n, edges, source, destination) {
    const sourceToDes = new Map()
    for(let edge of edges){
        if(!sourceToDes.has(edge[0]))
            sourceToDes.set(edge[0], [])

        if(!sourceToDes.has(edge[1]))
            sourceToDes.set(edge[1], [])

        sourceToDes.get(edge[1]).push(edge[0])
        sourceToDes.get(edge[0]).push(edge[1])

            
    }

    const visited = new Set()
    return dfs(source)

    function dfs(node){
        if(visited.has(node) || node === undefined)
            return false

        visited.add(node)
        if(node === destination){
            return true
        }
        
        const des = sourceToDes.get(node)
        for(let src of des){
            if(dfs(src))
                return true
        }
        return false
    }
};
