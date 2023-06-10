const edges = [[1,5],[2,4],[3,4],[1,3],[3,5]]

console.log(findRedundantConnection(edges))

/**
 * UnionFind Solution
 * Time: O(n)
 * Space: O(n)
 * @param {number[][]} edges
 * @return {number[]}
 */
function findRedundantConnection(edges) {
    const parent = Array(edges.length + 1).fill().map((e, index)=> index)
    const rank = Array(edges.length + 1).fill(1)

    function find(node){
        let p = parent[node]
        while (p !== parent[p]){ // if this condition is true, we found the root node
            // this is compression
            // which make the way to find root shorter
            // and making the parent array to root array gradually
            parent[p] = parent[parent[p]]
            p = parent[p]
        }
        return p
    }

    function union(n1, n2){
        const p1 = find(n1), p2 = find(n2)

        if(p1 === p2) // cannot do union bc they have same parent
            return false

        if(rank[p1] > rank[p2]){
            parent[p2] = p1
            rank[p1] += rank[p2]
        }else{
            parent[p1] = p2
            rank[p2] += rank[p1]
        }
        return true

    }

    for(let [n1, n2] of edges){
        if(!union(n1, n2))
            return [n1, n2]
    }

}