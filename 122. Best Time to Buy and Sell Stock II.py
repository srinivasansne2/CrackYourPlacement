class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([max(0, j - i) for i, j in zip(prices, prices[1:])])