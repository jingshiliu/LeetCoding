var generateParenthesis = function(n) {
    let stack = []
    let res = []

    function findRes(openN, closeN){
        if(openN === closeN && openN === n){
            res.push(stack.join(''))
        }

        if (openN < n){
            stack.push('(')
            findRes(openN+1, closeN)
            stack.pop()
        }
        if (closeN < openN){
            stack.push(')')
            findRes(openN, closeN + 1)
            stack.pop()
        }
    }

    findRes(0,0)
    return res
};