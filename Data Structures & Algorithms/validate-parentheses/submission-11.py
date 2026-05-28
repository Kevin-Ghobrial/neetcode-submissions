class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        # ([{}()])
        # ([]]])

        open_closed = 0
        open_count = 0
        closed_count = 0

        if len(s) < 2:
            return False

        for c in s:
            if c in "({[":
                stack.append(c)
                open_closed += 1
                open_count += 1
                continue
            
            closed_count += 1
            if len(stack) > 0:
                p = stack.pop()
            
                if p == "(":
                    if c != ")":
                        return False
                    elif c == ")":
                        open_closed -= 1
                if p == "[":
                    if c != "]":
                        return False
                    elif c == "]":
                        open_closed -= 1
                if p == "{":                  
                    if c != "}":
                        return False
                    elif c == "}":
                        open_closed -= 1
        
        print(open_closed)


        return True if (open_closed == 0 and open_count == closed_count) else False

            

