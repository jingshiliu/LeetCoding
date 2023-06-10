class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1:
            self.minStack.append(val)
        elif val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Above solution is very efficient
# However, if 'val == min' append to stack repeatedly, we end up with same number on stack which occupies more space
# But in general, above has better performance because of less condition check.

# If same minVal doesn't append to stack for most operations, we end up higher space and worse performance
# because condition checks were for nothing, and list creation for each new Min
# Here is a MaxStack using improved solution of 2 stack

class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxStack = []

    def push(self, val):
        self.stack.append(val)
        if len(self.stack) == 1 or val > self.maxStack[-1][0]:
            self.maxStack.append([val, 1])
        elif val == self.stack[-1][0]:
            self.stack[-1][1] += 1

    def pop(self):
        if self.stack.pop() == self.maxStack[-1][0]:
            self.maxStack[-1][1] -= 1
            if self.maxStack[-1][1] == 0:
                self.maxStack.pop()

    def top(self):
        return self.stack[-1]

    def getMax(self):
        return self.maxStack[-1][0]