class Solution(object):
    def moveZeroes(self, nums):
        start = 0   # Starting from index 0
        for i in range(len(nums)):  # Creating the loop
            if nums[i] != 0 :       # Checking the index nums is not zero
                nums[start], nums[i] = nums[i], nums[start]  # Here we swaping the index
                start += 1          # Increasing the Index value to check
        return nums 