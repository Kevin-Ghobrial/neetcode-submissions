class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        #self.min1 = float('inf')

    # 1, 2, 0
    # 1, 1, 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            min1 = min(val, self.minStack[-1])
        else:
            min1 = val
        self.minStack.append(min1)

    def pop(self) -> None:

        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        print(self.stack, self.minStack)
        if len(self.minStack) != 0:
            return self.minStack[-1]
        else:
            return 0