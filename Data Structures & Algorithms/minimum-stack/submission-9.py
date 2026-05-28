class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.minStack) > 0:
            curMin = self.minStack[-1]
        else:
            curMin = val
        curMin = min(curMin, val)
        self.minStack.append(curMin)
        self.stack.append(val)
        print(self.stack, self.minStack)
        
    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if len(self.stack) > 0 else 0

    def getMin(self) -> int:
        return self.minStack[-1] if len(self.minStack) > 0 else 0
       
