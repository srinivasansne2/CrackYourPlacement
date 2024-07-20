class Solution:
    def removeDuplicates(self, nums):
        nums[:]= sorted(list(set(nums)))  
        return len(nums)
# First we sorting the list , then we convert into set for removing duplicate