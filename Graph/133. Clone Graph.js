
// Definition for a Node.
class Node{
    constructor(val, neighbors) {
        this.val = val === undefined ? 0 : val;
        this.neighbors = neighbors === undefined ? [] : neighbors;
    }
}


/**
 * @param {Node} node
 * @return {Node}
 */
const cloneGraph = function (node) {
    const created = new Map()

    created.set(null, null)

    // visit each node in og graph and clone it, and put into created graph
    function createClone(node) {
        if (created.has(node))
            return created.get(node)

        const clone = new Node(node.val)
        created.set(node, clone)

        const neighborClones = []
        let curNeighborClone
        for (let neighbor of node.neighbors) {
            curNeighborClone = createClone(neighbor)
            if (curNeighborClone)
                neighborClones.push(curNeighborClone)
        }
        clone.neighbors = neighborClones
        return clone
    }

    return createClone(node)
};