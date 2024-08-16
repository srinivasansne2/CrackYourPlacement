class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        m=0
        n=len(cardPoints)
        for i in range (k):
            m+=cardPoints[i]
        mx=m
        c=k-1
        for j in range (n-1,n-k-1,-1):
            m= m+cardPoints[j]-cardPoints[c]
            if m>mx:
                mx= m   
            c-=1         
        return mx