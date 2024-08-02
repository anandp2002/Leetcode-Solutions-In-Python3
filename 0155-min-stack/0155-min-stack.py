class MinStack:

    def __init__(self):
        self.stack=[]
        self.minimumStack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimumStack:
            min_val=min(val,self.minimumStack[-1])
        else:
            min_val=val        
        self.minimumStack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.minimumStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimumStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()