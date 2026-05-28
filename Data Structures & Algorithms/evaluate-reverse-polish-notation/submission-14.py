class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        i = 0
        while i < len(tokens):
            if tokens[i] == "+":
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif tokens[i] == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif tokens[i] == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a) if a != 0 else 0)
            else:
                stack.append(int(tokens[i]))
            i += 1
        
        return stack[-1]

                