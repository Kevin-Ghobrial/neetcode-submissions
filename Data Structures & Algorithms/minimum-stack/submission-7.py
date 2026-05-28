class MinStack:



    # 2, 3, 1, 1, 0
    # 2, 2, 1, 1
    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            if val < self.minStack[len(self.minStack) - 1]:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[len(self.minStack) - 1])
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]    

    def getMin(self) -> int:
        return self.minStack[len(self.minStack) - 1]

