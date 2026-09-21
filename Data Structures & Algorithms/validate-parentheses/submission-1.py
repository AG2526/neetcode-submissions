class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for c in s: 
            if c in pairs and stack and stack[-1] == pairs[c]:
                stack.pop()
            else: 
                stack.append(c)
        return len(stack) ==0 