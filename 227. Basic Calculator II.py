class Solution:
    def calculate(self, s: str) -> int:
        pre = 0
        sign = '+'
        num = ''
        ans = 0

        for c in itertools.chain(s, '+'):
            if c.isdigit():
                num += c
            if c in "+-*/":
                num = int(num)
                if sign == '+':
                    pre += num
                if sign == '-':
                    pre -= num
                if sign == '*':
                    pre *= num
                if sign == '/':
                    pre = int(pre / num)
                if c in "+-":
                    ans += pre
                    pre = 0
                sign = c
                num = ''
        
        return ans