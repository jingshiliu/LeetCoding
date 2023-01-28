const n = 5
const edges = [[0,1],[1,2],[3,4]]
console.log(countComponents(n, edges))

/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
function countComponents(n, edges) {
    // union find, and see how many root are there

    // the root actually tells 2 information
    // 1. what is the root node, if root = parent[root]
    // 2. where to look for the root node, if root != parent[root]
    // if later on, root1 become part of the tree of root2
    // then, parent[root1] tells where to look for the new root
    const parent = Array(n).fill().map((x, i) => i)
    const rank = Array(n).fill(1)

    function find(node){
        let p = parent[node]
        while( p !== parent[p]){
            parent[p] = parent[parent[p]] // compression, make the way to find root shorter
            p = parent[p]
        }
        return p
    }

    function union(node1, node2){
        const root1 = find(node1), root2 = find(node2)
        if(root1 === root2){
            rank[root1]++
            return
        }
        if(rank[root1] > rank[root2]){
            rank[root1] += rank[root2]
            parent[root2] = root1
        }else{
            rank[root2] += rank[root1]
            parent[root1] = root2
        }
    }

    for(let [node1, node2] of edges){
        union(node1, node2)
    }

    const roots = new Set()
    for(let i = 0; i < n; i++){
        roots.add(find(i))
    }

    return roots.size

}