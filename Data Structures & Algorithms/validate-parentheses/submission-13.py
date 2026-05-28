class Solution:
    def isValid(self, s: str) -> bool:

        # idea: add all open to a stack
        # once there is a closed, we will pop off the stack
        
        stack = []
        for c in s:
            if c in "{([":
                stack.append(c)
            
            elif c in ")}]":
                popped = stack.pop() if len(stack) > 0 else "BAD"
                if c == ")":
                    if popped != "(":
                        return False
                elif c == "}":
                    if popped != "{":
                        return False
                elif c == "]":
                    if popped != "[":
                        return False
        
        return True if len(stack) == 0 else False
            
