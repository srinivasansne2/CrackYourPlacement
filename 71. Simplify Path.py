class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for p in [x for x in path.split('/') if x]:
            if p == '..':
                res.pop() if res else False
            elif p != '.':
                res.append(p)
        return '/' + '/'.join(res)