// require this library to be Version 4.1
const { MinPriorityQueue } = require('@datastructures-js/priority-queue');


const points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
console.log(minCostConnectPoints(points))

/**
 * use visited array, and visitCount rather than Set to improve performance
 * calculate distance while prim algo rather than calculate distance before the prim algo
 * @param {number[][]} points
 * @return {number}
 */
function minCostConnectPoints(points) {
    const minHeap = new MinPriorityQueue()
    const visited = Array(points.length).fill(false)
    let visitCount = 0
    let cost = 0

    minHeap.enqueue(0, 0)
    while(visitCount < points.length){
        let {priority, element} = minHeap.dequeue()
        if(visited[element])
            continue

        visited[element] = true
        visitCount++
        cost += priority

        for(let i = 0; i < points.length; i++){
            if(visited[i])
                continue
            minHeap.enqueue(i, getDistance(element, i))
        }
    }

    return cost

    function getDistance(src, dst){
        return Math.abs(points[src][0] - points[dst][0]) + Math.abs(points[src][1] - points[dst][1])
    }
}

/**
 * @param {number[][]} points
 * @return {number}
 */
function minCostConnectPointsNonOptimal(points) {
    const graph = Array(points.length).fill().map(() => [])
    let distance = 0
    for(let src = 0; src < points.length - 1; src++){
        for(let dst = src + 1; dst < points.length; dst++){
            distance = Math.abs(points[src][0] - points[dst][0]) + Math.abs(points[src][1] - points[dst][1])
            graph[dst].push([src, distance])
            graph[src].push([dst, distance])
        }
    }

    const minHeap = new MinPriorityQueue()
    const visited = Array(points.length).fill(false)
    let visitCount = 0
    let cost = 0

    minHeap.enqueue(0, 0)
    while(visitCount < points.length){
        let {priority, element} = minHeap.dequeue()
        if(visited[element])
            continue

        visited[element] = true
        visitCount++
        cost += priority

        for(let point of graph[element]){
            if(visited[point[0]])
                continue
            minHeap.enqueue(point[0], point[1])
        }
    }

    return cost

}