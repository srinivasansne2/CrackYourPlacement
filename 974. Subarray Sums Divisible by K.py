class Solution:
    def sub(nums: List[int], k: int) -> int:
        ream=ans=0
        d=defaultdict(int)
        d[0]=1
    
        for i in nums:
            ream=(ream+i)%k
            ans+=d[ream]
            d[ream]+=1
    
        return ans

    sys.stdout=open('user.out','w')
    for nums in map(loads,stdin):
        print(sub(nums,int(stdin.readline())))
    exit()