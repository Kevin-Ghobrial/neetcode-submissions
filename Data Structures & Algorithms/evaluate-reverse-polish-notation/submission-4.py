class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second / first))
            else:
                stack.append(int(i))


        return stack[0]
            
         
        
