class Solution:
    def maxArea(self, height: List[int]) -> int:
        r , l = len(height)-1, 0
        res=0
        while l<r:
            d=r-l
            m=min(height[l],height[r])
            f=d*m
            if f>res:
                res=f
            elif height[l]>height[r]:
                r=r-1
            else:
                l+=1
        return res