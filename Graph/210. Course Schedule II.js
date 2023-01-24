
const pres = [[1,0],[2,0],[3,1],[3,2]]

const numCourses = 4

console.log(findOrder(numCourses, pres))


/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
function findOrder(numCourses, prerequisites) {
    const courseToPres = new Map()
    for(let pre of prerequisites){
        if(courseToPres.has(pre[0]))
            courseToPres.get(pre[0]).push(pre[1])
        else
            courseToPres.set(pre[0], [pre[1]])
    }

    const output = []

    // when we visit a node, we add it to findCycle, and it gets removed once all prerequisites are taken
    // however, if we visit a node again before all its prerequisites been fulfilled, we find a cycle
    // we can detect it bc it is not removed from findCycle
    const findCycle = new Set()
    const visited = new Set() // if a course is already schedule, there is no need to traverse the tree again

    let cycle = false

    for (let i = 0; i < numCourses; i++) {
        dfs(i)
    }
    return cycle? []: output

    function dfs(course){

        if(findCycle.has(course)){
            cycle = true
            return
        }
        if(visited.has(course))
            return

        if(courseToPres.has(course)){
            findCycle.add(course)
            visited.add(course)
            for(let pre of courseToPres.get(course)){
                dfs(pre)
            }
            findCycle.delete(course)
        }else{
            // if a course hasn't been taken and have no prerequisite,
            // we can just push it to output but remember to add it to visited first
            visited.add(course)
        }
        output.push(course)

    }
}