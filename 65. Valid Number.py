class Solution:
    def isNumber(self, s: str) -> bool:
        import re
        integer = r"[-+]?\d+"
        decimal = r"[-+]?(?=\.?\d)\d*\.\d*"
        return re.compile("(%s|%s)([eE]%s)?" % (integer, decimal, integer)).fullmatch(s)
        