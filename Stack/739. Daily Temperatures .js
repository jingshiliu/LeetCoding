var dailyTemperatures = function(temperatures) {
    // Idea:
    // If found a Temp higher than 'top' of stack,
    //     pop until it the above condition fails.
    //     When pop, change the res array
    // else
    //     append on the stack

    const res = Array(temperatures.length).fill(0)
    const stack = [[101, -1]] // [temperature, index]

    for(let i = 0; i < temperatures.length; i++){ // O(n)
        while (temperatures[i] > stack[stack.length - 1][0]){ // O(n)
            let topStack = stack.pop()
            res[topStack[1]] = i - topStack[1]
        }
        stack.push([temperatures[i], i]) // O(1)
    }

    return res

};

const temperatures = [73,74,75,71,69,72,76,73]
console.log(dailyTemperatures(temperatures))