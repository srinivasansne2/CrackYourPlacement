class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(myString):
            stack = []
            for char in myString:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        return helper(s) == helper(t)