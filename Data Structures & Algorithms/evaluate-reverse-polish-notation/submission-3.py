class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Do action if token is sign
        stack = []

        for token in tokens:
            if token == "+":
                opSum = stack.pop() + stack.pop()
                stack.append(opSum)
            elif token == "-":
                opSub = stack.pop()
                opMin = stack.pop()
                stack.append(opMin - opSub)
            elif token == "*":
                opMult = stack.pop() * stack.pop()
                stack.append(opMult)
            elif token == "/":
                opDsr = stack.pop()
                opDvd = stack.pop()
                stack.append(int(opDvd / opDsr))
            else:
                stack.append(int(token))

        return stack.pop()