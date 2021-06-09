class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []


    def push(self, val: int) -> None:
        if len(self.stack) :
            tmp = min(val, self.minStack[-1])      
        else:
            tmp = val
        self.stack.append(val)
        self.minStack.append(tmp)

    def pop(self) -> None:
        if self.stack:
            self.minStack.pop()
            return self.stack.pop()
        else:
            return self.stack

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return self.stack

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()