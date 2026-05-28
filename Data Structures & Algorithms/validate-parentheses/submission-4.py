class Solution:
    def isValid(self, s: str) -> bool:
        p = []

        if len(s) % 2 != 0:
            return False

        # (({})())
        for i in s:

            print(p)
            if i in "({[":
                p.append(i)
            else:

                if len(p) == 0:
                    return False

                openP = p.pop()
                if openP == '[':
                    if i != ']':
                        return False
                elif openP == '(':
                    if i != ')':
                        return False    
                elif openP == '{':
                    if i != '}':
                        return False   
                        
        if len(p) == 0:
            return True
        return False
        