class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        a, b = 1, 1
        for i in range(n-1):
            b, a = a + b, b
        return b