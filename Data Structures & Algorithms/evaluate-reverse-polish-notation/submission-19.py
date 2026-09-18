class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def evaluate(a, b, arith):
            a = int(a)
            b = int(b)
            if arith == "+": return a + b
            if arith == "-": return b - a
            if arith == "*": return a * b
            if arith == '/': return (int)(b/a)
            
        arith = ['+', '-', '/', '*']
        s = []
        for i in tokens:
            s.append(i) if i not in arith else s.append(evaluate(s.pop(), s.pop(), i))

        return int(s[0])
    
        