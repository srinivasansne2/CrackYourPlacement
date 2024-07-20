class Solution(object):
    def findDuplicate(self, nums):
        arr = {}
        for i in nums:
            if i in arr:
                return i
            else:
                arr[i] = 1
        return 0