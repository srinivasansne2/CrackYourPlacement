class Solution(object):
    def addBinary(self, a, b):
        s=int(a,2)+int(b,2)
        return(format(s,'b'))