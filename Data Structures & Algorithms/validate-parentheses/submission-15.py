class Solution:
    def isValid(self, s: str) -> bool:
        # rules:
        # 1. it must be open to close
        # 2. the last one open is the first one closed -> stack

        stack = []

        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if stack:
                    pop = stack.pop()
                else:
                    return False
                if pop == "(" and i != ")":
                    return False
                elif pop == "{" and i != "}":
                    return False
                elif pop == "[" and i != "]":
                    return False
        
        return True if not stack else False
                    
                