import math


def evalRPN(self, tokens) -> int:
    # Idea:
    # Expand the tree of outcomes through Recursion which utilizes the built-in call stack
    stack = []
    for token in tokens:
        try:
            stack.append(int(token))
        except:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                stack.append(0 - (stack.pop() - stack.pop()))
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                res = math.floor(n1 / n2) if n1 / n2 > 0 else math.ceil(n1 / n2)
                stack.append(res)

    return stack[0]
