class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dp = nums[:]
        for i in range(1, len(nums)):
            self.dp[i] = self.dp[i-1] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        result = 0
        if i - 1 >= 0:
            return self.dp[j] - self.dp[i-1]
        else:
            return self.dp[j]