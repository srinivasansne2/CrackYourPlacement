class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sum = sum(nums)
        self.hashmap = {}

    def update(self, index: int, val: int) -> None:
        self.sum += val - self.nums[index]
        self.nums[index] = val
        self.hashmap = {}

    def sumRange(self, left: int, right: int) -> int:
        if (left, right) in self.hashmap:
            return self.hashmap[(left, right)]
        if right - left > len(self.nums) // 2:
            result = self.sum - sum(self.nums[:left]) - sum(self.nums[right+1:])
        else:
            result = sum(self.nums[left:right + 1])
        self.hashmap[(left, right)] = result
        return result