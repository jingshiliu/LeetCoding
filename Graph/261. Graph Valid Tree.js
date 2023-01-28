const n = 5
const edges = [[0,1],[0,4],[1,4],[2,3]]
console.log(validTree(n, edges))

/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {boolean}
 */
function validTree(n, edges) {
    // union find
    // check if there is a cycle during each union
    // check if it is connected at the last
    const parent = Array(n).fill().map((x, i) => i)
    const rank = Array(n).fill(1)

    function find(node){
        let p = parent[node]

        while(p !== parent[p]){
            parent[p] = parent[parent[p]]
            p = parent[p]
        }

        return p
    }

    function union(node1, node2){
        const root1 = find(node1), root2 = find(node2)

        if(root1 === root2){
            return false
        }

        if(rank[root1] > rank[root2]){
            rank[root1] += rank[root2]
            parent[root2] = root1
        }else{
            rank[root2] += rank[root1]
            parent[root1] = root2
        }

        return true
    }

    let rootCount = n
    for(let [node1, node2] of edges){
        // if unsuccessful, means found cycle
        if(! union(node1, node2)){
            return false
        }

        rootCount--
    }
    return rootCount === 1
}