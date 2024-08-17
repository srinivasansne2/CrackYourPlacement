class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        sl = path.split('/')
        sl = [item for item in sl if item != ""]
        STAY, GOUP = ".", ".."
        for c in sl:
            if c == GOUP:
                if stack:
                    stack.pop()
            elif c != STAY:
                stack.append(c)
        return "/" + "/".join(stack)