class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = ['+', '-', '*', '/']
        stack = []
        for token in tokens: 
            if token in symbols: 
                b = stack.pop()
                a = stack.pop()
                if token == '+': 
                    calc = a + b
                elif token == '-':
                    calc = a-b
                elif token == '*': 
                    calc = a*b
                else: 
                    calc = int(a/b)
                stack.append(calc)
            else: 
                stack.append(int(token))
        return stack[0] 



        
        
        