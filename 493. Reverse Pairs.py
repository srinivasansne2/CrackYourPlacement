class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        from sortedcontainers import SortedList
        sl = SortedList([])
        ans = 0
        for num in nums:
            ans += len(sl) - sl.bisect_right(2*num)
            sl.add(num)
        return ans