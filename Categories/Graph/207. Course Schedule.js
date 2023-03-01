/**
 * detect cycle in a graph by using dfs
 * we search the graph starting at a node, and detect cycle by visit the nodes it points to
 * we do this recursively and if we visit some node again before its release on call stack
 * we know there is a cycle
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {
    const courseToPre = new Map()
    for(let pre of prerequisites){
        if(courseToPre.has(pre[0]))
            courseToPre.get(pre[0]).push(pre[1])
        else
            courseToPre.set(pre[0], [pre[1]])
    }

    const finished = new Set()
    const pre = new Set()
    let foundCycle = false
    for(let i = 0; i < prerequisites.length; i++){
        if(foundCycle) // if found cycle we stop checking here
            return false

        detectCycle(prerequisites[i][0])
    }

    return !foundCycle

    function detectCycle(node){
        if (node === undefined || finished.has(node))
            return
        if (pre.has(node)){
            foundCycle = true
            return
        }

        pre.add(node)
        const pres = courseToPre.get(node)
        if(pres)
            for(let pre of pres){
                detectCycle(pre)
            }
        finished.add(node)
    }

};


const numCourses = 5
const prerequisites = [[1,4],[2,4],[3,1],[3,2]]

console.log(canFinish(numCourses, prerequisites))